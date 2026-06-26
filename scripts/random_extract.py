#!/usr/bin/env python3
"""
AI知识库随机抽取脚本
从知识库中随机抽取一篇文章进行讲解
"""

import os
import json
import random
from pathlib import Path
from datetime import datetime, timedelta

BASE_DIR = Path(__file__).parent.parent / "ai-knowledge-base"
INDEX_FILE = Path(__file__).parent.parent / "ai-knowledge-base" / "topics-index.json"
LOG_FILE = Path(__file__).parent.parent / "extraction-log.json"

# 难度权重
DIFFICULTY_WEIGHTS = {
    "beginner": 0.3,
    "intermediate": 0.5,
    "advanced": 0.2
}

def load_index():
    """加载主题索引"""
    if INDEX_FILE.exists():
        with open(INDEX_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"topics": []}

def load_log():
    """加载抽取记录"""
    if LOG_FILE.exists():
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"records": []}

def save_log(log):
    """保存抽取记录"""
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(log, f, ensure_ascii=False, indent=2)

def get_recently_extracted(log, days=7):
    """获取最近N天已抽取的文章"""
    recent = set()
    cutoff = datetime.now() - timedelta(days=days)
    for record in log.get("records", []):
        if record.get("date"):
            try:
                record_date = datetime.fromisoformat(record["date"])
                if record_date > cutoff:
                    recent.add(record.get("path"))
            except:
                pass
    return recent

def filter_by_difficulty(topics, difficulty):
    """按难度筛选"""
    return [t for t in topics if t.get("difficulty") == difficulty]

def select_by_weight(topics):
    """按权重选择"""
    categorized = {d: filter_by_difficulty(topics, d) for d in DIFFICULTY_WEIGHTS.keys()}
    selected_difficulty = random.choices(
        list(DIFFICULTY_WEIGHTS.keys()),
        weights=list(DIFFICULTY_WEIGHTS.values()),
        k=1
    )[0]
    candidates = categorized.get(selected_difficulty, [])
    return random.choice(candidates) if candidates else random.choice(topics)

def random_extract(tag_filter=None):
    """随机抽取一篇文章"""
    index = load_index()
    topics = index.get("topics", [])

    if not topics:
        return None, "知识库为空，请先添加内容"

    # 过滤标签
    if tag_filter:
        topics = [t for t in topics if tag_filter in t.get("tags", [])]

    if not topics:
        return None, f"没有找到标签为 {tag_filter} 的文章"

    # 获取最近已抽取的文章
    log = load_log()
    recently_extracted = get_recently_extracted(log)

    # 优先选择未抽取或超过7天的文章
    not_recent = [t for t in topics if t.get("path") not in recently_extracted]

    if not_recent:
        candidates = not_recent
    else:
        candidates = topics

    selected = select_by_weight(candidates)

    # 记录抽取
    log["records"].append({
        "date": datetime.now().isoformat(),
        "path": selected.get("path"),
        "title": selected.get("title"),
        "difficulty": selected.get("difficulty")
    })
    save_log(log)

    return selected, None

def get_article_content(path):
    """读取文章内容"""
    full_path = BASE_DIR / path
    if full_path.exists():
        with open(full_path, 'r', encoding='utf-8') as f:
            return f.read()
    return None

def format_explanation(topic, content):
    """格式化讲解内容"""
    return f"""📚 今日知识点：{topic['title']}

📖 领域：{topic.get('domain', '通用')}
📊 难度：{topic.get('difficulty', 'intermediate')}
🏷️  标签：{', '.join(topic.get('tags', []))}

## 内容预览
{content[:500]}...

💡 想了解更多？告诉我"讲解更多"或"下一个知识点"
"""

if __name__ == "__main__":
    import sys

    tag = sys.argv[1] if len(sys.argv) > 1 else None

    topic, error = random_extract(tag)

    if error:
        print(f"❌ {error}")
        sys.exit(1)

    content = get_article_content(topic['path'])

    if content:
        print(format_explanation(topic, content))
    else:
        print(f"❌ 无法读取文章：{topic['path']}")

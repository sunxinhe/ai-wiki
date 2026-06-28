#!/usr/bin/env python3
import json
import os
import random
from datetime import datetime, timedelta
from pathlib import Path

KNOWLEDGE_BASE_DIR = "/workspace/ai-knowledge-base"
LOG_FILE = "/workspace/extraction-log.json"
DAYS_TO_EXPIRE = 7

def load_log():
    """加载抽取日志"""
    if not os.path.exists(LOG_FILE):
        return {"extractions": [], "last_updated": datetime.now().isoformat() + "Z"}

    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_log(log_data):
    """保存抽取日志"""
    log_data["last_updated"] = datetime.now().isoformat() + "Z"
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(log_data, f, ensure_ascii=False, indent=2)

def is_recently_extracted(file_path, log_data):
    """检查文章是否在最近7天内被抽取过"""
    cutoff_time = datetime.now() - timedelta(days=DAYS_TO_EXPIRE)

    for extraction in log_data["extractions"]:
        if extraction["file_path"] == file_path:
            extraction_time = datetime.fromisoformat(extraction["timestamp"].replace('Z', '+00:00'))
            if extraction_time.replace(tzinfo=None) > cutoff_time:
                return True
    return False

def get_all_articles():
    """获取所有文章"""
    articles = []
    for root, dirs, files in os.walk(KNOWLEDGE_BASE_DIR):
        for file in files:
            if file.endswith('.md'):
                articles.append(os.path.join(root, file))
    return articles

def extract_article_metadata(file_path):
    """从文章中提取元数据"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    metadata = {
        'title': '',
        'category': '',
        'tags': '',
        'difficulty': '中等'
    }

    lines = content.split('\n')
    for line in lines:
        if line.startswith('# '):
            metadata['title'] = line[2:].strip()
        elif '**分类：**' in line:
            metadata['category'] = line.split('**分类：**')[1].strip()
        elif '**标签：**' in line:
            metadata['tags'] = line.split('**标签：**')[1].strip()

    # 从路径中提取分类（如果元数据中没有）
    if not metadata['category']:
        parts = file_path.split('/')
        for i, part in enumerate(parts):
            if part in ['基础知识', '前沿探索', '学科历史', '工程应用', '随手记']:
                metadata['category'] = part
                break

    return metadata

def format_message(article_path):
    """格式化推送消息"""
    with open(article_path, 'r', encoding='utf-8') as f:
        content = f.read()

    metadata = extract_article_metadata(article_path)

    # 提取各个部分
    sections = {}
    current_section = None
    section_content = []

    lines = content.split('\n')
    for line in lines:
        if line.startswith('## '):
            if current_section:
                sections[current_section] = '\n'.join(section_content).strip()
            current_section = line[3:].strip()
            section_content = []
        elif line.startswith('### ') and current_section:
            section_content.append(line)
        elif current_section:
            section_content.append(line)

    if current_section:
        sections[current_section] = '\n'.join(section_content).strip()

    # 格式化消息
    message = f"""📚 今日知识点：{metadata['title']}
📖 领域：{metadata['category']}
📊 难度：{metadata['difficulty']}
🏷️ 标签：{metadata['tags']}

## 核心概念
{sections.get('概述', sections.get('核心内容', '暂无内容'))}

## 实际应用
{sections.get('关键要点', '暂无内容')}

## 延伸思考
{sections.get('延伸思考', '暂无内容')}

💡 思考：这些知识如何应用到你的工作中？"""

    return message, metadata

def main():
    # 加载日志
    log_data = load_log()

    # 获取所有文章
    all_articles = get_all_articles()

    # 过滤掉最近抽取的文章
    available_articles = [
        article for article in all_articles
        if not is_recently_extracted(article, log_data)
    ]

    if not available_articles:
        print("所有文章都在7天内被抽取过，将重新抽取最近的文章")
        available_articles = all_articles

    # 随机选择一篇文章
    selected_article = random.choice(available_articles)

    # 格式化消息
    message, metadata = format_message(selected_article)

    # 记录抽取
    log_data["extractions"].append({
        "file_path": selected_article,
        "title": metadata['title'],
        "category": metadata['category'],
        "timestamp": datetime.now().isoformat() + "Z"
    })

    # 保存日志
    save_log(log_data)

    print(f"已选择文章: {selected_article}")
    print(f"\n消息内容:\n{message}")

    return message, selected_article

if __name__ == "__main__":
    main()
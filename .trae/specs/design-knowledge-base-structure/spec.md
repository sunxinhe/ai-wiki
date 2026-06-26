# 知识库目录结构设计 Spec

## Why
需要一个通用知识管理系统，按主题分类组织 AI 相关各领域知识、读书笔记、技术文章等内容，便于长期积累和快速检索。

## What Changes
- 新建知识库根目录 `knowledge-base/`
- 按主题划分为 6 个一级目录：AI、技术文章、数据科学、学习资源、模板、归档
- AI 目录按子领域细分为 11 个二级目录
- 技术文章按方向细分为 6 个二级目录
- 提供标准模板（书籍笔记、论文笔记、技术文章、主题笔记）
- 顶层 README 作为知识库导航索引

## Impact
- 新增文件：知识库目录结构 + 模板文件 + README
- 无已有代码受影响

## ADDED Requirements

### Requirement: 一级目录划分
知识库根目录 `knowledge-base/` 下包含以下一级目录：
- `ai/` — AI 相关知识（核心）
- `tech-articles/` — 技术文章（按方向分类）
- `data-science/` — 数据科学基础
- `learning/` — 学习资源（课程、讲座等）
- `templates/` — 笔记模板
- `archives/` — 归档内容

### Requirement: AI 子领域分类
`ai/` 目录下按子领域划分：
- `fundamentals/` — 机器学习、深度学习基础理论
- `nlp/` — 自然语言处理
- `cv/` — 计算机视觉
- `speech/` — 语音识别与合成
- `llm/` — 大语言模型（Transformer、预训练、微调、RLHF）
- `rag/` — RAG 检索增强生成
- `agents/` — AI Agent、工具调用、多智能体
- `prompt-engineering/` — Prompt 工程
- `applications/` — AI 在各领域的应用（医疗、金融、教育等）
- `ethics/` — AI 伦理与安全
- `papers/` — AI 论文阅读笔记

### Requirement: 技术文章分类
`tech-articles/` 目录下按技术方向划分：
- `programming/` — 编程语言相关（Python、Go、Rust、Java 等）
- `system-design/` — 系统设计、分布式、微服务
- `devops/` — DevOps、CI/CD、容器化
- `database/` — 数据库（SQL、NoSQL、向量数据库）
- `cloud/` — 云平台、云原生
- `security/` — 安全相关

### Requirement: 笔记模板
`templates/` 目录提供 4 种标准模板：
- `book-note-template.md` — 书籍读书笔记模板
- `paper-note-template.md` — 论文阅读笔记模板
- `article-note-template.md` — 技术文章笔记模板
- `topic-note-template.md` — 主题知识整理模板

### Requirement: 顶层导航
`knowledge-base/README.md` 作为知识库首页索引，包含：
- 目录结构说明
- 各目录用途简介
- 快速导航链接

## MODIFIED Requirements
无

## REMOVED Requirements
无

# 知识库目录结构设计 Spec

## Why
需要一个通用知识管理系统，按随手记、学科历史、基础知识、工程应用、前沿探索五大板块组织 AI 相关各领域知识、读书笔记、技术文章等内容，便于长期积累和快速检索。

## What Changes
- 新建知识库根目录 `knowledge-base/`
- 按五大板块划分为 5 个一级目录：随手记、学科历史、基础知识、工程应用、前沿探索
- 各一级目录下按具体内容细分二级、三级目录
- 提供标准模板（随手记、书籍笔记、论文笔记、技术文章笔记）
- 顶层 README 作为知识库导航索引

## Impact
- 新增文件：知识库目录结构 + 模板文件 + README
- 无已有代码受影响

## ADDED Requirements

### Requirement: 一级目录划分
知识库根目录 `knowledge-base/` 下包含以下 5 个一级目录：
- `notes/` — 随手记（日常灵感、想法、碎片知识）
- `history/` — 学科历史（AI 发展脉络、重要里程碑、人物传记）
- `fundamentals/` — 基础知识（核心概念、理论基础、数学基础、经典模型）
- `applications/` — 工程应用（实战项目、工具使用、代码实现、最佳实践）
- `frontier/` — 前沿探索（最新研究、论文解读、新兴技术、趋势洞察）

### Requirement: 随手记目录结构
`notes/` 目录下按类型划分：
- `ideas/` — 灵感想法
- `snippets/` — 代码片段、知识碎片
- `questions/` — 问题与思考
- `daily/` — 日常记录

### Requirement: 学科历史目录结构
`history/` 目录下按主题划分：
- `timeline/` — AI 发展时间线
- `milestones/` — 重要里程碑事件
- `pioneers/` — 人物传记与贡献
- `schools/` — 各流派与研究方向演变

### Requirement: 基础知识目录结构
`fundamentals/` 目录下按领域划分：
- `concepts/` — 核心概念与术语
- `math/` — 数学基础（线代、概率、统计、优化）
- `ml/` — 传统机器学习
- `dl/` — 深度学习基础
- `nlp/` — NLP 基础
- `cv/` — 计算机视觉基础

### Requirement: 工程应用目录结构
`applications/` 目录下按场景划分：
- `projects/` — 实战项目
- `tools/` — 工具使用（框架、库、平台）
- `code/` — 代码实现与范例
- `practices/` — 最佳实践与经验总结
- `tutorials/` — 教程与指南

### Requirement: 前沿探索目录结构
`frontier/` 目录下按主题划分：
- `papers/` — 论文阅读笔记
- `research/` — 最新研究动态
- `emerging/` — 新兴技术与方向
- `trends/` — 趋势分析与展望

### Requirement: 笔记模板
`templates/` 目录提供 4 种标准模板：
- `quick-note-template.md` — 随手记模板
- `book-note-template.md` — 书籍读书笔记模板
- `paper-note-template.md` — 论文阅读笔记模板
- `article-note-template.md` — 技术文章笔记模板

### Requirement: 顶层导航
`knowledge-base/README.md` 作为知识库首页索引，包含：
- 五大板块用途说明
- 目录结构树形图
- 快速导航链接

## MODIFIED Requirements
无

## REMOVED Requirements
无

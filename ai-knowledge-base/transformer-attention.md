---
title: Transformer注意力机制
domain: 深度学习
difficulty: 中级
tags: [Transformer, 注意力机制, NLP, 深度学习]
---

# Transformer注意力机制

## 核心概念

Transformer注意力机制是一种让模型能够关注输入序列中不同部分的技术。它通过计算查询(Query)、键(Key)和值(Value)之间的相似度来确定每个位置的权重，从而实现动态的信息聚合。

注意力公式：Attention(Q, K, V) = softmax(QK^T / √d_k)V

其中：
- Q (Query): 查询矩阵
- K (Key): 键矩阵
- V (Value): 值矩阵
- d_k: 键的维度

## 实际应用

1. **机器翻译**: Transformer模型在各种翻译任务中取得了突破性成果
2. **文本生成**: GPT系列模型基于Transformer架构
3. **图像处理**: Vision Transformer将注意力机制引入计算机视觉
4. **语音识别**: Whisper等模型使用Transformer进行语音处理

## 举个例子

假设翻译句子 "The cat sat on the mat" 到中文：

在处理 "sat" 这个词时，注意力机制会计算它与句子中其他词的相关性：
- 与 "cat" 的关联度高（谁在坐）
- 与 "mat" 的关联度高（坐在哪里）
- 与 "the" 的关联度较低

这样模型就能准确理解 "sat" 的上下文含义，生成准确的翻译。

## 思考问题

为什么Transformer中使用缩放因子 √d_k？如果不使用缩放，会发生什么问题？
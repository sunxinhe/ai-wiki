# Transformer架构

## 背景

Transformer是2017年由Google在论文《Attention Is All You Need》中提出的革命性架构，它完全基于**注意力机制（Attention Mechanism）**，摒弃了传统的RNN和CNN结构，成为现代大语言模型（LLM）的基石。

## 核心组件

### 1. 自注意力机制（Self-Attention）

自注意力让序列中的每个位置都能关注到序列中的所有其他位置，从而捕获长距离依赖关系。

```
计算流程：
1. 输入 → 三个向量：Query(Q)、Key(K)、Value(V)
2. 计算注意力分数：score = Q · K^T / √d
3. Softmax归一化
4. 加权求和：output = Σ(attention_weights × V)
```

### 2. 多头注意力（Multi-Head Attention）

将注意力机制并行运行多次，捕获不同类型的依赖关系：

```
每个头独立计算：
- 头1：句法关系
- 头2：语义关系
- 头3：位置关系
...
最终拼接所有头的输出
```

### 3. 位置编码（Positional Encoding）

由于Transformer没有循环结构，需要显式注入位置信息：

```python
# 位置编码公式
PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
```

### 4. 前馈神经网络（FFN）

每个Transformer层包含两层全连接网络：

```
FFN(x) = max(0, xW₁ + b₁)W₂ + b₂
```

## Transformer编码器-解码器结构

```
输入 → 编码器栈 → 解码器栈 → 输出

编码器（处理输入）：
- Multi-Head Self-Attention
- Feed Forward
- 残差连接 + Layer Norm

解码器（生成输出）：
- Masked Self-Attention
- Cross Attention（关注编码器输出）
- Feed Forward
```

## GPT系列 vs BERT

| 特性 | GPT | BERT |
|------|-----|------|
| 架构 | Decoder-only | Encoder-only |
| 训练方式 | 自回归 | 掩码语言模型 |
| 任务适用 | 生成任务 | 理解任务 |
| 代表模型 | GPT-4 | BERT |

## Transformer的变体

1. **BERT**：双向编码器表示
2. **GPT**：生成式预训练
3. **T5**：Text-to-Text转换器
4. **ViT**：Vision Transformer

## 关键优势

- **并行计算**：克服RNN的顺序计算限制
- **长距离依赖**：直接建模任意距离的关系
- **可扩展性**：易于堆叠更多层

## 思考问题

1. Transformer相比RNN的主要优势是什么？
2. 为什么需要多头注意力而不是单头？

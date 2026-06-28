# Transformer架构

> **分类：** 基础知识
> **标签：** 深度学习, NLP, 注意力机制, 神经网络
> **创建时间：** 2026-06-15

## 概述
Transformer是一种基于自注意力机制的神经网络架构,彻底改变了自然语言处理领域,成为现代大语言模型的基石。

## 核心内容

### 自注意力机制
Transformer的核心创新在于自注意力机制(Self-Attention),它允许模型在处理序列时,动态关注序列中的不同部分。具体计算公式为:

```
Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V
```

其中Q、K、V分别代表Query、Key、Value三个矩阵。

### 编码器-解码器结构
原始Transformer包含两个部分:
- **编码器(Encoder)**: 由N个相同的层堆叠而成,每层包含多头自注意力和前馈网络
- **解码器(Decoder)**: 同样由N层堆叠,增加了掩码机制防止信息泄露

### 位置编码
由于Transformer没有循环结构,需要通过位置编码来注入序列的位置信息:

```
PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
```

## 关键要点
- 自注意力机制使模型能并行处理整个序列,相比RNN大幅提升训练效率
- 多头注意力允许模型在不同表示子空间中关注信息
- 位置编码为序列注入位置信息,弥补了并行处理的不足
- Transformer已成为GPT、BERT等主流大模型的基础架构

## 延伸思考
Transformer的自注意力机制的时间复杂度为O(n²),在处理超长序列时会遇到性能瓶颈。如何改进这一限制?Vision Transformer(ViT)如何将Transformer应用于图像领域?
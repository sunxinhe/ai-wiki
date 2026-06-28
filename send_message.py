#!/usr/bin/env python3
"""
直接调用飞书API发送消息
"""
import requests
import json
import os

# 从环境中获取token
USER_ACCESS_TOKEN = os.getenv('LARKSUITE_CLI_USER_ACCESS_TOKEN', '')
APP_ID = os.getenv('LARKSUITE_CLI_APP_ID', '')

CHAT_ID = "oc_79cd434fbd4f8fcd31eb21038dc7ca19"

def send_message(token):
    """发送消息"""
    url = "https://open.feishu.cn/open-apis/im/v1/messages"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # 构造post格式的消息
    post_content = {
        "zh_cn": {
            "title": "📚 今日知识点：Transformer架构",
            "content": [
                [
                    {"tag": "text", "text": "📖 领域：基础知识\n📊 难度：中等\n🏷️ 标签：深度学习, NLP, 注意力机制, 神经网络\n\n"}
                ],
                [
                    {"tag": "text", "text": "## 核心概念\n"}
                ],
                [
                    {"tag": "text", "text": "Transformer是一种基于自注意力机制的神经网络架构,彻底改变了自然语言处理领域,成为现代大语言模型的基石。\n\n"}
                ],
                [
                    {"tag": "text", "text": "## 实际应用\n"}
                ],
                [
                    {"tag": "text", "text": "• 自注意力机制使模型能并行处理整个序列,相比RNN大幅提升训练效率\n"}
                ],
                [
                    {"tag": "text", "text": "• 多头注意力允许模型在不同表示子空间中关注信息\n"}
                ],
                [
                    {"tag": "text", "text": "• 位置编码为序列注入位置信息,弥补了并行处理的不足\n"}
                ],
                [
                    {"tag": "text", "text": "• Transformer已成为GPT、BERT等主流大模型的基础架构\n\n"}
                ],
                [
                    {"tag": "text", "text": "## 延伸思考\n"}
                ],
                [
                    {"tag": "text", "text": "Transformer的自注意力机制的时间复杂度为O(n²),在处理超长序列时会遇到性能瓶颈。如何改进这一限制?Vision Transformer(ViT)如何将Transformer应用于图像领域?\n\n"}
                ],
                [
                    {"tag": "text", "text": "💡 思考：这些知识如何应用到你的工作中？"}
                ]
            ]
        }
    }

    data = {
        "receive_id": CHAT_ID,
        "msg_type": "post",
        "content": json.dumps(post_content)
    }

    params = {"receive_id_type": "chat_id"}

    response = requests.post(url, headers=headers, params=params, json=data)
    result = response.json()

    return result

def main():
    if not USER_ACCESS_TOKEN:
        print("❌ 未找到USER_ACCESS_TOKEN环境变量")
        return

    print(f"使用APP_ID: {APP_ID}")
    print(f"使用USER_ACCESS_TOKEN (长度: {len(USER_ACCESS_TOKEN)})")

    result = send_message(USER_ACCESS_TOKEN)

    if result.get("code") == 0:
        print("✅ 消息发送成功!")
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("❌ 消息发送失败")
        print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
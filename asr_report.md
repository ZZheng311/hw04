# 开源语音识别（ASR）方案对比报告
## 对比方案：Whisper / Vosk / FunASR

## 1. OpenAI Whisper
- 仓库：https://github.com/openai/whisper
- 协议：MIT
- 语言支持：99种语言，支持中文普通话
- 模型大小：tiny ~ large（多档可选）
- 推理速度：PC笔记本极快
- 流式支持：不支持
- 部署难度：极低
- 实测：安装简单、识别准、适合本地作业

## 2. Vosk
- 仓库：https://github.com/alphacep/vosk-api
- 协议：Apache 2.0
- 语言支持：多语言
- 模型小、速度极快
- 支持流式
- 部署简单

## 3. FunASR
- 仓库：https://github.com/modelscope/FunASR
- 协议：MIT
- 中文识别超强
- 模型较大
- 部署稍复杂

## 最终选型
选择 **OpenAI Whisper**
理由：安装最简单、笔记本可直接运行、支持文件识别、满足作业要求。

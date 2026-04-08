import whisper
import os
import subprocess

# 1. 先检查 ffmpeg 是否安装成功
def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        print("✅ ffmpeg 已安装，可正常解码音频")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ ffmpeg 未安装！请先安装 ffmpeg 才能运行 Whisper")
        return False

# 2. 检查环境
if not check_ffmpeg():
    raise RuntimeError("请先安装 ffmpeg 后再运行")

try:
    print("✅ whisper 导入成功，版本：", whisper.__version__)
except ImportError:
    print("❌ whisper 未安装，请先运行 !pip install openai-whisper torch")
    raise

# 3. 加载模型（第一次运行会自动下载tiny模型，耐心等待）
model = whisper.load_model("tiny")

# 4. 音频路径（推荐用绝对路径，r前缀避免转义）
AUDIO_PATH = r"D:/人工智能通识/hw04/audio/output.mp3"

# 5. 双重验证：文件存在 + 可读取
if not os.path.exists(AUDIO_PATH):
    print(f"❌ 音频文件不存在！路径：{AUDIO_PATH}")
else:
    print(f"✅ 音频文件存在，开始识别...")
    try:
        # 中文识别，指定 language="zh" 准确率更高
        result = model.transcribe(AUDIO_PATH, language="zh")
        
        # 输出结果
        print("\n📝 识别结果：")
        print(result["text"])
        
        # 保存结果（用绝对路径，避免找不到文件）
        save_path = r"D:/人工智能通识/hw04/result.txt"
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(result["text"])
        print(f"\n✅ 结果已保存到：{save_path}")
    except Exception as e:
        print(f"\n❌ 识别失败，错误信息：{str(e)}")
        print("请检查：1. ffmpeg是否安装 2. 音频文件是否损坏 3. 路径是否正确")

from faster_whisper import WhisperModel
import soundfile as sf
import numpy as np

# Загружаем модель
model = WhisperModel("small", device="cpu", compute_type="int8")

# Загружаем запись
audio, rate = sf.read("debug_record.wav")
print(f"✅ Файл загружен: {audio.shape}, rate: {rate}")

if rate != 16000:
    print("⚠️ Неверная частота дискретизации!")
    exit()

# Убедимся, что один канал
if len(audio.shape) == 2:
    audio = audio[:, 0]

# Прогон через модель
segments, _ = model.transcribe(audio, language="ru", beam_size=1)

for segment in segments:
    print(f"🗣️ [{segment.start:.2f}s - {segment.end:.2f}s]: {segment.text}")

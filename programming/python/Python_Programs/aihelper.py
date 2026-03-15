import os
import subprocess
import sounddevice as sd
import queue
import time
import numpy as np
import pyttsx3
import webbrowser
import psutil
import threading
import keyboard
import vlc
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from faster_whisper import WhisperModel
from ollama import chat as ollama_chat
from duckduckgo_search import DDGS

# === НАСТРОЙКИ ===
WAKE_WORDS = ["hello"]
HOTKEY = "shift+y"
SAMPLE_RATE = 16000
CHANNELS = 1
MODEL_NAME = "tiny"
OLLAMA_MODEL = "mistral"
DING_PATH = "ding.mp3"

# === SPOTIFY ===
SPOTIPY_CLIENT_ID = "f13f5ebb2f5f41d89eec581669a7d833"
SPOTIPY_CLIENT_SECRET = "3c1286fb06d04ba9a3c78e1e8e5c9d94"
SPOTIPY_REDIRECT_URI = "http://127.0.0.1:8888/callback"
SCOPE = "user-read-playback-state,user-modify-playback-state,playlist-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=SCOPE
))

# === ГОЛОС ===
engine = pyttsx3.init()
engine.setProperty("rate", 170)

def speak(text):
    print(f"\n🤖: {text}\n")
    engine.say(text)
    engine.runAndWait()

def play_ding():
    player = vlc.MediaPlayer(DING_PATH)
    player.play()
    time.sleep(0.6)
    player.stop()

# === МОДЕЛЬ РАСПОЗНАВАНИЯ ===
model = WhisperModel(MODEL_NAME, device="cpu", compute_type="int8")
q = queue.Queue()

def callback(indata, frames, time_, status):
    q.put(indata.copy())

def listen_and_transcribe(timeout=5):
    with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS, blocksize=256, dtype='int16', callback=callback):
        print("🎤 Говорите...")
        audio = []
        start = time.time()
        while time.time() - start < timeout:
            try:
                audio.append(q.get(timeout=1))
            except queue.Empty:
                continue

    if not audio:
        return ""

    audio_np = np.concatenate(audio, axis=0)

    MAX_DURATION = 5
    max_samples = int(SAMPLE_RATE * MAX_DURATION)
    if len(audio_np) > max_samples:
        print(f"⚠️ Аудио длиннее {MAX_DURATION} секунд, обрезаю.")
        audio_np = audio_np[:max_samples]

    try:
        audio_norm = audio_np.astype(np.float32) / 32768.0
        segments, _ = model.transcribe(audio_norm, beam_size=1)
        text = ' '.join(segment.text for segment in segments).strip().lower()
        print(f"📝 Распознано: {text}")
        return text
    except Exception as e:
        print(f"❌ Ошибка при расшифровке: {e}")
        return ""

# === ОБРАБОТКА КОМАНД ===
def ask_ollama(prompt):
    response = ollama_chat(model=OLLAMA_MODEL, messages=[
        {"role": "system", "content": "Ты помощник. Отвечай кратко и по-русски."},
        {"role": "user", "content": prompt}
    ])
    return response["message"]["content"]

def search_duckduckgo(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=1))
            if results:
                return results[0]["body"]
    except Exception as e:
        print("🔍 Ошибка поиска:", e)
    return None

def launch_application(app_name):
    for proc in psutil.process_iter(['name']):
        if app_name.lower() in proc.info['name'].lower():
            speak(f"{app_name} уже запущен.")
            return

    search_dirs = [
        "C:/Program Files",
        "C:/Program Files (x86)",
        f"C:/Users/{os.getlogin()}/AppData/Local"
    ]

    for base in search_dirs:
        for root, _, files in os.walk(base):
            for file in files:
                if file.lower().endswith(".exe") and app_name.lower() in file.lower():
                    try:
                        subprocess.Popen(os.path.join(root, file))
                        speak(f"Открываю {app_name}")
                        return
                    except Exception as e:
                        print(f"❌ Не удалось запустить {file}: {e}")

    speak(f"Программа {app_name} не найдена.")

def handle_spotify_command(command):
    if "включи спотифай" in command:
        launch_application("Spotify")
        return True
    if "включи следующий" in command:
        sp.next_track()
        speak("Следующий трек")
        return True
    if "предыдущий" in command:
        sp.previous_track()
        speak("Предыдущий трек")
        return True
    if "пауза" in command:
        sp.pause_playback()
        speak("Пауза")
        return True
    if "продолжи музыку" in command:
        sp.start_playback()
        speak("Продолжаю")
        return True
    if "включи плейлист" in command:
        name = command.split("включи плейлист")[-1].strip()
        results = sp.current_user_playlists()
        for playlist in results['items']:
            if name.lower() in playlist['name'].lower():
                sp.start_playback(context_uri=playlist['uri'])
                speak(f"Включаю плейлист {playlist['name']}")
                return True
        speak("Плейлист не найден")
        return True
    return False

def process_command(command):
    print(f"⚙️ Обработка команды: {command}")

    if handle_spotify_command(command):
        return

    if command.startswith("открой в браузере") or "включи видео" in command:
        query = command.replace("открой в браузере", "").replace("включи видео", "").strip()
        if query:
            url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(url)
            speak("Открываю в браузере")
        else:
            speak("Что открыть?")
        return

    if command.startswith("открой") or command.startswith("запусти"):
        app = command.replace("открой", "").replace("запусти", "").strip()
        if app:
            launch_application(app)
        else:
            speak("Какую программу открыть?")
        return

    result = search_duckduckgo(command)
    if result:
        speak(result)
    else:
        response = ask_ollama(command)
        speak(response)

# === ГЛАВНЫЙ ЦИКЛ ===
def assistant_loop():
    print(f"🔁 Ожидание активации ('{' / '.join(WAKE_WORDS)}' или {HOTKEY})...")
    while True:
        text = listen_and_transcribe(timeout=5)
        if any(w in text for w in WAKE_WORDS):
            print("✅ Активация!")
            play_ding()
            speak("Слушаю")
            user_command = listen_and_transcribe(timeout=7)
            print(f"🎙️ Команда пользователя: {user_command}")
            if user_command:
                process_command(user_command)
            else:
                speak("Не услышал команду. Попробуй ещё раз.")

# === ГОРЯЧАЯ КЛАВИША ===
def hotkey_listener():
    def on_hotkey():
        play_ding()
        speak("Слушаю")
        user_command = listen_and_transcribe(timeout=7)
        print(f"🎙️ Команда пользователя: {user_command}")
        if user_command:
            process_command(user_command)
        else:
            speak("Не услышал команду. Попробуй ещё раз.")
    keyboard.add_hotkey(HOTKEY, on_hotkey)
    keyboard.wait()

# === ЗАПУСК ===
if __name__ == "__main__":
    threading.Thread(target=hotkey_listener).start()
    assistant_loop()

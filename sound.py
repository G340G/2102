import pyttsx3
import numpy as np
import wave
import random

def generate_tts(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 120)
    engine.setProperty("voice", engine.getProperty("voices")[0].id)
    engine.save_to_file(text[:500], "voice.wav")
    engine.runAndWait()

def generate_noise(duration=6):
    sr = 44100
    t = np.linspace(0, duration, sr*duration)
    noise = np.random.normal(0,0.2,sr*duration)
    hum = 0.3*np.sin(2*np.pi*50*t)
    data = noise + hum

    with wave.open("noise.wav","w") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(sr)
        f.writeframes((data*32767).astype(np.int16))

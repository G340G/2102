import numpy as np
import wave

def generate_noise():
    sr = 44100
    t = np.linspace(0, 5, sr*5)
    noise = np.random.normal(0,0.3,sr*5)
    tone = 0.3*np.sin(2*np.pi*55*t)
    audio = noise + tone

    with wave.open("generator/audio.wav","w") as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(sr)
        f.writeframes((audio*32767).astype(np.int16))

import sounddevice as sd
import numpy as np

print("Program started")

def audio_callback(indata, frames, time, status):
    rms = np.sqrt(np.mean(np.square(indata)))
    print(f"{rms:.4f}")

print("Opening stream...")

with sd.InputStream(device=2, callback=audio_callback):
    print("Stream opened")
    input("Listening... Press Enter to stop.\n")






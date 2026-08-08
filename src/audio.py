import numpy as np
import sounddevice as sd


current_rms = 0.0


def audio_callback(indata, frames, time, status):
    global current_rms

    if status:
        print(status)

    current_rms = np.sqrt(np.mean(indata ** 2))
# Guitar Visualiser 🎸

A real-time guitar visualizer built with Python. The goal is to analyze live guitar audio and create visuals that react to loudness, pitch, and other musical features.

---

## Roadmap

- [x] Capture live audio
- [x] Measure loudness (RMS)
- [ ] Draw first circle
- [ ] Animate circle with loudness
- [ ] Detect pitch
- [ ] Map pitch to colors
- [ ] Draw waveform
- [ ] Draw frequency spectrum (FFT)
- [ ] Support guitar amp input
- [ ] Audio device selector
- [ ] Final UI polish

---

## Development Log

### Day 1

#### Completed
- Created the project structure.
- Set up the Python virtual environment.
- Installed the required libraries.
- Learned the basic Git workflow (`git add`, `git commit`, `git push`).
- Captured live microphone input using `sounddevice`.
- Calculated real-time loudness using RMS.
- Verified the audio pipeline by detecting a clap.

#### Learned
- Audio arrives as chunks of samples.
- `indata` is a NumPy array with shape `(samples, channels)`.
- RMS is a standard way to measure loudness from raw audio.
# Guitar Audio Visualizer

A real-time audio visualizer that converts guitar sounds into visual elements.

The project takes audio input from a guitar/microphone, analyzes the incoming signal, and generates visual circles based on the characteristics of the sound. The long-term goal is to turn guitar playing into an evolving digital "paint splash" visualization.

## Project Status

**In progress**

The basic audio input and visualization pipeline is working. The current version can detect guitar sound, create circles based on the sound level, place them randomly on the screen, and gradually shrink them over time.

## Current Features

- Real-time audio input using `sounddevice`
- RMS-based audio amplitude detection
- Audio smoothing to reduce sudden visual jumps
- Normalization of audio levels
- Threshold-based sound detection
- Circles generated in response to audio
- Circle size based on the loudness of the detected sound
- Random positioning of circles
- Independent shrinking of each circle
- Multiple circles can exist on screen simultaneously

## How It Currently Works

The current pipeline is:

Audio Input  
↓  
RMS Calculation  
↓  
Smoothing  
↓  
Normalization  
↓  
Sound/Note Detection  
↓  
Circle Generation  
↓  
Pygame Visualization

Each detected sound event creates a new circle. The circle's initial size depends on the detected audio level, and it gradually shrinks after being created.

## Technologies Used

- Python
- NumPy
- SoundDevice
- Pygame
- Git / GitHub

## Project Structure

```text
guitar-audio-visualizer/
│
├── src/
│   ├── audio.py
│   └── visualizer.py
│
├── README.md
└── ...

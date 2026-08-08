import pygame
import sounddevice as sd
import audio

pygame.init()

stream = sd.InputStream(callback=audio.audio_callback)
stream.start()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Guitar Visualiser")

running = True

MIN_RMS = 0.01
MAX_RMS = 0.10

smooth_rms = 0.0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    smooth_rms = smooth_rms * 0.85 + audio.current_rms * 0.15

    if smooth_rms > MIN_RMS:
        normalized = (smooth_rms - MIN_RMS) / (MAX_RMS - MIN_RMS)
        normalized = max(0, min(normalized, 1))

        radius = int(20 + normalized * (150 - 20))

        print(f"RMS: {audio.current_rms:.6f} | Radius: {radius}")

        pygame.draw.circle(
            screen,
            (255, 255, 255),
           (400, 300),
             radius
    )

    pygame.display.flip()

pygame.quit()
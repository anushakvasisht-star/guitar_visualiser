import pygame
import sounddevice as sd
import audio

pygame.init()

stream = sd.InputStream(callback=audio.audio_callback)
stream.start()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Guitar Visualiser")

running = True

smooth_rms = 0.0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    smooth_rms = smooth_rms * 0.85 + audio.current_rms * 0.15
    radius = int(smooth_rms * 50)

    if radius > 10:
        print(f"RMS: {audio.current_rms:.6f} | Radius: {radius}")

    pygame.draw.circle(
        screen,
        (255, 255, 255),
        (400, 300),
        radius
    )

    pygame.display.flip()

pygame.quit()
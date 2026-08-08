import pygame
import sounddevice as sd
import audio
import random

pygame.init()

stream = sd.InputStream(callback=audio.audio_callback)
stream.start()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Guitar Visualiser")

running = True

MIN_RMS = 0.01
MAX_RMS = 0.10

MIN_RADIUS = 20
MAX_RADIUS = 150

smooth_rms = 0.0
circles = []
was_above_threshold = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    smooth_rms = smooth_rms * 0.85 + audio.current_rms * 0.15

    is_above_threshold = smooth_rms > MIN_RMS

    if is_above_threshold and not was_above_threshold:

        normalized = (smooth_rms - MIN_RMS) / (MAX_RMS - MIN_RMS)
        normalized = max(0, min(normalized, 1))

        radius = int(
            MIN_RADIUS
            + normalized * (MAX_RADIUS - MIN_RADIUS)
        )

        circles.append({
            "x": random.randint(50, 750),
            "y": random.randint(50, 550),
            "radius": radius,
            "shrink_speed": 0.5
        })

        print(
            f"RMS: {smooth_rms:.6f} | "
            f"New circle radius: {radius}"
        )

    was_above_threshold = is_above_threshold

    for circle in circles:
        circle["radius"] -= circle["shrink_speed"]

    for circle in circles:
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (circle["x"], circle["y"]),
            int(circle["radius"])
        )

    pygame.display.flip()

pygame.quit()
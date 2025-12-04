import time
import threading
import pygame
from rich import print
import signal
import sys

def sonarMusic():
    pygame.mixer.init()
    pygame.mixer.music.load("Rock That Body.mp3") #nombre de la cancion
    pygame.mixer.music.play()

def printLetra():
    lines =[
        ("♫  ♫  ♫", 10.0,"yellow"),
        ("♫  ♫", 6.0,"bright_yellow"),
        ("(I wanna, I wanna rock right now)", 1.8,"bright_yellow"),
        ("(I wanna, I wanna rock right now)", 1.8,"bright_yellow"),
        ("(I wanna, I wanna rock right now)", 1.8,"bright_yellow"),
        ("(now, now, rock right now)", 2.0,"bright_yellow"),
        ("(I wanna, I wanna rock right now)", 1.9,"bright_yellow"),
        ("(I wanna, I wanna rock right now)", 1.9,"bright_yellow"),
        ("(I wanna, I wanna rooock riiightt nooow)", 4.1,"bright_yellow"),
        ("I wanna da-", 1.8, "bright_yellow"),
        ("I wanna dance in the lights", 2.1, "bright_yellow"),#Hasta aca va bien
        ("I wanna rock-", 1.9,"bright_yellow"),
        ("I wanna rock your body", 1.9,"bright_yellow"),
        ("I wanna go", 1.9,"bright_yellow"),
        ("I wanna go for a ride", 2.0, "bright_yellow"),
        ("Hop in the music and", 1.9, "bright_yellow"),
        ("Rock your body", 1.8,"bright_yellow"),
        ("Rock that body", 1.7,"bright_yellow"),
        ("come on, come on", 1.5,"bright_yellow"),
        ("Rock that body", 1.6,"bright_yellow"),
        ("(Rock your body)", 1.7,"bright_yellow"),
        ("Rock that body", 1.8, "bright_yellow"),
        ("come on, come on", 0.5,"bright_yellow"),
        ("Rock that body", 0.8,"bright_yellow")
    ]

    for line, delay, color in lines:
        print(f"[{color}]{line}[/{color}]")
        time.sleep(delay)

def cierre(sig, frame):
    print("\n[red]Deteniendo musica...[\red]")
    pygame.mixer.music.stop()
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler=exit)
    threading.Thread(target=sonarMusic, daemon=True).start()
    printLetra()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
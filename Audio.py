import pyttsx3
import pyautogui
import speedtest


def Voice(x):
    engine = pyttsx3.init()
    engine.say(x)
    engine.runAndWait()

def Screenshot(sc):
    screenshot = pyautogui.screenshot()
    screenshot.save(sc+'.png')




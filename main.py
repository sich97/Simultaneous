import pyautogui
import time


def main():
    pyautogui.PAUSE = 0.0

    time.sleep(5)
    first_spot = pyautogui.position()

    time.sleep(5)
    second_spot = pyautogui.position()

    time.sleep(5)
    pyautogui.leftClick(first_spot)
    pyautogui.leftClick(second_spot)


if __name__ == "__main__":
    main()

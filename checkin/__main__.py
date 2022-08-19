import pyautogui
import time
from datetime import datetime, timedelta
import argparse

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("date_goal", 
                        help="eg: 2022/08/20 14:21")
    parser.add_argument("--text", 
                        default=None,
                        help="eg: Back to working now.")
    args = parser.parse_args()
    date_goal = args.date_goal
    delta = datetime.strptime(date_goal, "%Y/%m/%d %H:%M")-datetime.now()

    # Setup the position on a checkin button
    for t in list(range(10))[::-1]:
        print(f"({delta.total_seconds()}) {t} - {pyautogui.position()} Put the mouse on the button")
        time.sleep(1)
    position_button = pyautogui.position()

    # Setup the position on a text field position
    for t in list(range(10))[::-1]:
        print(f"({delta.total_seconds()}) {t} - {pyautogui.position()} Put the mouse on the text field")
        time.sleep(1)
    position_text = pyautogui.position()

    # Counter
    while delta.total_seconds()>0:
        delta = datetime.strptime(date_goal, "%Y/%m/%d %H:%M")-datetime.now()
        print(delta)
        time.sleep(1)

    # KOT - Click on the checkin button
    pyautogui.moveTo(position_button)
    pyautogui.click()

    # Teams - Input text in the text field (if no text paste from the clipboard)
    pyautogui.moveTo(position_text)
    pyautogui.click()
    if args.text is None:
        pyautogui.hotkey("ctrl", "v")
    else:
        pyautogui.write(args.text)
    pyautogui.hotkey('enter')


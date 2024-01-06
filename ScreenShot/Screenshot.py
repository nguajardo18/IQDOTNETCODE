import os
import pyautogui
import logging
import argparse
import time
from datetime import datetime
from PIL import ImageGrab

def generate_timestamp():
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    return timestamp

def capture_custom_area(save_path, x1, y1, x2, y2, filename):
    try:
        timestamp = generate_timestamp()
        full_save_path = os.path.join(save_path, f"{timestamp}_{filename}")

        pyautogui.moveTo(x1, y1)
        time.sleep(1)

        screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        screenshot.save(full_save_path)

        success_message = f"\nCustom screenshot taken and saved to {full_save_path}"
        logging.info(success_message)
    except OSError as e:
        logging.error(f"An error occurred while saving the screenshot: {e}")
    except pyautogui.FailSafeException as e:
        logging.error(f"PyAutoGUI failsafe exception: {e}")
    except KeyboardInterrupt:
        logging.info("Screenshot capture interrupted by the user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Capture and save a custom area screenshot.")
    parser.add_argument("--filename", help="Specify the filename for saving the screenshot.", default="custom_screenshot.png")
    args = parser.parse_args()

    user_home = os.path.expanduser("~")
    save_path = os.path.join(user_home, "Pictures")

    # Calculate coordinates for capturing a central 600x600 area
    width = 600
    height = 600

    screen_width, screen_height = pyautogui.size()
    x1 = (screen_width - width) // 2
    y1 = (screen_height - height) // 2
    x2 = x1 + width
    y2 = y1 + height

    logging.basicConfig(filename='custom_screenshot.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s: %(message)s')

    capture_custom_area(save_path, x1, y1, x2, y2, args.filename)
#IQDOTNET CODE - By Nelson Guajardo
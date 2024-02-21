import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
import cv2
import time
import re
import pyautogui

from PIL import ImageGrab

from fetchStats import fetchStats
from statsWindowQt5 import CreateMainWindow, getInfoFromQueue, QApplication
from identification import onscreen, putInfoinQueue
# from PyQt6.QtGui import QScreen (possible 2nd monitor support)


def main():
    # Gets the most up to date full list of augment Names and avg placement (above diamond) from tactics.tools and stores it in a local SQLite3 database
    fetchStats()

    # Gets the screen size for resolution to accommodate 4K and 1080p resolutions

    screen_size = pyautogui.size()

    # This is the app that runs the visual GUI display of Augment Stats using PyQt5
    app = QApplication([])
    # Sets the stylesheet of the application (colors table blue and text white etc.)
    app.setStyleSheet("""
        QTableView {
            background-color: #0d3868;
            /* background-color: #0f1720; */
            /* gridline-color: #f7fbff; */ 
            gridline-color: #0095ff13;
            color: #eaf6ff; 
            /* font-size: 20px; */
            font-size: 16px;
        }
    """)
    # For the first time window creation on 2-1, does a check to call CreateWindow which requires window=None (could be written another way)
    window = None
    if screen_size[0] == 1920 and screen_size[1] == 1080:
        print("1080p screen resolution")

        # 2-1 Augment Selection
        while not onscreen("./captures/1080p2-1.png"):
            time.sleep(2)

        if onscreen("./captures/1080p2-1.png"):
            while onscreen("./captures/tft_overlay_highlighted_reroll.png") or onscreen("./captures/tft_overlay_used_reroll.png"):
                data = putInfoinQueue(2)
                if window is None:
                    window = CreateMainWindow(data, 2, screen_size[0], screen_size[1])
                else:
                    getInfoFromQueue(data, window, 2)
                    print("reaches inside else of 2-1 while loop")
            
        # Prints waiting and closes the window since 2-1 augment selection phase is over
        print("waiting for 3-2")
        window.updateTable("hide", 3)

        while not onscreen("./captures/1080p3-2.png"):
            time.sleep(2)    

        window.updateTable("show", 3)
        if onscreen("./captures/1080p3-2.png"):
            while onscreen("./captures/tft_overlay_highlighted_reroll.png") or onscreen("./captures/tft_overlay_used_reroll.png"):
                data = putInfoinQueue(3)
                getInfoFromQueue(data, window, 3)
                print("reaches inside else of 3-2 while loop")
                
        # Prints waiting and closes the window since 3-2 augment selection phase is over and hides the statsWindow
        print("waiting for 4-2")
        window.updateTable("hide", 4)

        while not onscreen("./captures/1080p4-2.png"):
            time.sleep(2)

        window.updateTable("show", 4)
        if onscreen("./captures/1080p4-2.png"):
            while onscreen("./captures/tft_overlay_highlighted_reroll.png") or onscreen("./captures/tft_overlay_used_reroll.png"):
                data = putInfoinQueue(4)
                getInfoFromQueue(data, window, 4)
                print("reaches inside else of 4-2 while loop")
                
        print("finished last augment")
        window.close()
    elif screen_size[0] == 3840 and screen_size[1] == 2160:
        # Currently we have not tested 4K window support, these image and statsWindowPosition values are rough estimates and will produce bugs
        # Feel free to change this if your resolution is 4K
        print("4k screen resloution")

        while not onscreen("./captures/2-1.png"):
            print("sleeping")
            time.sleep(2)

        stage_two_augment_one_val = ""
        stage_two_augment_two_val = ""
        stage_two_augment_three_val = ""
        if onscreen("./captures/2-1.png"):
            augments_ss = ImageGrab.grab(bbox = (903, 1080, 1403, 1130))
            augments_ss.save("stage_two_first_augment.png")
            augments_ss.close()
            stage_two_augment_one_img = cv2.imread("stage_two_first_augment.png")
            stage_two_augment_one_text = pytesseract.image_to_string(stage_two_augment_one_img)
            #print(re.sub(r'\b\w{1,2}\b', '', stage_two_augment_one_text))

            augments_ss = ImageGrab.grab(bbox = (1693, 1080, 2193, 1130))
            augments_ss.save("stage_two_second_augment.png")
            augments_ss.close()
            stage_two_augment_two_img = cv2.imread("stage_two_second_augment.png")
            stage_two_augment_two_text = pytesseract.image_to_string(stage_two_augment_two_img)
            #print(re.sub(r'\b\w{1,2}\b', '', stage_two_augment_two_text))

            augments_ss = ImageGrab.grab(bbox = (2503, 1080, 3003, 1130))
            augments_ss.save("stage_two_third_augment.png")
            augments_ss.close()
            stage_two_augment_three_img = cv2.imread("stage_two_third_augment.png")
            stage_two_augment_three_text = pytesseract.image_to_string(stage_two_augment_three_img)
            #print(re.sub(r'\b\w{1,2}\b', '', stage_two_augment_three_text))

            stage_two_augment_one_text = re.sub(r'\b\w{1,2}\b', '', stage_two_augment_one_text)
            stage_two_augment_two_text = re.sub(r'\b\w{1,2}\b', '', stage_two_augment_two_text)
            stage_two_augment_three_text = re.sub(r'\b\w{1,2}\b', '', stage_two_augment_three_text)

            if stage_two_augment_one_text != stage_two_augment_one_val or stage_two_augment_two_text != stage_two_augment_two_val or stage_two_augment_three_text != stage_two_augment_three_val:
                print(stage_two_augment_one_text)
                stage_two_augment_one_val = stage_two_augment_one_text
                print(stage_two_augment_two_text)
                stage_two_augment_two_val = stage_two_augment_two_text
                print(stage_two_augment_three_text)
                stage_two_augment_three_val = stage_two_augment_three_text

            time.sleep(0.5)
            

        while not onscreen("./captures/3-2.png"):
            time.sleep(2)    

        stage_three_augment_one_val = ""
        stage_three_augment_two_val = ""
        stage_three_augment_three_val = ""
        if onscreen("./captures/3-2.png"):
            augments_ss = ImageGrab.grab(bbox = (903, 1080, 1403, 1130))
            augments_ss.save("stage_three_first_augment.png")
            augments_ss.close()
            stage_three_augment_one_img = cv2.imread("stage_three_first_augment.png")
            stage_three_augment_one_text = pytesseract.image_to_string(stage_three_augment_one_img)
            #print(re.sub(r'\b\w{1,2}\b', '', stage_three_augment_one_text))

            augments_ss = ImageGrab.grab(bbox = (1693, 1080, 2193, 1130))
            augments_ss.save("stage_three_second_augment.png")
            augments_ss.close()
            stage_three_augment_two_img = cv2.imread("stage_three_second_augment.png")
            stage_three_augment_two_text = pytesseract.image_to_string(stage_three_augment_two_img)
            #print(re.sub(r'\b\w{1,2}\b', '', stage_three_augment_two_text))

            augments_ss = ImageGrab.grab(bbox = (2503, 1080, 3003, 1130))
            augments_ss.save("stage_three_third_augment.png")
            augments_ss.close()
            stage_three_augment_three_img = cv2.imread("stage_three_third_augment.png")
            stage_three_augment_three_text = pytesseract.image_to_string(stage_three_augment_three_img)
            #print(re.sub(r'\b\w{1,2}\b', '', stage_three_augment_three_text))

            stage_three_augment_one_text = re.sub(r'\b\w{1,2}\b', '', stage_three_augment_one_text)
            stage_three_augment_two_text = re.sub(r'\b\w{1,2}\b', '', stage_three_augment_two_text)
            stage_three_augment_three_text = re.sub(r'\b\w{1,2}\b', '', stage_three_augment_three_text)

            if stage_three_augment_one_text != stage_three_augment_one_val or stage_three_augment_two_text != stage_three_augment_two_val or stage_three_augment_three_text != stage_three_augment_three_val:
                print(stage_three_augment_one_text)
                stage_three_augment_one_val = stage_three_augment_one_text
                print(stage_three_augment_two_text)
                stage_three_augment_two_val = stage_three_augment_two_text
                print(stage_three_augment_three_text)
                stage_three_augment_three_val = stage_three_augment_three_text

            time.sleep(0.5)


        while not onscreen("./captures/4-2.png"):
            time.sleep(2)    

        stage_four_augment_one_val = ""
        stage_four_augment_two_val = ""
        stage_four_augment_three_val = ""
        if onscreen("./captures/4-2.png"):
            augments_ss = ImageGrab.grab(bbox = (903, 1080, 1403, 1130))
            augments_ss.save("stage_four_first_augment.png")
            augments_ss.close()
            stage_four_augment_one_img = cv2.imread("stage_four_first_augment.png")
            stage_four_augment_one_text = pytesseract.image_to_string(stage_four_augment_one_img)
            #print(re.sub(r'\b\w{1,2}\b', '', stage_four_augment_one_text))

            augments_ss = ImageGrab.grab(bbox = (1693, 1080, 2193, 1130))
            augments_ss.save("stage_four_second_augment.png")
            augments_ss.close()
            stage_four_augment_two_img = cv2.imread("stage_four_second_augment.png")
            stage_four_augment_two_text = pytesseract.image_to_string(stage_four_augment_two_img)
            #print(re.sub(r'\b\w{1,2}\b', '', stage_four_augment_two_text))

            augments_ss = ImageGrab.grab(bbox = (2503, 1080, 3003, 1130))
            augments_ss.save("stage_four_third_augment.png")
            augments_ss.close()
            stage_four_augment_three_img = cv2.imread("stage_four_third_augment.png")
            stage_four_augment_three_text = pytesseract.image_to_string(stage_four_augment_three_img)
            #print(re.sub(r'\b\w{1,2}\b', '', stage_four_augment_three_text))

            stage_four_augment_one_text = re.sub(r'\b\w{1,2}\b', '', stage_four_augment_one_text)
            stage_four_augment_two_text = re.sub(r'\b\w{1,2}\b', '', stage_four_augment_two_text)
            stage_four_augment_three_text = re.sub(r'\b\w{1,2}\b', '', stage_four_augment_three_text)

            if stage_four_augment_one_text != stage_four_augment_one_val or stage_four_augment_two_text != stage_four_augment_two_val or stage_four_augment_three_text != stage_four_augment_three_val:
                print(stage_four_augment_one_text)
                stage_four_augment_one_val = stage_four_augment_one_text
                print(stage_four_augment_two_text)
                stage_four_augment_two_val = stage_four_augment_two_text
                print(stage_four_augment_three_text)
                stage_four_augment_three_val = stage_four_augment_three_text

            time.sleep(0.5)



# Runs main and since sys.exit(main), also ignores unexpected exits (early player death before 4-2)
if __name__ == "__main__":
    main()
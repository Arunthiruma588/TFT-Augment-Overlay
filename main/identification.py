from python_imagesearch.imagesearch import imagesearch as search
from PIL import ImageGrab
# from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
import cv2
# import time
import re
# import pyautogui

# import sys
from fetchStats import getAugmentPlacement
# from statsWindowQt5 import *
# from PyQt6.QtGui import QScreen


def onscreen(path, precision=0.8):
    return search(path, precision)[0] != -1

def stringProcessing(string):
    # First need to strip string of \n and whitespace we get from pytesseract
    finalString = str.rstrip(string)
    # Second we need to get rid of extra / misread space 
    # ' case - because of sparkle effects on augment image 
    # ‘ case - special character for same sparkle effects reason
    # Il case - sometimes misreading II
    finalString = re.sub(r"^'", "", re.sub(r"^‘", "", re.sub(r"Il$", "II", finalString)))
    # Lastly some edge cases have trouble dealing with I's (i.e. attached to word: BagI instead of Bag I, Pumping Up! instead of Pumping Up I) 
    # Certain words also are consistently misread (Ona instead of On a), Young and Wild and Free due to box screenshot limitations
    if "!" in finalString:
        if finalString != "One, Two, Five!":
            finalString = re.sub(r"\s?!$", " I", finalString)
    if (" I" or " II" or " III") not in finalString:
        finalString = re.sub(r"I$", " I", finalString)
    if "|" in finalString:
        finalString = re.sub(r"\s?\|$", " I", finalString)
    if finalString == "Ona Roll":
        finalString = "On a Roll"
    elif "Wild and" in finalString:
        finalString = "Young and Wild and Free"

    return finalString

def putInfoinQueue(stageNumber):
    # This method returns data, a table which lists (first augment name, first augment placement), (second augment name, second augment placement), (third augment name, third augment placement)

    # It does this by determining the stageNumber 
    # and then taking screenshots of each of the augment text locations (this method is for 1920 x 1080 resolution)
    # and parsing those text images to text using pytesseract
    # doing string processing to get exact matches of text in the SQLite3 database
    # and searching for the average placement in the database using the augmentName and stageNumber info
    # and returning all this info in data
    data = None
    if stageNumber == 2:
        # Takes a screenshot of the location of the first augment text and turns it into an img and then string using pytesseract

        augments_ss = ImageGrab.grab(bbox = (435, 540, 671, 565))
        augments_ss.save("stage_two_first_augment.png")
        augments_ss.close()
        stage_two_augment_one_img = cv2.imread("stage_two_first_augment.png")
        stage_two_augment_one_text = pytesseract.image_to_string(stage_two_augment_one_img)

        # Takes a screenshot of the location of the second augment text and turns it into an img and then string using pytesseract

        augments_ss = ImageGrab.grab(bbox = (840, 540, 1086, 565))
        augments_ss.save("stage_two_second_augment.png")
        augments_ss.close()
        stage_two_augment_two_img = cv2.imread("stage_two_second_augment.png")
        stage_two_augment_two_text = pytesseract.image_to_string(stage_two_augment_two_img)

        # Takes a screenshot of the location of the third augment text and turns it into an img and then string using pytesseract

        augments_ss = ImageGrab.grab(bbox = (1254, 540, 1484, 565))
        augments_ss.save("stage_two_third_augment.png")
        augments_ss.close()
        stage_two_augment_three_img = cv2.imread("stage_two_third_augment.png")
        stage_two_augment_three_text = pytesseract.image_to_string(stage_two_augment_three_img)

        #Testing 
        print("Before string processing:")
        print("---" + stage_two_augment_one_text + "---")
        print("---" + stage_two_augment_two_text + "---")
        print("---" + stage_two_augment_three_text + "---")


        # String processing

        stage_two_augment_one_text = stringProcessing(stage_two_augment_one_text)
        stage_two_augment_two_text = stringProcessing(stage_two_augment_two_text)
        stage_two_augment_three_text = stringProcessing(stage_two_augment_three_text)

        print("After string processing:")
        print("---" + stage_two_augment_one_text + "---")
        print("---" + stage_two_augment_two_text + "---")
        print("---" + stage_two_augment_three_text + "---")

        # Group data into tuples (augmentName, augmentPlacement) listed in order of first,second,third augments and return result as a table: data

        data = [
            [stage_two_augment_one_text, getAugmentPlacement(stage_two_augment_one_text, stageNumber)],
            [stage_two_augment_two_text, getAugmentPlacement(stage_two_augment_two_text, stageNumber)],
            [stage_two_augment_three_text, getAugmentPlacement(stage_two_augment_three_text, stageNumber)],
        ]
    elif stageNumber == 3:
        # Takes a screenshot of the location of the first augment text and turns it into an img and then string using pytesseract

        augments_ss = ImageGrab.grab(bbox = (435, 540, 671, 565))
        augments_ss.save("stage_three_first_augment.png")
        augments_ss.close()
        stage_three_augment_one_img = cv2.imread("stage_three_first_augment.png")
        stage_three_augment_one_text = pytesseract.image_to_string(stage_three_augment_one_img)
        #print(re.sub(r'\b\w{1,2}\b', '', stage_three_augment_one_text))

        # Takes a screenshot of the location of the second augment text and turns it into an img and then string using pytesseract

        augments_ss = ImageGrab.grab(bbox = (840, 540, 1086, 565))
        augments_ss.save("stage_three_second_augment.png")
        augments_ss.close()
        stage_three_augment_two_img = cv2.imread("stage_three_second_augment.png")
        stage_three_augment_two_text = pytesseract.image_to_string(stage_three_augment_two_img)
        #print(re.sub(r'\b\w{1,2}\b', '', stage_three_augment_two_text))

        # Takes a screenshot of the location of the third augment text and turns it into an img and then string using pytesseract

        augments_ss = ImageGrab.grab(bbox = (1254, 540, 1484, 565))
        augments_ss.save("stage_three_third_augment.png")
        augments_ss.close()
        stage_three_augment_three_img = cv2.imread("stage_three_third_augment.png")
        stage_three_augment_three_text = pytesseract.image_to_string(stage_three_augment_three_img)
        #print(re.sub(r'\b\w{1,2}\b', '', stage_three_augment_three_text))

        #Testing 
        print("Before string processing:")
        print("---" + stage_three_augment_one_text + "---")
        print("---" + stage_three_augment_two_text + "---")
        print("---" + stage_three_augment_three_text + "---")

        #String processing

        stage_three_augment_one_text = stringProcessing(stage_three_augment_one_text)
        stage_three_augment_two_text = stringProcessing(stage_three_augment_two_text)
        stage_three_augment_three_text = stringProcessing(stage_three_augment_three_text)

        print("After string processing:")
        print("---" + stage_three_augment_one_text + "---")
        print("---" + stage_three_augment_two_text + "---")
        print("---" + stage_three_augment_three_text + "---")

        # Group data into tuples (augmentName, augmentPlacement) listed in order of first,second,third augments and return result as a table: data

        data = [
            [stage_three_augment_one_text, getAugmentPlacement(stage_three_augment_one_text, stageNumber)],
            [stage_three_augment_two_text, getAugmentPlacement(stage_three_augment_two_text, stageNumber)],
            [stage_three_augment_three_text, getAugmentPlacement(stage_three_augment_three_text, stageNumber)],
        ]
    elif stageNumber == 4:
        # Takes a screenshot of the location of the first augment text and turns it into an img and then string using pytesseract

        augments_ss = ImageGrab.grab(bbox = (435, 540, 671, 565))
        augments_ss.save("stage_four_first_augment.png")
        augments_ss.close()
        stage_four_augment_one_img = cv2.imread("stage_four_first_augment.png")
        stage_four_augment_one_text = pytesseract.image_to_string(stage_four_augment_one_img)
        #print(re.sub(r'\b\w{1,2}\b', '', stage_four_augment_one_text))

        # Takes a screenshot of the location of the second augment text and turns it into an img and then string using pytesseract

        augments_ss = ImageGrab.grab(bbox = (840, 540, 1086, 565))
        augments_ss.save("stage_four_second_augment.png")
        augments_ss.close()
        stage_four_augment_two_img = cv2.imread("stage_four_second_augment.png")
        stage_four_augment_two_text = pytesseract.image_to_string(stage_four_augment_two_img)
        #print(re.sub(r'\b\w{1,2}\b', '', stage_four_augment_two_text))

        # Takes a screenshot of the location of the third augment text and turns it into an img and then string using pytesseract

        augments_ss = ImageGrab.grab(bbox = (1254, 540, 1484, 565))
        augments_ss.save("stage_four_third_augment.png")
        augments_ss.close()
        stage_four_augment_three_img = cv2.imread("stage_four_third_augment.png")
        stage_four_augment_three_text = pytesseract.image_to_string(stage_four_augment_three_img)
        #print(re.sub(r'\b\w{1,2}\b', '', stage_four_augment_three_text))

        # String processing

        stage_four_augment_one_text = stringProcessing(stage_four_augment_one_text)
        stage_four_augment_two_text = stringProcessing(stage_four_augment_two_text)
        stage_four_augment_three_text = stringProcessing(stage_four_augment_three_text)

        # Group data into tuples (augmentName, augmentPlacement) listed in order of first,second,third augments and return result as a table: data

        data = [
            [stage_four_augment_one_text, getAugmentPlacement(stage_four_augment_one_text, stageNumber)],
            [stage_four_augment_two_text, getAugmentPlacement(stage_four_augment_two_text, stageNumber)],
            [stage_four_augment_three_text, getAugmentPlacement(stage_four_augment_three_text, stageNumber)],
        ]

    return data

# def augments():
#     fetchStats()

#     screen_size = pyautogui.size()
#     #print(screen_size[0])
#     #print(screen_size[1])
#     if screen_size[0] == 1920 and screen_size[1] == 1080:
#         print("1080p screen resolution")
#         while not onscreen("./captures/1080p2-1.png"):
#             #print("sleeping")
#             time.sleep(2)

#         stage_two_augment_one_val = ""
#         stage_two_augment_two_val = ""
#         stage_two_augment_three_val = ""
#         app = QApplication([])
#         app.setStyleSheet("""
#                 QTableView {
#                 background-color: #0d3868;
#                 /* background-color: #0f1720; */
#                 /* gridline-color: #f7fbff; */ 
#                 gridline-color: #0095ff13;
#                 color: #eaf6ff; 
#                 font-size: 20px
#                 }
#         """)
#         while onscreen("./captures/1080p2-1.png"):
#             augments_ss = ImageGrab.grab(bbox = (440, 540, 666, 565))
#             augments_ss.save("stage_two_first_augment.png")
#             augments_ss.close()
#             stage_two_augment_one_img = cv2.imread("stage_two_first_augment.png")
#             stage_two_augment_one_text = pytesseract.image_to_string(stage_two_augment_one_img)

#             augments_ss = ImageGrab.grab(bbox = (850, 540, 1076, 565))
#             augments_ss.save("stage_two_second_augment.png")
#             augments_ss.close()
#             stage_two_augment_two_img = cv2.imread("stage_two_second_augment.png")
#             stage_two_augment_two_text = pytesseract.image_to_string(stage_two_augment_two_img)

#             augments_ss = ImageGrab.grab(bbox = (1259, 540, 1469, 565))
#             augments_ss.save("stage_two_third_augment.png")
#             augments_ss.close()
#             stage_two_augment_three_img = cv2.imread("stage_two_third_augment.png")
#             stage_two_augment_three_text = pytesseract.image_to_string(stage_two_augment_three_img)

#             stage_two_augment_one_text = str.rstrip(stage_two_augment_one_text)
#             stage_two_augment_two_text = str.rstrip(stage_two_augment_two_text)
#             stage_two_augment_three_text = str.rstrip(stage_two_augment_three_text)

#             print("---" + stage_two_augment_one_text + "---")
#             print("---" + stage_two_augment_two_text + "---")
#             print("---" + stage_two_augment_three_text + "---")

#             # Create the statsWindow only the FIRST TIME we see 3 augments
#             if stage_two_augment_one_val == "" and stage_two_augment_two_val == "" and stage_two_augment_three_val == "":
#                 print("Creates the table the first time")
#                 data = [
#                         [stage_two_augment_one_text, getAugmentPlacement(stage_two_augment_one_text, 2)],
#                         [stage_two_augment_two_text, getAugmentPlacement(stage_two_augment_two_text, 2)],
#                         [stage_two_augment_three_text, getAugmentPlacement(stage_two_augment_three_text, 2)],
#                 ]

#                 window = CreateTable(data, 2, screen_size[0], screen_size[1])

#                 window.show()

#             if stage_two_augment_one_text != stage_two_augment_one_val or stage_two_augment_two_text != stage_two_augment_two_val or stage_two_augment_three_text != stage_two_augment_three_val:
#                 print(stage_two_augment_one_text)
#                 # If it's not the first 3 augments then update
#                 # if(stage_two_augment_one_val != ""):
#                 #     window.updateFirstAugmentStats(stage_two_augment_one_text, getAugmentPlacement(stage_two_augment_one_text, 2))
#                 stage_two_augment_one_val = stage_two_augment_one_text

#                 print(stage_two_augment_two_text)
#                 # If it's not the first 3 augments then update
#                 # if(stage_two_augment_two_val != ""):
#                 #     window.updateSecondAugmentStats(stage_two_augment_two_text, getAugmentPlacement(stage_two_augment_two_text, 2))
#                 stage_two_augment_two_val = stage_two_augment_two_text

#                 print(stage_two_augment_three_text)
#                 # If it's not the first 3 augments then update
#                 # if(stage_two_augment_three_val != ""):
#                 #     window.updateThirdAugmentStats(stage_two_augment_three_text, getAugmentPlacement(stage_two_augment_three_text, 2))
#                 stage_two_augment_three_val = stage_two_augment_three_text

#             time.sleep(0.5)
            
#         print("waiting for 3-2")
#         # QtCore.QMetaObject.invokeMethod(window, "close", QtCore.Qt.ConnectionType.QueuedConnection)
#         while not onscreen("./captures/1080p3-2.png"):
#             time.sleep(2)    

#         stage_three_augment_one_val = ""
#         stage_three_augment_two_val = ""
#         stage_three_augment_three_val = ""
#         while onscreen("./captures/1080p3-2.png"):
#             augments_ss = ImageGrab.grab(bbox = (440, 540, 666, 565))
#             augments_ss.save("stage_three_first_augment.png")
#             augments_ss.close()
#             stage_three_augment_one_img = cv2.imread("stage_three_first_augment.png")
#             stage_three_augment_one_text = pytesseract.image_to_string(stage_three_augment_one_img)
#             #print(re.sub(r'\b\w{1,2}\b', '', stage_three_augment_one_text))

#             augments_ss = ImageGrab.grab(bbox = (853, 540, 1076, 565))
#             augments_ss.save("stage_three_second_augment.png")
#             augments_ss.close()
#             stage_three_augment_two_img = cv2.imread("stage_three_second_augment.png")
#             stage_three_augment_two_text = pytesseract.image_to_string(stage_three_augment_two_img)
#             #print(re.sub(r'\b\w{1,2}\b', '', stage_three_augment_two_text))

#             augments_ss = ImageGrab.grab(bbox = (1259, 540, 1469, 565))
#             augments_ss.save("stage_three_third_augment.png")
#             augments_ss.close()
#             stage_three_augment_three_img = cv2.imread("stage_three_third_augment.png")
#             stage_three_augment_three_text = pytesseract.image_to_string(stage_three_augment_three_img)
#             #print(re.sub(r'\b\w{1,2}\b', '', stage_three_augment_three_text))

#             stage_three_augment_one_text = re.sub(r'\b\w{1,2}\b', '', stage_three_augment_one_text)
#             stage_three_augment_two_text = re.sub(r'\b\w{1,2}\b', '', stage_three_augment_two_text)
#             stage_three_augment_three_text = re.sub(r'\b\w{1,2}\b', '', stage_three_augment_three_text)

#             print("Stage 3 first augment: " + stage_two_augment_one_text)
#             print("Stage 3 second augment: " + stage_two_augment_two_text)
#             print("Stage 3 third augment: " + stage_two_augment_three_text)


#             if stage_three_augment_one_text != stage_three_augment_one_val or stage_three_augment_two_text != stage_three_augment_two_val or stage_three_augment_three_text != stage_three_augment_three_val:
#                 print(stage_three_augment_one_text)
#                 stage_three_augment_one_val = stage_three_augment_one_text
#                 print(stage_three_augment_two_text)
#                 stage_three_augment_two_val = stage_three_augment_two_text
#                 print(stage_three_augment_three_text)
#                 stage_three_augment_three_val = stage_three_augment_three_text

#             time.sleep(0.5)


#         while not onscreen("./captures/1080p4-2.png"):
#             time.sleep(2)

#         stage_four_augment_one_val = ""
#         stage_four_augment_two_val = ""
#         stage_four_augment_three_val = ""
#         while onscreen("./captures/1080p4-2.png"):
#             augments_ss = ImageGrab.grab(bbox = (440, 540, 666, 565))
#             augments_ss.save("stage_four_first_augment.png")
#             augments_ss.close()
#             stage_four_augment_one_img = cv2.imread("stage_four_first_augment.png")
#             stage_four_augment_one_text = pytesseract.image_to_string(stage_four_augment_one_img)
#             #print(re.sub(r'\b\w{1,2}\b', '', stage_four_augment_one_text))

#             augments_ss = ImageGrab.grab(bbox = (850, 540, 1076, 565))
#             augments_ss.save("stage_four_second_augment.png")
#             augments_ss.close()
#             stage_four_augment_two_img = cv2.imread("stage_four_second_augment.png")
#             stage_four_augment_two_text = pytesseract.image_to_string(stage_four_augment_two_img)
#             #print(re.sub(r'\b\w{1,2}\b', '', stage_four_augment_two_text))

#             augments_ss = ImageGrab.grab(bbox = (1259, 540, 1469, 565))
#             augments_ss.save("stage_four_third_augment.png")
#             augments_ss.close()
#             stage_four_augment_three_img = cv2.imread("stage_four_third_augment.png")
#             stage_four_augment_three_text = pytesseract.image_to_string(stage_four_augment_three_img)
#             #print(re.sub(r'\b\w{1,2}\b', '', stage_four_augment_three_text))

#             stage_four_augment_one_text = re.sub(r'\b\w{1,2}\b', '', stage_four_augment_one_text)
#             stage_four_augment_two_text = re.sub(r'\b\w{1,2}\b', '', stage_four_augment_two_text)
#             stage_four_augment_three_text = re.sub(r'\b\w{1,2}\b', '', stage_four_augment_three_text)

#             if stage_four_augment_one_text != stage_four_augment_one_val or stage_four_augment_two_text != stage_four_augment_two_val or stage_four_augment_three_text != stage_four_augment_three_val:
#                 print(stage_four_augment_one_text)
#                 stage_four_augment_one_val = stage_four_augment_one_text
#                 print(stage_four_augment_two_text)
#                 stage_four_augment_two_val = stage_four_augment_two_text
#                 print(stage_four_augment_three_text)
#                 stage_four_augment_three_val = stage_four_augment_three_text

#             time.sleep(0.5)

#     elif screen_size[0] == 3840 and screen_size[1] == 2160:
#         print("4k screen resloution")

#         print("waiting for stage 2-1")
#         while not onscreen("./captures/2-1.png"):
#             #print("sleeping")
#             time.sleep(2)

#         stage_two_augment_one_val = ""
#         stage_two_augment_two_val = ""
#         stage_two_augment_three_val = ""
#         while onscreen("./captures/2-1.png"):
#             augments_ss = ImageGrab.grab(bbox = (903, 1080, 1403, 1130))
#             augments_ss.save("stage_two_first_augment.png")
#             augments_ss.close()
#             stage_two_augment_one_img = cv2.imread("stage_two_first_augment.png")
#             stage_two_augment_one_text = pytesseract.image_to_string(stage_two_augment_one_img)
#             #print(re.sub(r'\b\w{1,2}\b', '', stage_two_augment_one_text))

#             augments_ss = ImageGrab.grab(bbox = (1693, 1080, 2193, 1130))
#             augments_ss.save("stage_two_second_augment.png")
#             augments_ss.close()
#             stage_two_augment_two_img = cv2.imread("stage_two_second_augment.png")
#             stage_two_augment_two_text = pytesseract.image_to_string(stage_two_augment_two_img)
#             #print(re.sub(r'\b\w{1,2}\b', '', stage_two_augment_two_text))

#             augments_ss = ImageGrab.grab(bbox = (2503, 1080, 3003, 1130))
#             augments_ss.save("stage_two_third_augment.png")
#             augments_ss.close()
#             stage_two_augment_three_img = cv2.imread("stage_two_third_augment.png")
#             stage_two_augment_three_text = pytesseract.image_to_string(stage_two_augment_three_img)
#             #print(re.sub(r'\b\w{1,2}\b', '', stage_two_augment_three_text))

#             stage_two_augment_one_text = re.sub(r'\b\w{1,2}\b', '', stage_two_augment_one_text)
#             stage_two_augment_two_text = re.sub(r'\b\w{1,2}\b', '', stage_two_augment_two_text)
#             stage_two_augment_three_text = re.sub(r'\b\w{1,2}\b', '', stage_two_augment_three_text)

#             if stage_two_augment_one_text != stage_two_augment_one_val or stage_two_augment_two_text != stage_two_augment_two_val or stage_two_augment_three_text != stage_two_augment_three_val:
#                 print(stage_two_augment_one_text)
#                 stage_two_augment_one_val = stage_two_augment_one_text
#                 print(stage_two_augment_two_text)
#                 stage_two_augment_two_val = stage_two_augment_two_text
#                 print(stage_two_augment_three_text)
#                 stage_two_augment_three_val = stage_two_augment_three_text

#             time.sleep(0.5)
            
#         print("waiting for stage 3-2")
#         while not onscreen("./captures/3-2.png"):
#             time.sleep(2)    

#         stage_three_augment_one_val = ""
#         stage_three_augment_two_val = ""
#         stage_three_augment_three_val = ""
#         while onscreen("./captures/3-2.png"):
#             augments_ss = ImageGrab.grab(bbox = (903, 1080, 1403, 1130))
#             augments_ss.save("stage_three_first_augment.png")
#             augments_ss.close()
#             stage_three_augment_one_img = cv2.imread("stage_three_first_augment.png")
#             stage_three_augment_one_text = pytesseract.image_to_string(stage_three_augment_one_img)
#             #print(re.sub(r'\b\w{1,2}\b', '', stage_three_augment_one_text))

#             augments_ss = ImageGrab.grab(bbox = (1693, 1080, 2193, 1130))
#             augments_ss.save("stage_three_second_augment.png")
#             augments_ss.close()
#             stage_three_augment_two_img = cv2.imread("stage_three_second_augment.png")
#             stage_three_augment_two_text = pytesseract.image_to_string(stage_three_augment_two_img)
#             #print(re.sub(r'\b\w{1,2}\b', '', stage_three_augment_two_text))

#             augments_ss = ImageGrab.grab(bbox = (2503, 1080, 3003, 1130))
#             augments_ss.save("stage_three_third_augment.png")
#             augments_ss.close()
#             stage_three_augment_three_img = cv2.imread("stage_three_third_augment.png")
#             stage_three_augment_three_text = pytesseract.image_to_string(stage_three_augment_three_img)
#             #print(re.sub(r'\b\w{1,2}\b', '', stage_three_augment_three_text))

#             stage_three_augment_one_text = re.sub(r'\b\w{1,2}\b', '', stage_three_augment_one_text)
#             stage_three_augment_two_text = re.sub(r'\b\w{1,2}\b', '', stage_three_augment_two_text)
#             stage_three_augment_three_text = re.sub(r'\b\w{1,2}\b', '', stage_three_augment_three_text)

#             if stage_three_augment_one_text != stage_three_augment_one_val or stage_three_augment_two_text != stage_three_augment_two_val or stage_three_augment_three_text != stage_three_augment_three_val:
#                 print(stage_three_augment_one_text)
#                 stage_three_augment_one_val = stage_three_augment_one_text
#                 print(stage_three_augment_two_text)
#                 stage_three_augment_two_val = stage_three_augment_two_text
#                 print(stage_three_augment_three_text)
#                 stage_three_augment_three_val = stage_three_augment_three_text

#             time.sleep(0.5)

#         print("waiting for stage 4-2")
#         while not onscreen("./captures/4-2.png"):
#             time.sleep(2)    

#         stage_four_augment_one_val = ""
#         stage_four_augment_two_val = ""
#         stage_four_augment_three_val = ""
#         while onscreen("./captures/4-2.png"):
#             augments_ss = ImageGrab.grab(bbox = (903, 1080, 1403, 1130))
#             augments_ss.save("stage_four_first_augment.png")
#             augments_ss.close()
#             stage_four_augment_one_img = cv2.imread("stage_four_first_augment.png")
#             stage_four_augment_one_text = pytesseract.image_to_string(stage_four_augment_one_img)
#             #print(re.sub(r'\b\w{1,2}\b', '', stage_four_augment_one_text))

#             augments_ss = ImageGrab.grab(bbox = (1693, 1080, 2193, 1130))
#             augments_ss.save("stage_four_second_augment.png")
#             augments_ss.close()
#             stage_four_augment_two_img = cv2.imread("stage_four_second_augment.png")
#             stage_four_augment_two_text = pytesseract.image_to_string(stage_four_augment_two_img)
#             #print(re.sub(r'\b\w{1,2}\b', '', stage_four_augment_two_text))

#             augments_ss = ImageGrab.grab(bbox = (2503, 1080, 3003, 1130))
#             augments_ss.save("stage_four_third_augment.png")
#             augments_ss.close()
#             stage_four_augment_three_img = cv2.imread("stage_four_third_augment.png")
#             stage_four_augment_three_text = pytesseract.image_to_string(stage_four_augment_three_img)
#             #print(re.sub(r'\b\w{1,2}\b', '', stage_four_augment_three_text))

#             stage_four_augment_one_text = re.sub(r'\b\w{1,2}\b', '', stage_four_augment_one_text)
#             stage_four_augment_two_text = re.sub(r'\b\w{1,2}\b', '', stage_four_augment_two_text)
#             stage_four_augment_three_text = re.sub(r'\b\w{1,2}\b', '', stage_four_augment_three_text)

#             if stage_four_augment_one_text != stage_four_augment_one_val or stage_four_augment_two_text != stage_four_augment_two_val or stage_four_augment_three_text != stage_four_augment_three_val:
#                 print(stage_four_augment_one_text)
#                 stage_four_augment_one_val = stage_four_augment_one_text
#                 print(stage_four_augment_two_text)
#                 stage_four_augment_two_val = stage_four_augment_two_text
#                 print(stage_four_augment_three_text)
#                 stage_four_augment_three_val = stage_four_augment_three_text

#             time.sleep(0.5)



# # Makes sure bad exit conditions are cleared
# sys.exit(augments())

#4kaugment pixels
#augments_ss = ImageGrab.grab(bbox = (903, 1080, 1403, 1130))
#augments_ss.save("first_augment.png")
#augments_ss.close()

#augments_ss = ImageGrab.grab(bbox = (1693, 1080, 2193, 1130))
#augments_ss.save("second_augment.png")
#augments_ss.close()

#augments_ss = ImageGrab.grab(bbox = (2503, 1080, 3003, 1130))
#augments_ss.save("third_augment.png")
#augments_ss.close()

        
#4kstage pixels
#augments_ss = ImageGrab.grab(bbox = (1545, 25, 1613, 63))
#augments_ss.save("3-2.png")
#augments_ss.close()

#img = cv2.imread("stage_three_augments.png")
#text = pytesseract.image_to_string(img)
#print(re.sub(r'\b\w{1,2}\b', '', text))
#cv2.imshow('Result', img)
#cv2.waitKey(0)
#print(pytesseract.image_to_string(Image.open('stage_three_augments.png')))
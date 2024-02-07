import time
import sys
from fetchStats import *
from statsWindowQt5 import *
from PyQt6.QtGui import QScreen

from python_imagesearch.imagesearch import imagesearch as search
from PIL import ImageGrab
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
import cv2
import time
import re
import pyautogui

# def runApp(data):
#   app = QApplication([])

#   # Stylesheet
#   # Helpful reference: https://stackoverflow.com/questions/26162387/qtableview-qtablewidget-grid-stylesheet-grid-line-width
#   app.setStyleSheet("""
#     QTableView {
#       background-color: #0d3868;
#       /* background-color: #0f1720; */
#       /* gridline-color: #f7fbff; */ 
#       gridline-color: #0095ff13;
#       color: #eaf6ff; 
#       font-size: 18px
#     }
#   """)
#   window = CreateMainWindow(data)
#   app.exec()

def testing():
  fetchStats()

  # image = cv2.imread('stage_two_first_augment.png')
  # # blur = cv2.GaussianBlur(gray, (3,3), 0)
  # # thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

  # # # Morph open to remove noise and invert image
  # # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
  # # opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
  # # invert = 255 - opening

  # # Perform text extraction
  # data = pytesseract.image_to_string(gray, lang='eng', config='--psm 6')
  # data = str.rstrip(data)
  # print('---' + data + '---')

  # cv2.imshow('image', image)
  # # cv2.imshow('opening', opening)
  # # cv2.imshow('invert', invert)
  # cv2.waitKey(0)

  # stage_two_augment_three_img = cv2.imread("stage_two_third_augment.png")
  # stage_two_augment_three_text = pytesseract.image_to_string(stage_two_augment_three_img)
  # print(stage_two_augment_three_text)
  # stage_two_augment_three_text = re.sub(r'\b\w{1,2}\b', '', stage_two_augment_three_text)
  # print(stage_two_augment_three_text)


  # print(getAugmentPlacement("Twin Terror l", 2))
  # stage_two_augment_first_augment = "Lucky Streak"
  # stage_two_augment_second_augment = "Heroic Grab Bag"
  # stage_two_augment_third_augment = "Stationary Support"
  # # Create application that runs the new window
  # app = QApplication([])

  # # Stylesheet
  # # Helpful reference: https://stackoverflow.com/questions/26162387/qtableview-qtablewidget-grid-stylesheet-grid-line-width
  # app.setStyleSheet("""
  #   QTableView {
  #     background-color: #0d3868;
  #     /* background-color: #0f1720; */
  #     /* gridline-color: #f7fbff; */ 
  #     gridline-color: #0095ff13;
  #     color: #eaf6ff; 
  #     font-size: 20px
  #   }
  # """)
  # loopCounter = 0


  # # data = [
  # #         ["", ""], 
  # #         ["", ""], 
  # #         ["", ""],
  # # ]

  # data = [
  #           [stage_two_augment_first_augment, getAugmentPlacement(stage_two_augment_first_augment, 2)],
  #           [stage_two_augment_second_augment, getAugmentPlacement(stage_two_augment_second_augment, 2)],
  #           [stage_two_augment_third_augment, getAugmentPlacement(stage_two_augment_third_augment, 2)],
  # ]
  # # runApp(data)

  # # window = None

  # # print(window.table.item(0,0).text())
  # # print(data[0][0])
  # # print(window.table.item(0,0).text() == data[0][0])
  # # while (loopCounter < 20):

  # #   loopCounter += 1


  #   # print("---" + stage_two_augment_first_augment + "---")
  #   # print("---" + stage_two_augment_second_augment + "---")
  #   # print("---" + stage_two_augment_third_augment + "---")

  # # Inputs of line below explained: 
  #   # Data is data from above
  #   # 3 is the stageNumber (3-2)
  #   # 1920 x 1080 is the last 2 resolution numbers which determine the size of the augment screen (need to adjust for 4K display)
  # window = CreateMainWindow(data, 2, 1920, 1080)
  # # while True:
  # #     # parent = QMainWindow()
  # time.sleep(2)
  # window.updateTable("hide", 3)
  # # window.show()
  # # window.lower()
  # time.sleep(2)
  # window.setStyleSheet(("""
  #   QTableView {
  #     background-color: #0d3868;
  #     /* background-color: #0f1720; */
  #     /* gridline-color: #f7fbff; */ 
  #     gridline-color: #0095ff13;
  #     color: #eaf6ff; 
  #     font-size: 20px
  #   }
  # """))
  # window.updateTable("show", 3)
  # time.sleep(2)

  # # window.show()
  # #     # table = CreateTable(window, data, 2, 1920, 1080)
  # #     # window.show()
  # #     # table.show()
  # #     print("hi")

  # # app.exec()
  # # window.table2.close()
  # # time.sleep(2)
  # # window.UIComponents(data, 2, 1920, 1080)
  # # time.sleep(2)
  # # window.updateTable(data, 2, 1920, 1080)
  # # window.table.setHidden(False)
  # # time.sleep(2)
  # # window.table.setHidden(True)
  # # window.show()
  # # time.sleep(2)
  # # window.table.setHidden(False)

  #     # window.updateTable(data, 2, 1920, 1080)
  #     # print(window.table.item(0,0).text())
  #   # elif loopCounter == 15:
  # data = [
  #       ["Scrappy Inventions", getAugmentPlacement("Scrappy Inventions", 2)],
  #       [stage_two_augment_second_augment, getAugmentPlacement(stage_two_augment_second_augment, 2)],
  #       [stage_two_augment_third_augment, getAugmentPlacement(stage_two_augment_third_augment, 2)],
  # ]
    
  # #   # # # if window.table.item(0,0).text() != data[0][0]:
  # #   # #   print(window.table.item(0,0).text())
  # #   # #   print(data[0][0])
  # window.updateFirstAugmentStats(data[0][0], data[0][1])
  # time.sleep(2)
  #   #   print(window.table.item(0,0).text())
  #   #   time.sleep(4)
  #   # # if window.table.item(1,0).text() != data[1][0]:
  #   #   window.updateSecondAugmentStats(data[1][0], data[1][1])
  #   # # if window.table.item(2,0).text() != data[2][0]:
  #   #   window.updateThirdAugmentStats(data[2][0], data[2][1])

  #   # time.sleep(0.5)
  # # print("2-1")
  # # time.sleep(3)

  # # time.sleep(2)
  # # #       # # window.show()
  # # # window.updateTable("hide", data, 2, 1920, 1080)
  # # # # window = CreateMainWindow(data, 2, 1920, 1080)
  # # # time.sleep(2)
  
  # # data = [
  # #           ["Scrappy Inventions", getAugmentPlacement("Scrappy Inventions", 2)],
  # #           [stage_two_augment_second_augment, getAugmentPlacement(stage_two_augment_second_augment, 2)],
  # #           [stage_two_augment_third_augment, getAugmentPlacement(stage_two_augment_third_augment, 2)],
  # # ]

  # # window.UIComponents(data, 3, 1920, 1080)
  # # time.sleep(2)
  # # newApp = QApplication([])

  # # # Stylesheet
  # # # Helpful reference: https://stackoverflow.com/questions/26162387/qtableview-qtablewidget-grid-stylesheet-grid-line-width
  # # newApp.setStyleSheet("""
  # #   QTableView {
  # #     background-color: #0d3868;
  # #     /* background-color: #0f1720; */
  # #     /* gridline-color: #f7fbff; */ 
  # #     gridline-color: #0095ff13;
  # #     color: #eaf6ff; 
  # #     font-size: 14px
  # #   }
  # # """)
  # # window = None
  # # print(window.table)
  # # window.updateTable(data, 3, 1920, 1080)
  # # window.show()
  # # print(window.table)
  # # window.update()
  # # print(window.table.item(0,0).text())
  # # time.sleep(2)
  # print("gets here after everything in testing")

  # runApp(data)
  # window.tableClose()
  # # window.show()
  # time.sleep(3)
  # window.tableOpen(data)
  # time.sleep(2)
  
  # random_index = 0
  # while random_index < 12:
  #   print("goodbye")
  #   time.sleep(0.5)
  #   random_index += 1

  # Potential second monitor support (haven't tested) 
  # referenced from https://stackoverflow.com/questions/6854947/how-to-display-a-window-on-a-secondary-display-in-pyqt
  # number in second line monitors[1] 0 = first monitor 1 = second monitor
  # needs import: "from PyQt6.QtGui import QScreen"

  # ''' 

  # monitors = QScreen.virtualSiblings(window.screen())
  # monitor = monitors[1].availableGeometry()

  # '''

testing()
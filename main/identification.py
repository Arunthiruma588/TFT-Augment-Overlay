from python_imagesearch.imagesearch import imagesearch as search
from PIL import ImageGrab
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
import cv2
import time
import re
import pyautogui



def onscreen(path, precision=0.8):
    return search(path, precision)[0] != -1

def augments():

    screen_size = pyautogui.size()
    #print(screen_size[0])
    #print(screen_size[1])
    if screen_size[0] == 1920 and screen_size[1] == 1080:
        print("1080p screen resloution")
        while not onscreen("./captures/1080p2-1.png"):
            #print("sleeping")
            time.sleep(2)

        stage_two_augment_one_val = ""
        stage_two_augment_two_val = ""
        stage_two_augment_three_val = ""
        while onscreen("./captures/1080p2-1.png"):
            augments_ss = ImageGrab.grab(bbox = (440, 540, 666, 565))
            augments_ss.save("stage_two_first_augment.png")
            augments_ss.close()
            stage_two_augment_one_img = cv2.imread("stage_two_first_augment.png")
            stage_two_augment_one_text = pytesseract.image_to_string(stage_two_augment_one_img)

            augments_ss = ImageGrab.grab(bbox = (850, 540, 1076, 565))
            augments_ss.save("stage_two_second_augment.png")
            augments_ss.close()
            stage_two_augment_two_img = cv2.imread("stage_two_second_augment.png")
            stage_two_augment_two_text = pytesseract.image_to_string(stage_two_augment_two_img)

            augments_ss = ImageGrab.grab(bbox = (1259, 540, 1469, 565))
            augments_ss.save("stage_two_third_augment.png")
            augments_ss.close()
            stage_two_augment_three_img = cv2.imread("stage_two_third_augment.png")
            stage_two_augment_three_text = pytesseract.image_to_string(stage_two_augment_three_img)

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
            
        print("waiting for 3-2")
        while not onscreen("./captures/1080p3-2.png"):
            time.sleep(2)    

        stage_three_augment_one_val = ""
        stage_three_augment_two_val = ""
        stage_three_augment_three_val = ""
        while onscreen("./captures/1080p3-2.png"):
            augments_ss = ImageGrab.grab(bbox = (440, 540, 666, 565))
            augments_ss.save("stage_three_first_augment.png")
            augments_ss.close()
            stage_three_augment_one_img = cv2.imread("stage_three_first_augment.png")
            stage_three_augment_one_text = pytesseract.image_to_string(stage_three_augment_one_img)
            #print(re.sub(r'\b\w{1,2}\b', '', stage_three_augment_one_text))

            augments_ss = ImageGrab.grab(bbox = (853, 540, 1076, 565))
            augments_ss.save("stage_three_second_augment.png")
            augments_ss.close()
            stage_three_augment_two_img = cv2.imread("stage_three_second_augment.png")
            stage_three_augment_two_text = pytesseract.image_to_string(stage_three_augment_two_img)
            #print(re.sub(r'\b\w{1,2}\b', '', stage_three_augment_two_text))

            augments_ss = ImageGrab.grab(bbox = (1259, 540, 1469, 565))
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


        while not onscreen("./captures/1080p4-2.png"):
            time.sleep(2)

        stage_four_augment_one_val = ""
        stage_four_augment_two_val = ""
        stage_four_augment_three_val = ""
        while onscreen("./captures/1080p4-2.png"):
            augments_ss = ImageGrab.grab(bbox = (440, 540, 666, 565))
            augments_ss.save("stage_four_first_augment.png")
            augments_ss.close()
            stage_four_augment_one_img = cv2.imread("stage_four_first_augment.png")
            stage_four_augment_one_text = pytesseract.image_to_string(stage_four_augment_one_img)
            #print(re.sub(r'\b\w{1,2}\b', '', stage_four_augment_one_text))

            augments_ss = ImageGrab.grab(bbox = (850, 540, 1076, 565))
            augments_ss.save("stage_four_second_augment.png")
            augments_ss.close()
            stage_four_augment_two_img = cv2.imread("stage_four_second_augment.png")
            stage_four_augment_two_text = pytesseract.image_to_string(stage_four_augment_two_img)
            #print(re.sub(r'\b\w{1,2}\b', '', stage_four_augment_two_text))

            augments_ss = ImageGrab.grab(bbox = (1259, 540, 1469, 565))
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

    elif screen_size[0] == 3840 and screen_size[1] == 2160:
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




augments()

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
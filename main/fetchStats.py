import sqlite3
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def dropTableDatabase():
  try:
      sqliteConnection = sqlite3.connect('Augment_Stats.db')
      cursor = sqliteConnection.cursor()
      print("Connected to SQLite")

      sqlite_delete_table = """DROP TABLE IF EXISTS AugmentTable;"""

      cursor.execute(sqlite_delete_table)
      sqliteConnection.commit()
      print("Successfully deleted table: AugmentTable")

      cursor.close()

  except sqlite3.Error as error:
      print("Failed to delete AugmentTable", error)
  finally:
      if sqliteConnection:
          sqliteConnection.close()
          print("The SQLite connection is closed")

# Referenced from https://pynative.com/python-sqlite/#h-create-sqlite-table-from-python
# Creates the table in the database Augment_Stats which will store the augments names and avg placements from tactics.tools in a table

def createTableDatabase():
  try:
      sqliteConnection = sqlite3.connect('Augment_Stats.db')
      cursor = sqliteConnection.cursor()
      print("Connected to SQLite")

      sqlite_create_table = """CREATE TABLE AugmentTable (augmentName TEXT NOT NULL UNIQUE PRIMARY KEY, first TEXT, second TEXT, third TEXT);"""

      cursor.execute(sqlite_create_table)
      sqliteConnection.commit()
      print("Successfully created table: AugmentTable")

      cursor.close()

  except sqlite3.Error as error:
      print("Failed to create AugmentTable", error)
  finally:
      if sqliteConnection:
          sqliteConnection.close()
          print("The SQLite connection is closed")

# Referenced from https://pynative.com/python-sqlite-insert-into-table/
          
def insertVaribleIntoTable(augmentName, first, second, third):
    try:
        sqliteConnection = sqlite3.connect('Augment_Stats.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO AugmentTable
                          (augmentName, first, second, third) 
                          VALUES (?, ?, ?, ?);"""

        data_tuple = (augmentName, first, second, third)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into AugmentTable")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into AugmentTable", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

# From https://www.scrapingbee.com/blog/selenium-python/#chrome-headless-mode
# and https://stackoverflow.com/questions/65755603/selenium-ssl-client-socket-impl-cc-handshake-failed

def fetchStats():
    options = webdriver.ChromeOptions()
    # Runs Chrome browser as a background process (doesn't pop up since no GUI)
    options.add_argument("--headless=new")
    # Tactics.tools has a missing/expired/invalid SSL certificate, they really need to fix that
    options.add_argument('--ignore-certificate-errors-spki-list')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://tactics.tools/augments")

    # Have to wait for the page to load (otherwise sometimes the JS doesn't generate the DOM elements we're searching for)

    time.sleep(0.5)

    # Gets the HTML for the augment names from tactics.tools by XPATH
    # Helpful source for XPATH: https://www.youtube.com/watch?v=yZY6-XSTveA&ab_channel=AutomatewithJonathan

    augHTML = driver.find_elements(By.XPATH, value="//*[contains(@class, 'pl-[6px]') and contains(@class, 'font-roboto') and contains(@class, 'font-normal') and contains(@class, 'truncate')]")

    # Dictionary used to store {index, augmentNames} so we can later link up the stats with the augment names

    augNames = {}
    augNamesIndex = 0

    for names in augHTML:
    # Gets rid of the first result which is not an augment name (AugmentsGamesPlaceTop 4WinAt ...).
        if(len(names.text) < 30):
            augNames[augNamesIndex] = names.text
            augNamesIndex+=1

    # print(augNames)

    # text="."
    # blank="—"

    indexofStat = 0
    statCounter = 0;

    # Refreshes the table database so stats are update

    dropTableDatabase()

    createTableDatabase()

    # Get stats for specific placements at Stage 2-1, 3-2, 4-2, instead of general stats for augments
    statsHTML = driver.find_elements(By.XPATH, value="//div[@id='tbl-body']//*[contains(@class, 'flex') and contains(@class, 'items-center') and contains(@class, 'justify-end') and contains(@class, 'px-[14px]') and contains(@class, 'css-1puwvti') and contains(@class, 'tbl-cell-right-border')]")
    # print(statsHTML)
    for stats in statsHTML:
        if statCounter == 0:
            first = stats.text
        if statCounter == 1:
            second = stats.text
        if statCounter == 2:
            third = stats.text
            # print(indexofStat, augNames[indexofStat], first, second, third)
            insertVaribleIntoTable(augNames[indexofStat], first, second, third)
            indexofStat += 1
            statCounter = -1
        statCounter += 1

    # Sourced from https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
    SCROLL_PAUSE_TIME = 0.5

    # Bottom of document
    # bottom = driver.execute_script("return document.body.scrollHeight")
    # Bottom of document varies so put it at 10000 for patch 14.2 of TFT
    # SUBJECT TO CHANGE
    bottom = 10000

    # Rough estimate of next height increment (this is SUBJECT TO CHANGE if tactics.tools ever changes it's table height)
    height_increment = 1170

    #Augment repeat number represents the index at which we want the stats of the non-repeated last augments of the table
    #For reference number meanings: 42 = starts from last 3 augments 45 = last 2 augments 48 = last augment (patch 14.2)
    # SUBJECT TO CHANGE (depends height increment and how many augments this patch/set)
    augmentRepeatNumber = 48

    # Update the current height so the first time in the loop it scrolls down the page to new height (we want to get new augment stats)
    # Which is the 13th augment on the table list (height is just rought estimate based on DOM rendering)
    current_height = height_increment

    # Counter to track when we are reaching the non-repeated last augments
    lastAugmentCounter = 0

    while True:
        if current_height == bottom:
            break
        # Scroll down to current_height which was just updated
        driver.execute_script("window.scrollTo(0, arguments[0]);", current_height)

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Get the avg placements of the newly displayed augments in a list of WebElements: newStats
        newStats = driver.find_elements(By.XPATH, value="//div[@id='tbl-body']//*[contains(@class, 'flex') and contains(@class, 'items-center') and contains(@class, 'justify-end') and contains(@class, 'px-[14px]') and contains(@class, 'css-1puwvti') and contains(@class, 'tbl-cell-right-border')]")

        for stats in newStats:
            # This is since the height increment scroll doesn't generate the last 2 augments in the table on the DOM
            # so we need to shorten the list to ignore repeated elements (it will repeat elements and we only want the last 6 values in the list)
            if current_height == (height_increment * 8):
                if lastAugmentCounter >= augmentRepeatNumber:
                    if statCounter == 0:
                        first = stats.text
                    if statCounter == 1:
                        second = stats.text
                    if statCounter == 2:
                        third = stats.text
                        print(third)
                        print(indexofStat, augNames[indexofStat], first, second, third)
                        insertVaribleIntoTable(augNames[indexofStat], first, second, third)
                        indexofStat += 1
                        statCounter = -1
                    statCounter += 1
                lastAugmentCounter+= 1
            else: 
                if statCounter == 0:
                    first = stats.text
                if statCounter == 1:
                    second = stats.text
                if statCounter == 2:
                    third = stats.text
                    print(third)
                    print(indexofStat, augNames[indexofStat], first, second, third)
                    insertVaribleIntoTable(augNames[indexofStat], first, second, third)
                    indexofStat += 1
                    statCounter = -1
                statCounter += 1

        # Calculate new scroll height
        current_height += height_increment
        # print("Height increment: %d", height_increment)
        print("Current height: %d", current_height)
        print(bottom)

        if current_height > bottom:
            current_height = bottom
        
    driver.close()

# Function gets average placement form the SQLite3 database table
# takes augment name as a string and stage number as an int ex: 2 (2-1 augment) and returns average placement as a string
# example: getAugmentPlacement("Healing Orbs II", 3)
# return: "4.45"

def getAugmentPlacement(augmentName, stage):
    result = ""

    try:
        sqliteConnection = sqlite3.connect('Augment_Stats.db')
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")

        sqlite_getAugment = ""

        if(stage == 2):
            sqlite_getAugment = "SELECT first FROM AugmentTable WHERE augmentName=?;"
        elif(stage == 3):
            sqlite_getAugment = "SELECT second FROM AugmentTable WHERE augmentName=?;"
        elif(stage == 4):
            sqlite_getAugment = "SELECT third FROM AugmentTable WHERE augmentName=?;"

        data_tuple = (augmentName,)
        cursor.execute(sqlite_getAugment, data_tuple)
        result = cursor.fetchall()
        sqliteConnection.commit()
        # print("Python Variables retrived from AugmentTable")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to retrieve value from AugmentTable", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
    try:
        print(result[0][0])
        return result[0][0]
    except Exception as error:
        return "Could not find augment Stats"

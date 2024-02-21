import sqlite3
import time

from selenium import webdriver
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

# Taken from https://stackoverflow.com/questions/37181403/how-to-set-browser-viewport-size for changing viewport of website in JS using selenium

def set_viewport_size(driver, width, height):
    window_size = driver.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    driver.set_window_size(*window_size)


# From https://www.scrapingbee.com/blog/selenium-python/#chrome-headless-mode
# and https://stackoverflow.com/questions/65755603/selenium-ssl-client-socket-impl-cc-handshake-failed

def fetchStats():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    # Tactics.tools has a missing/expired/invalid SSL certificate, they really need to fix that
    options.add_argument('--ignore-certificate-errors-spki-list')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://tactics.tools/augments")

    # This allows us to get all augments + their respective placement stats at the same time without having to deal with scrolling
    # 1700 is overkill

    bottom_of_page = driver.execute_script("return document.body.scrollHeight")
    set_viewport_size(driver, 1700, bottom_of_page) 

    # Have to wait for the page to load (otherwise sometimes the JS doesn't generate the DOM elements we're searching for)
    time.sleep(1) 

    # Gets the HTML for the augment names from tactics.tools by XPATH
    # Helpful source for XPATH: https://www.youtube.com/watch?v=yZY6-XSTveA&ab_channel=AutomatewithJonathan

    augHTML = driver.find_elements(By.XPATH, value="//*[contains(@class, 'pl-[6px]') and contains(@class, 'font-roboto') and contains(@class, 'font-normal') and contains(@class, 'truncate')]")

    augNames = {}
    augHTMLElements = {}
    augNamesIndex = 0

    for names in augHTML:
        # Gets rid of the first result which is not an augment name (AugmentsGamesPlaceTop 4WinAt ...).
        if(len(names.text) < 30): 
            augNames[augNamesIndex] = names.text
            augHTMLElements[augNamesIndex] = names;
            augNamesIndex+=1

    # Refreshes the table database so stats are update

    dropTableDatabase()

    createTableDatabase()

    # Finds stats of the augment placements at 2-1, 3-2, 4-2 of all augments 

    newStats = driver.find_elements(By.XPATH, value="//div[@id='tbl-body']//*[contains(@class, 'flex') and contains(@class, 'items-center') and contains(@class, 'justify-end') and contains(@class, 'px-[14px]') and contains(@class, 'css-1puwvti') and contains(@class, 'tbl-cell-right-border')]")

    # Goes through selenium webdriver elements and assigns data to placements and groups them in a tuple which we pass to the Sqlite3 database 
    # (augmentName, 2-1 avg placement, 3-2, avg placement, 4-2 avg placement)

    indexofStat = 0
    statCounter = 0;

    for stats in newStats:
        if statCounter == 0:
            first = stats.text
        if statCounter == 1:
            second = stats.text
        if statCounter == 2:
            third = stats.text
            print(indexofStat, augNames[indexofStat], first, second, third)
            insertVaribleIntoTable(augNames[indexofStat], first, second, third)
            indexofStat += 1
            statCounter = -1
        statCounter += 1
        
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

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to retrieve value from AugmentTable", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    try:
        print(result[0][0])
        return result[0][0]
    except Exception as error:
        return "Could not find augment Stats"

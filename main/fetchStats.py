import requests
import sqlite3
from bs4 import BeautifulSoup

URL = "https://tactics.tools/augments"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# Gets the HTML for the augment names from tactics.tools

augHTML = soup.find_all("div", {'class':['pl-[6px]', 'font-roboto', 'font-normal', 'truncate']})

# Dictionary used to store {index, augmentNames} so we can later link up the stats with the augment names

augNames = {}
augNamesIndex = 0

for names in augHTML:
  # Gets rid of the first result which is not an augment name (AugmentsGamesPlaceTop 4WinAt ...).
  if(len(names.text) < 30):
    augNames[augNamesIndex] = names.text
    augNamesIndex+=1

# print(augNames)

# Referenced from https://pynative.com/python-sqlite/#h-create-sqlite-table-from-python
# Creates the table in the database Augment_Stats which will store the augments names and avg placements from tactics.tools in a table

def createTableDatabase():
  try:
      sqliteConnection = sqlite3.connect('Augment_Stats.db')
      cursor = sqliteConnection.cursor()
      print("Connected to SQLite")

      sqlite_create_table = """CREATE TABLE AugmentTable (id INTEGER PRIMARY KEY, augmentName TEXT NOT NULL UNIQUE, first TEXT, second TEXT, third TEXT);"""

      # data_tuple = (id, augmentName, first, second, third)
      cursor.execute(sqlite_create_table)
      sqliteConnection.commit()
      print("Python Variables inserted successfully into AugmentTable")

      cursor.close()

  except sqlite3.Error as error:
      print("Failed to insert Python variable into sqlite table", error)
  finally:
      if sqliteConnection:
          sqliteConnection.close()
          print("The SQLite connection is closed")

# Referenced from https://pynative.com/python-sqlite-insert-into-table/
          
# Work in progress in which the stats are inserted into the data table

def insertVaribleIntoTable(id, augmentName, first, second, third):
    try:
        sqliteConnection = sqlite3.connect('Augment_Stats.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO AugmentTable
                          (id, augmentName, first, second, third) 
                          VALUES (?, ?, ?, ?, ?);"""

        data_tuple = (id, augmentName, first, second, third)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into AugmentTable table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

# Look in the table of stats on tactics.tools stats, otherwise fits too many divs as class names
    
tableBody = soup.find(id='tbl-body')

# Get stats for specific placements at Stage 2-1, 3-2, 4-2, instead of general stats for augments

statsHTML = tableBody.find_all("div", {'class':['flex', 'items-center', 'justify-end', 'px-[14px]', 'css-1puwvti', 'tbl-cell-right-border']})

# This is the text used to determine if the div contains a stat of avg placement or games played 

text="."
blank="—"

indexofStat = 0
statCounter = 0;

# createTableDatabase()

for stats in statsHTML:
  # Sort if they have an aria-label and then if they have a stat denoted by the . in the text instead of games played
  if stats.has_attr("aria-label") and (blank in stats.text):
    print(stats.text)
print(augNames)
    # if statCounter == 0:
    #   first = stats.text
    # if statCounter == 1:
    #   second = stats.text
    # if statCounter == 2:
    #   third = stats.text
    #   print(indexofStat, augNames[indexofStat], first, second, third)
    #   # insertVaribleIntoTable(indexofStat, augNames[indexofStat], first, second, third)
    #   statCounter = -1
    #   indexofStat += 1
    # statCounter += 1

# for stats in statsHTML:
#   statCounter = 0
#   for placement in stats.text:
#     if statCounter == 5:
#       first = placement
#     if statCounter == 6:
#       second = placement
#     if statCounter == 7:
#       third = placement
#     statCounter+=1
#   print(indexofStat, augNames[indexofStat], first, second, third)
#   # insertVaribleIntoTable(indexofStat, augNames[indexofStat], first, second, third)
#   indexofStat+=1

# getAugmentPlacement(soup, "Healing Orbs I", 3)

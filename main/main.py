<<<<<<< Updated upstream
import time
import sys
from fetchStats import *
from statsWindow import *
from PyQt6.QtGui import QScreen
=======
#from fetchStats import *
from overlay import *
>>>>>>> Stashed changes

def main():
  # fetchStats()

<<<<<<< Updated upstream
  # Create application that runs the new window
  app = QApplication([])

  # Stylesheet
  # Helpful reference: https://stackoverflow.com/questions/26162387/qtableview-qtablewidget-grid-stylesheet-grid-line-width
  app.setStyleSheet("""
    QTableView {
      background-color: #0d3868;
      /* background-color: #0f1720; */
      /* gridline-color: #f7fbff; */ 
      gridline-color: #0095ff13;
      color: #eaf6ff; 
      font-size: 20px
    }
  """)

  data = [
          ["Gifts From the Fallen", "4.43"],
          ["Healing Orbs II", "4.53"],
          ["Last Stand", "4.65"],
  ]

  # Inputs of line below explained: 
    # Data is data from above
    # 3 is the stageNumber (3-2)
    # 1920 x 1080 is the last 2 resolution numbers which determine the size of the augment screen (need to adjust for 4K display)

  window = CreateTable(data, 3, 1920, 1080)

  # Potential second monitor support (haven't tested) 
  # referenced from https://stackoverflow.com/questions/6854947/how-to-display-a-window-on-a-secondary-display-in-pyqt
  # number in second line monitors[1] 0 = first monitor 1 = second monitor
  # needs import: "from PyQt6.QtGui import QScreen"

  ''' 

  monitors = QScreen.virtualSiblings(window.screen())
  monitor = monitors[1].availableGeometry()

  '''



  window.show()  # Windows are created hidden by default, otherwise you create invisible window and you have to forcequit process.

  # ******** UNCOMMENT LINES BELOW FOR DEMO **************************************************
  
  '''
   #Simulating a reroll
  time.sleep(0.5)

  # New augment stats
  newData = [
    ["Submit to the Pit", "4.76"],
    ["You Have My Bow", "4.55"],
  ]

  # Update first and third augment choices in the table based on the newData
  window.updateFirstAugmentStats(newData[0][0], newData[0][1])
  # window.updateFirstAugmentStats("Submit to the Pit", "4.76") # <-- this also works
  window.updateThirdAugmentStats(newData[1][0], newData[1][1])

  #Delay
  time.sleep(2)

  #Closes the window
  window.close()

  '''

  #Runs the whole script from above and app.exec() calls thsi and sys.exit stops the script from running after it goes through the whole code
  sys.exit(app.exec())
=======
  app = QApplication([])

  app.setStyleSheet("""
      QLabel {
          margin: 0px;
          padding: 0px;
          font-size: 20px;
          color: "yellow";
       }
  """)

  window = MainWindow(3840, 2160)
  window.createFirstAugmentLabel("4.76")
  window.createSecondAugmentLabel("4.35")
  window.createThirdAugmentLabel("4.60")
  window.show()  # IMPORTANT!!!!! Windows are hidden by default.

  app.exec()
>>>>>>> Stashed changes

if __name__ == "__main__":
  main()
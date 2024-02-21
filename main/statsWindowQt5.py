import time

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMainWindow

class CreateTable(QTableWidget):
    def __init__(self, parent, data, stageNumber, resolution_x, resolution_y):
        # Since the parent is the QMainWindow the QTableWidget is created within the bounds of the QMainWindow area
        super(QTableWidget, self).__init__(parent)
        self.setRowCount(3)
        self.setColumnCount(2)

        self.setColumnWidth(0, 150)
        self.setColumnWidth(1, 120)

        self.setRowHeight(0, 50)
        self.setRowHeight(1, 50)
        self.setRowHeight(2, 50)

        self.__insertFirstAugmentStats(data[0][0], data[0][1])
        self.__insertSecondAugmentStats(data[1][0], data[1][1])
        self.__insertThirdAugmentStats(data[2][0], data[2][1])

        # This sets the height and width dimensions of the table in the QMainWindow
        self.resize(int(resolution_x * 0.22), int(resolution_y * 0.15))

        #Sets vertical and horizontal header to not visible (it just clutters UI)
        self.verticalHeader().setVisible(False);
        self.horizontalHeader().setVisible(False);


    def __insertFirstAugmentStats(self, augmentName, augmentPlacement):
        # Sets augmentName and augmentPlacement to the first row in table
        self.setItem(0,0, QTableWidgetItem(augmentName))
        self.setItem(0,1, QTableWidgetItem(augmentPlacement))
        
    def __insertSecondAugmentStats(self, augmentName, augmentPlacement):
        # Sets augmentName and augmentPlacement to the second row in table
        self.setItem(1,0, QTableWidgetItem(augmentName))
        self.setItem(1,1, QTableWidgetItem(augmentPlacement))
        
    def __insertThirdAugmentStats(self, augmentName, augmentPlacement):
        # Sets augmentName and augmentPlacement to the third row in table
        self.setItem(2,0, QTableWidgetItem(augmentName))
        self.setItem(2,1, QTableWidgetItem(augmentPlacement))
        
    def updateFirstAugmentStats(self, augmentName, augmentPlacement):
        self.setItem(0,0, QTableWidgetItem(augmentName))
        self.setItem(0,1, QTableWidgetItem(augmentPlacement))
        # Update and repaint ensure table values are updated regularly
        self.repaint()
        self.update()
    def updateSecondAugmentStats(self, augmentName, augmentPlacement):
        self.setItem(1,0, QTableWidgetItem(augmentName))
        self.setItem(1,1, QTableWidgetItem(augmentPlacement))
        # Update and repaint ensure table values are updated regularly
        self.repaint()
        self.update()
    def updateThirdAugmentStats(self, augmentName, augmentPlacement):
        self.setItem(2,0, QTableWidgetItem(augmentName))
        self.setItem(2,1, QTableWidgetItem(augmentPlacement))
        # Update and repaint ensure table values are updated regularly
        self.repaint()
        self.update()

class CreateMainWindow(QMainWindow):
    def __init__(self, data, stageNumber, resolution_x, resolution_y):
      QMainWindow.__init__(self)

      # Sets the size of the mainWindow to fit in the bottom left corner of the screen based on resolution size
      # self.setGeometry(x, y, width, height) where x, y, refer to coordinates on the user's screen
      if(resolution_x == 1920 and resolution_y == 1080):
        self.setGeometry(0, 880, int(resolution_x * 0.14), int(resolution_y * 0.16))
      elif(resolution_x == 3840 and resolution_y == 2160):
        self.setGeometry(0, 650, int(resolution_x * 0.28), int(resolution_y * 0.16666))

      # Name of the window based on the stageNumber given
      placeholder = ""
      if stageNumber == 2:
          placeholder = "2-1"
      elif stageNumber == 3:
          placeholder = "3-2"
      elif stageNumber == 4:
          placeholder = "4-2"

      self.setWindowTitle("Augment Stats at " + placeholder + "")

      # Set priority over other windows
      self.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint, on=True)

      # Create the table and show QMainWindow + widget as part of initializiation
      self.table = CreateTable(self, data, stageNumber, resolution_x, resolution_y)
      self.table.show()

      self.show()

    def updateTable(self, tag, stageNumber):
      if tag == "hide":
        placeholder = ""
        if stageNumber == 2:
            placeholder = "2-1"
        elif stageNumber == 3:
            placeholder = "3-2"
        elif stageNumber == 4:
            placeholder = "4-2"

        self.setWindowTitle("Augment Stats at " + placeholder + "")

        # Hides the QMainWindow
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_WState_Hidden)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_DontShowOnScreen, on=True)
      if tag == "show":
        # Shows the QMainWindow
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_WState_Visible)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_DontShowOnScreen, on=False)
        # Updates new values for further augment Stages (3-2, 4-2)
        self.show()
        self.table.repaint()
        self.repaint()
        self.update()

    def updateFirstAugmentStats(self, augmentName, augmentPlacement):
      self.table.updateFirstAugmentStats(augmentName, augmentPlacement)
      self.repaint()
      self.update()

    def updateSecondAugmentStats(self, augmentName, augmentPlacement):
      self.table.updateSecondAugmentStats(augmentName, augmentPlacement)
      self.repaint()
      self.update()

    def updateThirdAugmentStats(self, augmentName, augmentPlacement):
      self.table.updateThirdAugmentStats(augmentName, augmentPlacement)
      self.repaint()
      self.update()

def getInfoFromQueue(data, window, stageNumber):
  # Get the current QTableWidget values and checks if it has changed (compared to what's in variable: data)
  # If it has, then update the table, otherwise do nothing
  # We need to call "hide" and "show" because the QMainWindow will become unresponsive to updates after a certain time (5+ seconds)
  # essentially updateTable is acting as a refresh on this response timer (so we can see the augments)
  if window.table.item(0,0).text() != data[0][0]:
    window.updateTable("hide", stageNumber)
    window.updateTable("show", stageNumber)
    window.updateFirstAugmentStats(data[0][0], data[0][1])
  if window.table.item(1,0).text() != data[1][0]:
    window.updateTable("hide", stageNumber)
    window.updateTable("show", stageNumber)
    window.updateSecondAugmentStats(data[1][0], data[1][1])
  if window.table.item(2,0).text() != data[2][0]:
    window.updateTable("hide", stageNumber)
    window.updateTable("show", stageNumber)
    window.updateThirdAugmentStats(data[2][0], data[2][1])
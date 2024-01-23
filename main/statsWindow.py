# Referenced from https://coderslegacy.com/python/pyqt6-qtablewidget-example/
# and https://stackoverflow.com/questions/25950049/creating-a-transparent-overlay-with-qt
from PyQt6 import QtCore, QtGui
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout

class CreateTable(QTableWidget):
    def __init__(self, data, stageNumber, resolution_x, resolution_y):
        QTableWidget.__init__(self)
        self.setRowCount(3)
        self.setColumnCount(2)

        # Don't think we need layout, so trying to just show table

        # self.vBox = QVBoxLayout()
        # # self.vBox.addWidget(self)
        # self.setLayout(self.vBox)

        self.setColumnWidth(0, 250)
        self.setColumnWidth(1, 200)

        self.setRowHeight(0, 60)
        self.setRowHeight(1, 60)
        self.setRowHeight(2, 60)

        self.__insertFirstAugmentStats(data[0][0], data[0][1])
        self.__insertSecondAugmentStats(data[1][0], data[1][1])
        self.__insertThirdAugmentStats(data[2][0], data[2][1])

        # Name of the window based on the stageNumber given
        placeholder = ""
        if stageNumber == 2:
            placeholder = "2-1"
        elif stageNumber == 3:
            placeholder = "3-2"
        elif stageNumber == 4:
            placeholder = "4-2"

        self.setWindowTitle("Augment Stats at " + placeholder + "")

        # Makes sure window closes on Quit
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_QuitOnClose, on=True)

        # Sets geometry of the window 
        # referenced from: https://stackoverflow.com/questions/25950049/creating-a-transparent-overlay-with-qt
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LayoutDirection.LeftToRight, QtCore.Qt.AlignmentFlag.AlignCenter,
                #Dimensions of your screen (subject to change)
                QtCore.QSize(int(resolution_x * 0.28), int(resolution_y * 0.16666)),
                # QtCore.QSize(self.centralWidget.availableGeometry()),
                QtGui.QGuiApplication.primaryScreen().availableGeometry()
            )
        )

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

    # Update functions for rerolls of augments

    def updateFirstAugmentStats(self, augmentName, augmentPlacement):
        # Assigns new data to first row in table
        self.setItem(0,0, QTableWidgetItem(augmentName))
        self.setItem(0,1, QTableWidgetItem(augmentPlacement))

        # Data update 
        self.update()
        # Visible change
        self.repaint()
        

    def updateSecondAugmentStats(self, augmentName, augmentPlacement):
        # Assigns new data to second row in table
        self.setItem(1,0, QTableWidgetItem(augmentName))
        self.setItem(1,1, QTableWidgetItem(augmentPlacement))

        # Data update
        self.update()
        # Visible change
        self.repaint()

    def updateThirdAugmentStats(self, augmentName, augmentPlacement):
        # Sets items to third row in table
        self.setItem(2,0, QTableWidgetItem(augmentName))
        self.setItem(2,1, QTableWidgetItem(augmentPlacement))

        # Data update
        self.update()
        # Visible change
        self.repaint()

    def QCloseEvent(self):
        QApplication.quit()
    def mouseEvent(self):
        QApplication.quit()
# Testing purposes (moved to main.py)

# app = QApplication([])

# # app.setStyleSheet("""
# #     QLabel {
# #         margin: 0px;
# #         padding: 0px;
# #         font-size: 20px;
# #         color: "yellow";
# #     }
# # """)

# data = [
#           ["Jeweled Lotus II", "4.43"],
#           ["Healing Orbs II", "4.53"],
#           ["Last Stand", "4.65"],
#     ]

# window = CreateTable(data, 3, 1920, 1080)

# window.show()

# time.sleep(10)

# newData = [
#     ["Submit to the Pit", "4.76"],
#     ["You Have My Bow", "4.55"],
# ]

# window.updateFirstAugmentStats(newData[0][0], newData[0][1])
# # window.updateSecondAugmentStats(data[1][0], data[1][1])
# window.updateThirdAugmentStats(newData[1][0], newData[1][1])
# # window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# sys.exit(app.exec())
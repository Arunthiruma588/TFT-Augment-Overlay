from fetchStats import *
from overlay import *

def main():
  # fetchStats()

  data = [
          ["Jeweled Lotus II", "4.43"],
          ["Healing Orbs II", "4.53"],
          ["Last Stand", "4.65"],
    ]

  window = MainWindow(data, 1920, 1080)
  # window.createFirstAugmentLabel("4.76")
  # window.createSecondAugmentLabel("4.35")
  # window.createThirdAugmentLabel("4.60")
  window.show()  # IMPORTANT!!!!! Windows are hidden by default.

  sys.exit(app.exec())

if __name__ == "__main__":
  main()
# Teamfight Tactics Augment Overlay

[![Windows Installation](https://img.shields.io/badge/Windows-10%20%7C%2011-green)](#system-requirements)
[![Python](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://python.org/downloads/)
[![License](https://img.shields.io/github/license/Arunthiruma588/TFT-Tactics.tools-Augment-Overlay)](https://github.com/Arunthiruma588/TFT-Tactics.tools-Augment-Overlay/blob/main/LICENSE)

Overlay that displays live average augment placements from [tactics.tools/augments](https://tactics.tools/augments) during augment selection.

## Showcase

## Table of Contents

- [Features](#features)
- [Patch Notes](#patch-notes)
- [Installation](#installation)
  - [System Requirements](#system-requirements)
  - [Guide](#guide)
- [Usage](#usage)
- [Documentation](#documentation)
- [Frequently Asked Questions](#frequently-asked-questions)
- [License](#license)
- [Privacy Policy](#privacy-policy)
- [Acknowledgement](#acknowledgment)
  - [Contributors](#contributors)

## Features

* Easy to use.
* Live updates in-game.
* Stats update every main call.

## Patch Notes

[Upcoming] **14.4** - **DISCLAIMER - Please allow us to test whether the tool works with Vanguard**. More info in [Frequently Asked Questions](#frequently-asked-questions)

[Live] **14.3** - The Teamfight Tactics Augment Overlay tool is safe to use and working as intended.

## Installation  
  ### System Requirements
  
  * #### Windows 10, Windows 11
  * #### 1920 x 1080 resolution (1080p)
  
  We currently do not support Mac or Linux as our testing for those devices is limited.  
  
  As of upcoming patch 14.4 in League of Legends, Riot Games has made the decision to stop supporting Windows 7, 8, and 8.1, meaning a Windows installation of 10 or later is required to play. If you do not have those installed we recommend getting a device or license key that has those versions of Windows as soon as you can.

  Currently our tool only supports 1920 x 1080 resolution. If your monitor supports 1920 x 1080 resolution we recommend switching resolutions before using the Augment Overlay tool, otherwise the tool may not function correctly.
  
  ### Guide
## Usage
## Documentation

- If you are interested in how the tool works check out our [OVERVIEW.md](docs/OVERVIEW.md).
- For the complete documentation on all individual functions and files please check out our [docs](docs/).
## Frequently Asked Questions
  <details>
  <summary>
  <b>Is the Teamfight Tactics Augment Overlay tool allowed in TFT?</b>
  </summary>


  - TLDR: Yes  
   

  - Here is Mortdog, the lead game designer of TFT, presenting Riot's take on overlays: [Youtube Clip](https://www.youtube.com/watch?v=MoIueRc8IqQ&ab_channel=Mortdog-TFT).
   
  - Since our tool is basically a mirror of [tactics.tools/augments](https://tactics.tools/augments) it is no different than looking up stats on the [tactics.tools/augments](https://tactics.tools/augments) after looking up augment names by yourself during the game, which is allowed. Since these stats are available to all individuals before the game it does not violate Riot TOS, thus our Teamfight Tactics Augment Overlay tools does not provide any unfair advantage to any players more than tactics.tools/augments does.

  - Our tool only displays average placement stats from Diamond+ per augment and does not convince the player in any way, shape, or form to choose the augment with the highest average placement stat or any other augment. Our tool is meant to be merely be a reference for displaying stats and replace having to manually search for average augment placements on tactics.tools/augments during the game.
 </details>
 <details>
  <summary>
  <b>Will I get banned for using the Teamfight Tactics Augment Overlay tool?</b>
  </summary>
   

  - TLDR: Patch 14.3: No. Patch 14.4: We don't know.  


  - Patch 14.3 - overlays and tools are allowed in TFT. In addition, we have been testing for 2 weeks with this tool and our account has not been banned or flagged.  

  - Patch 14.4 - Riot is releasing Vanguard, their kernel anti-cheat, to the League of Legends Client and thus Teamfight Tactics this patch. Although our tool does not interact with in-game files at all, we are unsure of whether Vanguard will flag it as a cheat or not, and thus we do not know. We are not liable or responsible for any damages or suspensions placed on Riot Accounts using our Teamfight Tactics Augment Overlay tool if it is flagged by Vanguard during TFT games when Vanguard is released.
 </details>
 
## License

- The main code is licensed under [GPLv3](https://github.com/Arunthiruma588/TFT-Tactics.tools-Augment-Overlay/blob/main/LICENSE).
- Licenses to imports used in this code fall under the [Apache Software License (2.0)](https://www.apache.org/licenses/LICENSE-2.0), the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt), and the [HPND License](https://directory.fsf.org/wiki/License:HPND) which are all compatable with [GPLv3](https://github.com/Arunthiruma588/TFT-Tactics.tools-Augment-Overlay/blob/main/LICENSE)
- fetchStats.py (changes if any can be found and explained in [docs/fetchStats.md](docs/fetchStats.md)):
  - The import of [Selenium 4.16.0](https://pypi.org/project/selenium/4.16.0/) is licensed under the [Apache Software License (2.0)](https://www.apache.org/licenses/LICENSE-2.0).
  - The import of [webdriver-manager 4.0.1](https://pypi.org/project/webdriver-manager/) is licensed under the [Apache Software License](https://www.apache.org/licenses/).
  - The import of [requests 2.31.0](https://pypi.org/project/requests/) is licensed under the [Apache Software License (Apache 2.0)](https://www.apache.org/licenses/LICENSE-2.0).
  - Functions *dropTableDatabase()*, *createTableDatabase()*, *insertVariableIntoTable(augmentName, first, second, third)*, and *getAugmentPlacement(augmentName, stage)* are referenced from the [python docs on sqlite3](https://docs.python.org/3/library/sqlite3.html) which is licensed under [PSF License Agreement](https://docs.python.org/3/license.html#psf-license-agreement-for-python-release) which is compatible with [GPLv3](https://github.com/Arunthiruma588/TFT-Tactics.tools-Augment-Overlay/blob/main/LICENSE).
  - Function *set_viewport_size(driver, width, height)* is copied with no changes from a [stackoverflow](https://stackoverflow.com/questions/37181403/how-to-set-browser-viewport-size) user response by user Florent B. on May 12, 2016 at 9:49. Stackoverflow code is licensed under the [CC BY-SA 4.0 Deed](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en) which is compatible with [GPLv3](https://github.com/Arunthiruma588/TFT-Tactics.tools-Augment-Overlay/blob/main/LICENSE).
  - The first part of function *fetchStats()* used to address SSL certificate errors was built referencing a [response on stackoverflow](https://stackoverflow.com/questions/65755603/selenium-ssl-client-socket-impl-cc-handshake-failed) by user J.M. Arnold on Jan 26, 2021 at 18:17. Stackoverflow code is licensed under the [CC BY-SA 4.0 Deed](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en) which is compatible with [GPLv3](https://github.com/Arunthiruma588/TFT-Tactics.tools-Augment-Overlay/blob/main/LICENSE).
- statsWindowQt5.py (changes if any can be found and explained in [docs/statsWindowQt5.md](docs/statsWindowQt5.md)):
  - The import of [PyQt5 5.15.10](https://pypi.org/project/PyQt5/) was used to build statsWindowQt5.py and is licensed under [GPLv3](https://github.com/Arunthiruma588/TFT-Tactics.tools-Augment-Overlay/blob/main/LICENSE) and thus is compatible as our license is the same [license](https://github.com/Arunthiruma588/TFT-Tactics.tools-Augment-Overlay/blob/main/LICENSE).
- identification.py (changes if any can be found and explained in [docs/identification.md](docs/identification.md)):
  - The import of [pytesseract 0.3.10](https://pypi.org/project/pytesseract/) is licensed under the [Apache Software License (Apache Software License 2.0)](https://www.apache.org/licenses/LICENSE-2.0).
  - The import of [python image-search 1.3.0](https://pypi.org/project/python-imagesearch/) is licensed under the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).
  - The import of [pillow 10.2.0](https://pypi.org/project/pillow/) is licensed under the [HPND License](https://directory.fsf.org/wiki/License:HPND).
  - The import of [setuptools 69.0.3](https://pypi.org/project/setuptools/69.0.3/) is licensed under the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).
- testing.py has no relevant licenses are it is only used to manually test changes.

This compiled list shows all of the code in this repository used,referenced, or imported from other sources has been cited/documented and can legally fall under the [GPLv3](https://github.com/Arunthiruma588/TFT-Tactics.tools-Augment-Overlay/blob/main/LICENSE) in use. 

Each distribution made by cloning the repository **must make sure they have a copy of the [GPLv3](https://github.com/Arunthiruma588/TFT-Tactics.tools-Augment-Overlay/blob/main/LICENSE)**.

## Privacy Policy

*We, us* defined as owners and contributors of the Teamfight Tactics Augment Overlay tool want to inform you about the way that the Teamfight Tactics Augment Overlay tool handles and collects information. All information collected and stored by the tool will never be transferred to any other network/party/user unless specifically done so by the user activating or operating the tool. Unless consensually shared with us by the user for development fixes, **we will never ask for access to any of our users' augmentName screenshots or other personal or private information**. All such information shared with us will only be used for development purposes and will never be collected or transferred to any other network/party/user.

## Acknowledgment
- We want to firstly acknowledge and thank [Riot Games](https://riotgames.com), the owners and creators of [Teamfight Tactics](https://teamfighttactics.leagueoflegends.com/).
- Secondly we want to acknowledge and thank the creators and contributers of [tactics.tools](https://tactics.tools). Our tool is meant to be an extension of their fantastic analysis of stats in Teamfight Tactics and our tool cannot function without their amazing work.
- Lastly we want to acknowledge and thank our contributers for all their hard work.
### Contributors
- [KonstantinLiehr](https://github.com/KonstantinLiehr)
- [Arunthiruma588](https://github.com/Arunthiruma588)

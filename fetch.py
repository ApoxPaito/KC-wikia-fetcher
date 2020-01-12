import os
import urllib.request
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import time, json

fwe = False
ships = []
shipsFilename = "ships.txt"
logFilename = "log.txt"

if not os.path.isdir("img"):
    os.mkdir("img")

if not os.path.isfile(shipsFilename):
    raise SystemExit("No ships.txt wasn't found. Make sure a Text file named ships.txt containing " +
        "the ship IDs and names in format of \"ID - Name\" exists.")

with open(shipsFilename, "r") as shipsFile:
    ships = shipsFile.readlines()

with open(logFilename, "w") as logFile:
	#####################################################################################################################
	# -- Change the directory down there with the directory of the profile you've created and logged into Wikia with -- #
	#####################################################################################################################
    ffprofile = webdriver.FirefoxProfile("C:/Users/Apox/AppData/Roaming/Mozilla/Firefox/Profiles/8wk9rbul.KCWikiaFetcher")

    option = webdriver.FirefoxOptions()
    option.add_argument("-private")
    option.add_argument("-headless")

    browser = webdriver.Firefox(ffprofile)
    for ship in ships:
        shipID = ship[:ship.find("-") - 1].rstrip()
        shipName = ship[ship.find("-") + 2:].rstrip()
        url = f"https://kancolle.fandom.com/wiki/File:{shipName}_Full.png"
        try:
            browser.get(url)
            imageUrl = browser.find_element_by_xpath("//meta[@property='og:image']").get_attribute("content")
            logFile.write(f"INFO - Fetched image URL from {url}.\n")
            logFile.write(f"INFO - Downloading {imageUrl} ...\n")
            urllib.request.urlretrieve(imageUrl, f"img/{shipID}.png")
        except:
            msg = f"ERR - Failed to get {shipID} - {shipName} image, check name or try again."
            logFile.write(f"{msg}\n")
            print(msg)
            fwe = True

browser.quit()
if fwe:
    print("Finished with errors, check log.txt for more info.")
else:
    print("Finished with no errors.")
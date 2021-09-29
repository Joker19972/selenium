from selenium import webdriver
#from selenium.webdriver.common import keys
import time
from fake_useragent import UserAgent
import pandas as pd
import json


user_agent = UserAgent()



driver = webdriver.Chrome(executable_path="C:\\Users\\Internet_Club\\Downloads\\selenium\\chromedriver"
                                          "\\chromedriver.exe")
pages = 1733
try:
    for page in range(1,2):
        url = f"https://steamcommunity.com/market/search?appid=730#p{page}_popular_desc"

        driver.get(url)
        time.sleep(3)

        items =len(driver.find_elements_by_class_name("market_listing_row"))

        total = []
        for item in range(items):
            skin = driver.find_element_by_class_name("market_listing_item_name").click()
            time.sleep(5)
            skin_name = driver.find_element_by_id("largeiteminfo_item_name").text
            skin_price = driver.find_element_by_id("market_commodity_forsale").text
            skin_info = {
                "skin-name": skin_name,
                "skin_price": skin_price
            }
            total.append(skin_info)
            print(total)

    with open("Skin-info.json","a") as file:
        json.dump(total,file,indent=4,ensure_ascii=False)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

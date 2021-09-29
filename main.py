from selenium import webdriver
from selenium.webdriver.common import keys
import time
from fake_useragent import UserAgent


user_agent = UserAgent()

url = "https://www.vk.com/"

driver = webdriver.Chrome(executable_path="C:\\Users\\Internet_Club\\Downloads\\selenium\\chromedriver"
                                          "\\chromedriver.exe")

try:
    driver.get(url=url)
    time.sleep(5)

    email_input = driver.find_element_by_id("index_email")
    email_input.clear()
    email_input.send_keys("87476821700")
    time.sleep(2)

    password_input = driver.find_element_by_id("index_pass")
    password_input.clear()
    password_input.send_keys("Little2019")
    time.sleep(2)
    password_input.send_keys(keys.Keys.ENTER)
    time.sleep(10)

    message = driver.find_element_by_id("l_msg").click()
    time.sleep(5)
    man = driver.find_element_by_class_name("nim-dialog--content").click()
    time.sleep(4)

    write_message = driver.find_element_by_id("im_editable0")
    write_message.clear()
    write_message.send_keys("все брат")
    time.sleep(2)
    write_message.send_keys(keys.Keys.ENTER)
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

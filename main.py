from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
import time
import random

# def login(username, password):
#     browser = webdriver.Chrome("/path/to/chromedriver")
#     try:
#         browser.get("https://www.instagram.com")
#         time.sleep(random.randrange(3, 5))

#         username_input = browser.find_element("name","username")
#         username_input.clear()
#         username_input.send_keys(username)

#         time.sleep(2)

#         password_input = browser.find_element("name","password")
#         password_input.clear()
#         password_input.send_keys(password)

#         password_input.send_keys(Keys.ENTER)
#         time.sleep(50)

#         browser.close()
#         browser.quit()
#     except Exception as ex:
#         print(ex)
#         browser.close()
#         browser.quit()

# login(username,password)  


def hashtag_search(username, password, hashtag):

    browser = webdriver.Chrome(executable_path ="/path/to/chromedriver")
    try:
        browser.get("https://www.instagram.com")
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element("name","username")
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element("name","password")
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(50)

        try:
            browser.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
            time.sleep(5)
            hrefs = browser.find_element("By.TAG_NAME", "h1")

            for item in hrefs:
                href = item.get_attribute("href")
                print(href)

            browser.close()
            browser.quit()
        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()

hashtag_search(username, password, "surfing")


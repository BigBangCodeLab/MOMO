import re
from selenium.webdriver.common.keys import Keys
import time

from Utility.open_control import open_control


def search_control(query, driver):
    if "youtube" in query:
        search_query = query.split("search", 1)[1].replace("in youtube", "").replace("on youtube", "").strip()
        search_in_youtube(driver, search_query)

def search_in_youtube(driver,query):
    open_control("youtube", driver)
    time.sleep(5)  # Wait for the page to load
    search_box = driver.find_element("name", "search_query")
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
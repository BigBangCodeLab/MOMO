import datetime

from Utility.close_control import close_control
from Utility.open_control import open_control
from Utility.scroll_control import scroll_up_down_web
from Utility.search_control import search_control
from selenium import webdriver

driver = None

def commandControl(query):
    global driver
    if "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}"
    
    elif query.startswith("open"):
        if driver is None:
            driver = webdriver.Chrome()
        driver.get('https://www.google.com')
        open_control(query, driver)

    elif query.startswith("search"):
        if driver is None:
            driver = webdriver.Chrome()
        driver.get('https://www.google.com')
        search_control(query, driver)
        
    elif query.startswith("close"):
        close_control(query, driver)
        
    elif query.startswith("scroll"):
        scroll_up_down_web(driver, query)
        

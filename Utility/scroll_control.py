def scroll_up_down_web(driver, direction):
    if "up" in direction:
        driver.execute_script("window.scrollBy(0, -500);")
    else:
        driver.execute_script("window.scrollBy(0, 500);")

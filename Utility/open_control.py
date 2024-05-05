import time

def open_control(query, driver):
    sites = {
        "youtube": "https://www.youtube.com/",
        "facebook": "https://www.facebook.com/",
        "whatsapp": "https://web.whatsapp.com/",
        "instagram": "https://www.instagram.com/"
    }
    
    for site_keyword, site_url in sites.items():
        if site_keyword in query.lower():
            existing_tabs = driver.window_handles
            tab_open = False
            
            for tab in existing_tabs:
                driver.switch_to.window(tab)
                if site_url in driver.current_url:
                    tab_open = True
                    break
            
            if not tab_open:
                if existing_tabs:
                    driver.switch_to.window(existing_tabs[0])
                    driver.execute_script(f"window.open('{site_url}', '_blank');")
                    time.sleep(3)

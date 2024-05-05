def close_control(query, driver):
    if "browser" in query:
        if driver:
            driver.quit()
    elif any(site in query for site in ["youtube", "facebook", "whatsapp", "instagram"]):
        if driver:
            # Close the tab only if it matches the specified sites
            current_tabs = driver.window_handles
            
            # Create a dictionary to store tabs for each site
            tabs_by_site = {site: [] for site in ["youtube", "facebook", "whatsapp", "instagram"]}
            
            # Group tabs by site
            for tab in current_tabs:
                driver.switch_to.window(tab)
                for site in tabs_by_site:
                    if site in driver.current_url:
                        tabs_by_site[site].append(tab)
            
            # Close a tab for the specific site
            for site in ["youtube", "facebook", "whatsapp", "instagram"]:
                if site in query and tabs_by_site[site]:
                    driver.switch_to.window(tabs_by_site[site][0])
                    driver.close()
                    break  # Remove this line if you want to close all tabs for the specific site

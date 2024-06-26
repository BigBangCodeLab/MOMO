import datetime
import re

from Listen.ListenJs import Listen
from Speak.SpeakOffline import Speak
from Utility.close_control import close_control
from Utility.common import get_ip, get_speedtest, get_weather, system_stats, systemInfo
from Utility.open_control import open_control
from Utility.scroll_control import scroll_up_down_web
from Utility.search_control import search_control
from selenium import webdriver

from Utility.system_utility import SystemTasks, TabOpt, WindowOpt
from project_management import get_project_path, open_folder_dialog, open_vscode, save_project_path

driver = None

def commandControl(query):
    sys_ops = SystemTasks()
    tab_ops = TabOpt()
    win_ops = WindowOpt()

    global driver
    if "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}"
    
    elif "speed test" in query:
        return get_speedtest()

    elif "ip" in query:
        return get_ip()

    elif "weather" in query:
        city = re.search(r"(in|of|for) ([a-zA-Z]*)", query)
        if city:
            city = city[2]
            return get_weather(city)
        else:
            return get_weather()

    elif "system status" in query:
        return system_stats()

    elif "info" in query or "specs" in query or "information" in query:
        return systemInfo()

    elif query.startswith("open") and not query.endswith("project"):
        if driver is None:
            driver = webdriver.Chrome()
        driver.get('https://www.google.com')
        open_control(query, driver)
    
    elif query.endswith("project"):
        if 'register' in query:
            project_path = open_folder_dialog()
            Speak(f"Got the project path now tell me the project short name for that project")
            bnText = Listen()
            project_name = bnText.lower()
            save_project_path(project_name, project_path)
            return f"Registered {project_name}"

        open_index = query.find("open")
        project_index = query.find("project")

        # Extract the project name between "open" and "project"
        if open_index != -1 and project_index != -1:
            project_name = query[open_index+len("open"):project_index].strip()
            print(project_name)
            project_path = get_project_path(project_name.lower())
            print(project_path)
            if project_path is None:
                return f"Couldn't find the project {project_name}"
            else:
                open_vscode(project_path)
                return f"Opened {project_name}" 

    elif query.startswith("search"):
        if driver is None:
            driver = webdriver.Chrome()
        driver.get('https://www.google.com')
        search_control(query, driver)
        
    elif query.startswith("close"):
        close_control(query, driver)
        
    elif query.startswith("scroll"):
        scroll_up_down_web(driver, query)
        
    elif query.startswith("scroll"):
        scroll_up_down_web(driver, query)
    

    elif "select" in query:
        sys_ops.select()
    elif "copy" in query:
        sys_ops.copy()
    elif "paste" in query:
        sys_ops.paste()
    elif "delete" in query:
        sys_ops.delete()
    elif "new" in query:
        sys_ops.new_file()
    elif "save" in query:
        sys_ops.save()
    elif "switch" in query and "tab" in query:
        tab_ops.switchTab()
    elif "close" in query and "tab" in query:
        tab_ops.closeTab()
    elif "new" in query and "tab" in query:
        tab_ops.newTab()
    elif "close" in query:
        win_ops.closeWindow()
    elif "switch" in query:
        win_ops.switchWindow()
    elif "minimize" in query:
        win_ops.minimizeWindow()
    elif "maximize" in query:
        win_ops.maximizeWindow()
    elif "screenshot" in query:
        win_ops.Screen_Shot()
        

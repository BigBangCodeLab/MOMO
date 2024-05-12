import speedtest
import requests
import wmi
import math
import psutil

def get_speedtest():
    internet = speedtest.Speedtest()
    return (f"Your network's Download Speed is {round(internet.download() / 8388608, 2)}MBps Your network's Upload Speed is {round(internet.upload() / 8388608, 2)}MBps")


def get_ip():
    response = requests.get(f'http://ip-api.com/json/').json()
    return (f'Your IP address is {response["query"]}')


def get_weather(city=''):
    if city:
        response = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3c7173ebbdad653f86ba604719c58ce7&units=metric').json()
        return (f'It {response["main"]["temp"]}° Celsius {response["weather"][0]["main"]} But feels like {response["main"]["feels_like"]}° Celsius Wind is blowing at {round(response["wind"]["speed"] * 3.6, 2)}km/h Visibility is {int(response["visibility"] / 1000)}km')

def systemInfo():
    c = wmi.WMI()
    my_system_1 = c.Win32_LogicalDisk()[0]
    my_system_2 = c.Win32_ComputerSystem()[0]
    return (f"Total Disk Space: {round(int(my_system_1.Size)/(1024**3),2)} GB Free Disk Space: {round(int(my_system_1.Freespace)/(1024**3),2)} GB Manufacturer: {my_system_2.Manufacturer} Model: {my_system_2. Model} Owner: {my_system_2.PrimaryOwnerName} Number of Processors: {psutil.cpu_count()} System Type: {my_system_2.SystemType}")


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def system_stats():
    cpu_stats = str(psutil.cpu_percent())
    battery_percent = psutil.sensors_battery().percent
    memory_in_use = convert_size(psutil.virtual_memory().used)
    total_memory = convert_size(psutil.virtual_memory().total)
    return (f"Currently {cpu_stats} percent of CPU is being used {memory_in_use} of RAM out of total {total_memory} is being used battery level is at {battery_percent}%")

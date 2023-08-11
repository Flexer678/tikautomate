from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   options=webdriver.FirefoxOptions()
)
#driver.get("https://www.tiktok.com/login/")
driver.get("https://www.tiktok.com/@angel_movie612/video/7261607929554406699")
print("login")


def autoscroll(scrolls):
    time.sleep(10)
    for x in range (scrolls):
        
        downBtn = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[4]/button[2]')
        videoDuration = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[6]/div[2]/div[1]/div[2]')
    print(videoDuration)
    driver.quit()
    
autoscroll(5)

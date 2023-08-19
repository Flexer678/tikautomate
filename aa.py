from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium_stealth import stealth
import random
import undetected_chromedriver as uc
import time

options = webdriver.ChromeOptions()

#options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_experimental_option('useAutomationExtension', False)
#options.add_argument("--use_subprocess")
#options.add_argument("--headless")
driver = uc.Chrome( options = options)



timers = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]
variables = [
    "https://www.tiktok.com/login/phone-or-email/email", "//input[@placeholder='Email or username']",
    "//input[@placeholder='Password']", "//button[@type='submit']"
]

#with open('user.txt') as f:
#    line = f.readlines()
username = "alexander.mosomi46@gmail.com"
password = "Westler@567"

start_b = time.time()
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

def sleeper():
        time.sleep(float("0." + random.choice(timers[0:3]) + random.choice(timers[0:4]) + random.choice(timers[0:9])))

def logging_in():
        driver.get(variables[0])

        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, variables[1])))
            fieldForm = driver.find_element("xpath", variables[1])
        except:
                print("quittedd")
                driver.quit()
        finally:
                for i in username:
                        fieldForm.send_keys(i)
                        sleeper()

        fieldForm = driver.find_element("xpath", variables[2])
        for i in password:
                fieldForm.send_keys(i)
                sleeper()

        try:
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, variables[3])))
        except:
                print("quitted")
                driver.quit()
        finally:
                button = driver.find_element("xpath", variables[3])
                button.click()

logging_in()
end = time.time()
print(f"You has been succesfully logged in to your tik tok account, script executed in {end-start_b}s")
time.sleep(30)



def autoscroll(times):
        
        islogedIn = True
        if islogedIn :
            
            driver.get("https://www.tiktok.com/foryou")
            time.sleep(5)
            canvas = driver.find_element("xpath", '//*[@id="one-column-item-2"]')     
            canvas.click()
            time.sleep(10)
            for x in range(times):
            #waits for the browser to load
                driver.implicitly_wait(2)
                downbutton = driver.find_element("xpath", '//*[@id="app"]/div[2]/div[4]/div/div[1]/button[3]')
                number = driver.find_element("xpath", '//*[@id="app"]/div[2]/div[4]/div/div[1]/div[3]/div[2]/div[2]').get_attribute("innerText")
                sleep_duration = str(number[number.find("/")+1: len(number)])

            
                get_time = (int(sleep_duration[0:2])*60) + int(sleep_duration[3:len(sleep_duration)])
                print(get_time, "seconds till scroll")
                #self.driver.implicitly_wait(get_time +1)
                time.sleep(get_time)
                downbutton.click()
            
            
#autoscroll(56)
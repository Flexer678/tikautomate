
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium_stealth import stealth
import undetected_chromedriver as uc
#remove .v2
import time
import random


class tiktokbot:
    
    timers = [
        "10", "1", "2", "7", "4", "5", "6", "7", "8", "9"
]
    
    loginVariables = [
    "https://www.tiktok.com/login/phone-or-email/email",
    "//input[@placeholder='Email or username']",
    "//input[@placeholder='Password']", "//button[@type='submit']"
]

    scrollVariables = [
        '//*[@id="one-column-item-2"]', '//*[@id="app"]/div[2]/div[4]/div/div[1]/button[3]', '//*[@id="app"]/div[2]/div[4]/div/div[1]/div[3]/div[2]/div[2]'
    ]
    
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.islogedIn = False
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--proxy-bypass-list=<-loopback>')
        self.driver = uc.Chrome(options=self.options, use_subprocess=True)
        stealth(self.driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
        )
        self.actions = ActionChains(self.driver)
       
       
        
    #if only you had the patience and consistency 
    # if only i read my code to make sure it worked
    #chrome --v114
    
    
    
    def shoutout():
        print("shout out to Zinkq on github")
        time.sleep(6)
    
    def getBot(self):
        return self.drivers

    def login(self):
        print("workinf")
        self.driver.get(tiktokbot.loginVariables[0])
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,  tiktokbot.loginVariables[1])))            
            fieldForm =self.driver.find_element("xpath", tiktokbot.loginVariables[1])
        except:
            self.driver.quit()
        finally:
            for i in self.email:
                fieldForm.send_keys(i)
                float("0."+random.choice(tiktokbot.timers[0:9]) + random.choice(tiktokbot.timers[0:9]) + random.choice(tiktokbot.timers[0:9]))

        
        fieldForm = self.driver.find_element("xpath",  tiktokbot.loginVariables[2])
        for i in self.password:
            fieldForm.send_keys(i)
            float("0."+random.choice(tiktokbot.timers[0:9]) + random.choice(tiktokbot.timers[0:9]) + random.choice(tiktokbot.timers[0:9]))

        try:
                WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,  tiktokbot.loginVariables[3])))
        except:
                self.driver.quit()
        finally:
                button = self.driver.find_element("xpath",  tiktokbot.loginVariables[3])
                button.click()
                self.islogedIn = True
                                

    def autoscroll(self,times,mute):
    
        self.islogedIn = True
        if self.islogedIn :
            time.sleep(20)
            #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="one-column-item-2"]' )))            
            canvas = self.driver.find_element("xpath", tiktokbot.scrollVariables[0])     
            canvas.click_and_hold()
            time.sleep(5)
            for x in range(times):
            #waits for the browser to load
                self.driver.implicitly_wait(2)
                WebDriverWait(self.driver,10)
                downbutton = ""
                Vidlength = ""
                while downbutton == "" and Vidlength == "":
                    try:
                        downbutton = self.driver.find_element("xpath", tiktokbot.scrollVariables[1])
                        Vidlength = self.driver.find_element("xpath", tiktokbot.scrollVariables[2]).get_attribute("innerText")
                        sleep_duration = str(Vidlength[Vidlength.find("/")+1: len(Vidlength)])
                        get_time = (int(sleep_duration[0:2])*60) + int(sleep_duration[3:len(sleep_duration)])
                    except:
                        time.sleep(30)
                
                
                print(get_time, "seconds till scroll")
                #self.driver.implicitly_wait(get_time +1)
                time.sleep(get_time)
                downbutton.click()
        
        else:
            print("ur not logged in")
    




        

        
    
    #go to upload location
    #click video to select
    #wait for caption to loaf
    #change caption
    #wait for video to post
     
    #click post
    #repeat
    #wait for upload
    def upload(self,files):
        if self.islogedIn:
            self.driver.get("https://www.tiktok.com/upload?lang=en")
            uploadnewvid = '//*[@id="root"]/div/div/div/div[2]/div[2]/div[2]/div[9]/div/div[2]/div[1]'
        
            
            
    




bot = tiktokbot(open("logindetails/email.txt", 'r').read(), open("logindetails/password.txt", 'r').read())
bot.login()

bot.autoscroll(50,True)


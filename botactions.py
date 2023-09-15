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
from pynput.keyboard import Key, Controller
from pynput import mouse
from seleniumbase import BaseCase
import time
import random


class tiktokbot(BaseCase):
    
    timers = [
        "0", "2", "1", "3", "4", "5", "6", "7", "8", "9"
]
    list = [True, False]
    
    loginVariables = [
    "https://www.tiktok.com/login/phone-or-email/email",
    "//input[@placeholder='Email or username']",
    "//input[@placeholder='Password']", "//button[@type='submit']"
]

    scrollVariables = [
        '//*[@id="one-column-item-2"]', 
        '//*[@id="app"]/div[2]/div[4]/div/div[1]/button[3]', 
        '//*[@id="app"]/div[2]/div[4]/div/div[1]/div[3]/div[2]/div[2]'
    ]
    
    scrollVariablesInteraction = {
        "like_button" : '//*[@id="app"]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/button[1]/span' ,
        "save_button": '//*[@id="app"]/div[2]/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/button[3]/span',
        "comment_field": '//*[@id="app"]/div[2]/div[4]/div/div[2]/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/div/div/span/span',
    }
    
    uploadVariables ={
        "upload_link" : 'https://www.tiktok.com/creator-center/upload?from=upload',
        "select_file_btn" : '//*[@id="root"]/div/div/div/div/div/div/div/div/div[5]/button'
    }
    
    commentfile = "comments.txt"
    
    def __init__(self, email, password, profile, directory):
        self.email = email
        self.password = password
        self.islogedIn = True
        self.options = webdriver.ChromeOptions()
        self.profile = profile
        self.keyboard = Controller()
        self.directory =directory
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--user-data-dir='+self.directory)
        self.options.add_argument('--profile-directory='+self.profile)
        #self.options.add_argument('--proxy-bypass-list=<-loopback>')
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
       
       
        
    
    
    
    def shoutout():
        print("shout out to Zinkq on github")
    
    def getBot(self):
        return self.driver


    def login(self):
        self.islogedIn = True
        if self.islogedIn:
            print("WORKING")
            self.driver.get("https://www.tiktok.com/foryou")
        else:
            self.driver.get(tiktokbot.loginVariables[0])
            try:
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,  tiktokbot.loginVariables[1])))            
                fieldForm =self.driver.find_element("xpath", tiktokbot.loginVariables[1])
            except:
                self.driver.quit()
            finally:
                for i in self.email:
                    fieldForm.send_keys(i)
                    time.sleep(float("0."+random.choice(tiktokbot.timers[0:4]) + random.choice(tiktokbot.timers[0:7]) + random.choice(tiktokbot.timers[0:9])))

            
            fieldForm = self.driver.find_element("xpath",  tiktokbot.loginVariables[2])
            for i in self.password:
                fieldForm.send_keys(i)
                time.sleep(float("0."+random.choice(tiktokbot.timers[0:4]) + random.choice(tiktokbot.timers[0:7]) + random.choice(tiktokbot.timers[0:9])))
                
            try:
                    WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,  tiktokbot.loginVariables[3])))
            except:
                    self.driver.quit()
            finally:
                    button = self.driver.find_element("xpath",  tiktokbot.loginVariables[3])
                    button.clickandhold()
                    self.islogedIn = True


    
   

    def getComments():
        with open(tiktokbot.commentfile,  encoding='utf-8-sig') as file:
            lines = len(file.readlines())

        book  = random.randrange(2,lines)
    
        file1 = open("comments.txt","r+")
        file =open("comments.txt")
        content = file.readlines()

    
        return (content[book])
    
    def clickInteraction(self,type):
        #boolean variables
        # 0 to save ,1 to like 
        if type == 1:
            try:
                WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,  tiktokbot.scrollVariablesInteraction['like_button'])))
                Likebutton = self.driver.find_element("xpath", tiktokbot.scrollVariablesInteraction["like_button"])
                Likebutton.click()
                
                print("video liked")
            except:
                print("unable to like video")
        elif type == 2:
            try:
                WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,  tiktokbot.scrollVariablesInteraction['like_button'])))
                Likebutton = self.driver.find_element("xpath", tiktokbot.scrollVariablesInteraction["save_button"])
                Likebutton.click()
                print("video saved")
            except:
                print("unable to like video")
        else:
            print("not liked or saved")
        time.sleep(2)
        
    #threadimg required
    #currently not working
    def comment(self):
        print("commenting")
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,  tiktokbot.scrollVariablesInteraction['comment_field'])))
            commentform = self.driver.find_element("xpath", tiktokbot.scrollVariablesInteraction["comment_field"])
            for i in tiktokbot.getcomments():
                commentform.send_keys(i)
                time.sleep(float("0."+random.choice(tiktokbot.timers[0:4]) + random.choice(tiktokbot.timers[0:7]) + random.choice(tiktokbot.timers[0:9])))
                self.keyboard.press(Key.enter)
            print("commenting on this video")
        except:
            print("trying to comment")
            print("comment failed")
            pass
        
    def autoscroll(self,times,mute):
    
        self.islogedIn = True
        if self.islogedIn :
            self.driver.get("https://www.tiktok.com/foryou")
            #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="one-column-item-2"]' )))            
           # canvas = self.driver.find_element("xpath",'//*[@id="one-column-item-0"]/canvas')     
           # canvas.click()
            print("canvas clicked")
            
           
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
                
                
                choice = random.choice(tiktokbot.list)
                if choice == True:
                    if random.randint(0,1) == 1:
                        tiktokbot.comment
                    time.sleep(get_time - random.randint(1,3))
                    print("about", get_time, "seconds till scroll")
                    tiktokbot.clickInteraction(self,random.randint(0,2))
  
                   
                   
                    
            
                else:
                     time.sleep(random.randint(1,5))
                     print("ignored video")
                downbutton.click()
        
        else:
            print("ur not logged in")
            
            
        
        
    
    def wait(self,sleep):
        time.sleep(sleep)
        
        

        
    #currently not working
    def upload(self,files):
        if self.islogedIn:
            self.driver.get(tiktokbot.uploadVariables["upload_link"])
            time.sleep(3)
            self.driver.implicitly_wait(10) 
            
            username = "C:\\Users\\user\\Downloads\\video old\\stuff.mp4"
            self.driver.execute_script("document.querySelector('.jsx-2751257330').style.display='block'")
            time.sleep(3)
            self.driver.implicitly_wait(10) 
            

            
            button = self.driver.find_element("xpath",'//*[@id="root"]/div/div/div/div/div/div/div/div/div[5]')
            button.click()
            time.sleep(3)
            self.driver.implicitly_wait(2)
            self.keyboard.press(Key.enter)
            self.keyboard.release(Key.enter)
            self.keyboard.type("C:\\Users\\user\\Downloads\\video old\\stuff.mp4")
            self.keyboard.press(Key.enter)
            self.keyboard.release(Key.enter)
            self.driver.implicitly_wait(10)
            
            
        else:
            print("not logged in")
    def quit(self):
        self.driver.quit()
     




bot = tiktokbot(email=open("logindetails/email.txt", 'r').read(),password=open("logindetails/password.txt", 'r').read(), profile="Default", directory="C:/Users/user/AppData/Local/Google/Chrome/User Data")
bot.login()

files ={
    'r.mp4': "hello there"
}
                                               
bot.autoscroll(150,True)

#bot.autoscroll(50,True)
#https://stackoverflow.com/questions/52394408/how-to-use-chrome-profile-in-selenium-webdriver-python-3C:\Users\user\Downloads\video old\stuff.mp4

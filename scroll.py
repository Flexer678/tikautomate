from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time




def autoscroll(scrolls):
    driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   options=webdriver.FirefoxOptions()
)
    #driver.get("https://www.tiktok.com/login/")
    driver.get("https://www.tiktok.com/@angel_movie612/video/7261607929554406699")
    print("login")
    time.sleep(10)
    for x in range (scrolls):
        
        downBtn = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[4]/button[2]')
        videoDuration = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[6]/div[2]/div[1]/div[2]')
    print(videoDuration)
    driver.quit()
    print("bot quited")
    
#autoscroll(5)
import webbot
from webbot import Browser
web = Browser()
web.go_to('google.com') 
web.type('hello its me')  # or web.press(web.Key.SHIFT + 'hello its me')
web.press(web.Key.ENTER)
web.go_back()
web.click('Sign in')
web.type('mymail@gmail.com' , into='Email')
web.click('NEXT' , tag='span')
web.type('mypassword' , into='Password' , id='passwordFieldId')
web.click('NEXT' , tag='span') #

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GoogleSearch:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def search(self, query):
        self.driver.get("https://www.google.com")
        search_input = self.driver.find_element_by_name("q")
        search_input.clear()
        search_input.send_keys(query)
        search_input.send_keys(Keys.RETURN)

    def close(self):
        self.driver.quit()

# Create an instance of GoogleSearch class
google = GoogleSearch()

# Perform a search
google.search("OpenAI")

# Close the browser
google.close()
'''
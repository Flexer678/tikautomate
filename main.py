
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
import time



class tiktokbot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.options = webdriver.chromeOptions()
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        #options.add_argument('--profile-directory=Profile 2')
        self.driver = uc.Chrome(options=self.options)
    
    def getBot(self):
        return self.driver
    
    def login(self):
        print("login in")
        self.driver.get("https://accounts.google.com/v3/signin/identifier?opparams=%253Fplatform%253Dgoogle&dsh=S520410844%3A1692040509770177&client_id=1096011445005-sdea0nf5jvj14eia93icpttv27cidkvk.apps.googleusercontent.com&o2v=2&prompt=consent&redirect_uri=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F&response_type=token&scope=openid+profile&service=lso&state=%7B%22client_id%22%3A%221096011445005-sdea0nf5jvj14eia93icpttv27cidkvk.apps.googleusercontent.com%22%2C%22network%22%3A%22google%22%2C%22display%22%3A%22popup%22%2C%22callback%22%3A%22_hellojs_7wmuh48e%22%2C%22state%22%3A%22%22%2C%22redirect_uri%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%22%2C%22scope%22%3A%22basic%22%7D&flowName=GeneralOAuthFlow&continue=https%3A%2F%2Faccounts.google.com%2Fsignin%2Foauth%2Fconsent%3Fauthuser%3Dunknown%26part%3DAJi8hANO6MgoGH9GgEKE_1rukh9A_9hBBOJNoAyXpoFkkYER4eamiOBoZqboMbdBZESGR6kmQVpCvaK_mDbKiN6RmxrJ7iV94ptPoSabj16hTdCjZuP6PzJ2aJPJiw9Ia5CXK85Rp4Vfeq9izU2BfxCupy6u3IVnmZBpI9trkvxxm8os32vet6PFwPMYeBPOxyI_Eo4TXQXyf3uKyG6EjPqMlBFjGkLaLaEiajL6k4e7WLMB0BWhWsavKmU6TvSm4dsAPWoQ7zorV6vsZ39DDSZLZrvRSLlCco0dKyEXi834I_-staJVA3_mwXT1ITvydxfavWQoIXwjSwxfDMqNwJEDwkS-nW49oM1V0_KsuX4xkwK2h63M-Q07cAUtNOZ9jIHVqD-zrKyEyf23wZS6eCDe2S4YPKSJq4SPd6i4lZkENGAzgFsXcDyF-N2d3MVeqsbEDpwgGPrzvjxdV88Ea44kTdYOCkrYmQ%26as%3DS520410844%253A1692040509770177%26client_id%3D1096011445005-sdea0nf5jvj14eia93icpttv27cidkvk.apps.googleusercontent.com%23&app_domain=https%3A%2F%2Fwww.tiktok.com&rart=ANgoxcd5-uqrVm8_k2SFvblraN8_1sjPbuE_fn4BTQVlRv20_emi8titRLGovNgbPkvkzIM5e5y-lvB0KxlG9eACZJPRNUNpFw")
        try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, variables[1])))
                fieldForm = driver.find_element("xpath", variables[1])
        except:
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
                driver.quit()
        finally:
                button = driver.find_element("xpath", variables[3])
                button.click()
   



    def autoscroll(self,times):
    
        #initial webaddress
        ##self.driver.get('https://www.tiktok.com/login/phone-or-email/email')
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(
            '-').key_up(Keys.CONTROL).perform()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(
            '-').key_up(Keys.CONTROL).perform()
        time.sleep(50)

        #self.driver.find_element(By.XPATH, '//*[@id="one-column-item-9"]/canvas').click()
        
        for x in range(times):
            #waits for the browser to load
            self.driver.implicitly_wait(2)
            number = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div[1]/div[3]/div[2]/div[2]').get_attribute("innerText")
            downbutton = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div[1]/button[3]')
            mutebutton = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div/div[1]/div[4]/button')
            
            sleep_duration = str(number[number.find("/")+1: len(number)])

            
            get_time = (int(sleep_duration[0:2])*60) + int(sleep_duration[3:len(sleep_duration)])
            print(get_time, "seconds till scroll")
            #self.driver.implicitly_wait(get_time +1)
            time.sleep(get_time)
            downbutton.click()
        





        
    
        
    
    
    def scroll(scroll_time):
        print(scroll_time)
        
    
    #driver.quit()
tik = tiktokself.driver(open("logindetails/email.txt", "r"), open("logindetails/password.txt", "r"))
print(open("logindetails/email.txt").readline())
tik.login()
#https://www.bing.com/videos/search?q=webself.driver+python&&view=detail&mid=C79C8823961567DA386FC79C8823961567DA386F&&FORM=VRDGAR&ru=%2Fvideos%2Fsearch%3Fq%3Dwebself.driver%2520python%26qs%3Dn%26form%3DQBVR%26%3D%2525eManage%2520Your%2520Search%2520History%2525E%26sp%3D-1%26lq%3D0%26pq%3Dwebself.driver%2520pytho%26sc%3D3-12%26sk%3D%26cvid%3D9060DC11ABC74FCEA58F63BE4B74A5AF%26ghsh%3D0%26ghacc%3D0%26ghpl%3D
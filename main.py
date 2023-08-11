import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class tiktokBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.driver = webdriver.Firefox()
    
        
    
    
    def scroll(scroll_time):
        print(scroll_time)
        


#https://www.bing.com/videos/search?q=webbot+python&&view=detail&mid=C79C8823961567DA386FC79C8823961567DA386F&&FORM=VRDGAR&ru=%2Fvideos%2Fsearch%3Fq%3Dwebbot%2520python%26qs%3Dn%26form%3DQBVR%26%3D%2525eManage%2520Your%2520Search%2520History%2525E%26sp%3D-1%26lq%3D0%26pq%3Dwebbot%2520pytho%26sc%3D3-12%26sk%3D%26cvid%3D9060DC11ABC74FCEA58F63BE4B74A5AF%26ghsh%3D0%26ghacc%3D0%26ghpl%3D
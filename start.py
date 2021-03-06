print("""
   _____                                  
  / ____|                                 
 | |     _ __ __ ___  __  _ __  _ __ ___  
 | |    | '__/ _` \ \/ / | '_ \| '__/ _ \   Facebook : fb.com/nayfercs
 | |____| | | (_| |>  < _| |_) | | | (_) |  Telegram : @nayfercrax
  \_____|_|  \__,_/_/\_(_) .__/|_|  \___/   Website : crax.pro
                         | |                Our group : fb.com/groups/groupe.officiel.by.matry/
                         |_|              
                       
                                        Coded by Nayfer
                                        PS: You can run it more than 5+ times and talk to 5 supports at the same time ! 
                                        GL & HF
""")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
email = input('Netflix valid email : ')
print('Starting after 5 seconds  !')
time.sleep(5)
PATH = 'chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://help.netflix.com/en/")
driver.find_element_by_xpath('//*[@id="startChatTrigger"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="selfHelpPopover"]/div[2]/ul[2]/li/a').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="selfHelpDetailsPopover"]/div/div[2]/textarea').send_keys('Hello i want to change my password please ! i got issue when i click on reset password even i cleared my cookies with your clearing system netflix/clearcookies , and i got the same probelm i wanna reset my password if u could help me please asap and thanks !')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="selfHelpDetailsPopover"]/div/button').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="start-chat-popover"]/div/button').click()
print('restarting in 7 seconds , dont close the BOT ')
time.sleep(7)
driver.get("https://help.netflix.com/chatbox?locale=en&country=TN&cell=&stickyLocale=false&chatSessionId=-&enablePopout=true")
sourrce=driver.page_source
ok=0
while 'You are now chatting with' not in sourrce:
  if ok==0 :
   print('waiting for The Netflix Support')
   ok+=1
  sourrce=driver.page_source
if 'You are now chatting with' in sourrce:
 print('Here we go !')

print('Sending the message after 6 seconds ! ')
time.sleep(6)
driver.find_element_by_xpath('//*[@id="cse-chat-input"]').send_keys('Hello, here is my email if you could send me the reset link  : '+email)
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div[3]/div[3]/ul/li[2]/button').click()
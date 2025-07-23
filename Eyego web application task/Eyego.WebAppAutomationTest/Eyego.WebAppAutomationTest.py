import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #inisiate the chrome driver
driver.get("https://todomvc.com/examples/react/dist/#/") #opens the web application
time.sleep(2)

def add_todo(Buy_Milk): #first method,creats a task 
    input_bar = driver.find_element(By.XPATH, '//*[@id="todo-input"]')
    input_bar.send_keys(Buy_Milk)
    input_bar.send_keys(Keys.ENTER)
    time.sleep(2)
   

def mark_completed(): #second method,marks the task as completed
    check_box = driver.find_element(By.XPATH, '//*[@id="root"]/main/ul/li/div/input')
    check_box.click()
    time.sleep(3)

def delete_item(): #third method,delets the task
    clear_item = driver.find_element(By.XPATH,'//*[@id="root"]/footer/button')
    clear_item.click()
    time.sleep(3)

#calling all the three methods
add_todo("Buy Milk")
mark_completed()
delete_item()
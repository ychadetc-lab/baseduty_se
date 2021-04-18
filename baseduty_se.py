from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as t
import re
# Import package

def send_mes():
    print("searching...")
    x = "https://www.google.com/"
    
    mes = toSearch
    
    options = webdriver.ChromeOptions()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    browser.get(x)
    search = browser.find_element_by_name("q")
    t.sleep(3)
    search.send_keys(mes)
    t.sleep(3)
    search.send_keys(Keys.ENTER)
    t.sleep(5)
    search = browser.find_element_by_css_selector("span.aCOpRe")
    res = search.text
    print(res)
    t.sleep(5)
    


    print("sending message...")
    '''
    options = webdriver.ChromeOptions()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    '''
    browser.get('https://m.facebook.com/')
    search = browser.find_element_by_id("m_login_email")
    search.send_keys("")
    t.sleep(2)
    search = browser.find_element_by_id("m_login_password")
    search.send_keys("")
    t.sleep(2)
    search = browser.find_element_by_name("login").click()
    t.sleep(5)
    browser.get("")
    t.sleep(5)
    search = browser.find_element_by_id("composerInput")
    t.sleep(5)
    search.send_keys("qoobee_server:"+" "+res)
    t.sleep(5)
    search = browser.find_element_by_name("send").click()
    t.sleep(5)
    print("message has been sent!")
    
    browser.quit()
    retreive_message()

def retreive_message():

 while True:
        f1 = open("cache.txt", "r")
        cache = f1.read()
        f1.close()
       
        print("retreiving message...")
        message_id = ''
        options = webdriver.ChromeOptions()
        options.headless = True
        browser = webdriver.Chrome(options=options)

        browser.get('https://m.facebook.com/')
        search = browser.find_element_by_id("m_login_email")
        search.send_keys("")
        t.sleep(2)
        search = browser.find_element_by_id("m_login_password")
        search.send_keys("")
        t.sleep(2)
        search = browser.find_element_by_name("login").click()
        t.sleep(3)
        browser.get(message_id)
        t.sleep(3)


        search = browser.find_elements_by_class_name("_34ej")
        
        lst = []
        for searches in search:
            message_data = searches.text
            try:
               
                lst.append(message_data)
            except UnicodeEncodeError:
                continue

        global toSearch

       
        last_message = lst[-1]
        print(last_message)
        toSearch = str(last_message)
       
        
        #
        
        string = toSearch
        string1 = re.search("^qoobee_server:", string)


        if string1:
            print("cache has the past search please search another data")
            t.sleep(3)
            browser.quit()
            continue
        elif string != cache:
            f = open("cache.txt", "w")
            f.write(toSearch)
            f.close()
            
            send_mes()

        
retreive_message()           
        

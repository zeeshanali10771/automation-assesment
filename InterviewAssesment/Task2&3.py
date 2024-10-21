import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def task2():
    driver.maximize_window()                                # to maximize the window
    driver.get('https://staging.zoneomics.com/')            # to open the website
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/nav[2]/a[1]').click()   # to click the login button.
    time.sleep(2)
    driver.find_element(By.XPATH, '//input[@type="email"]').send_keys('saqlain.altaf@zoneomics.com')   # add email in text box
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/div/div/form/div[1]/div[2]/div/input').send_keys('saqlainaltaf') # add password in text box
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")   # scroll down the page
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()   # click on login button
    time.sleep(8)
    displaytext = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[2]/div[2]/div/div[1]/h1')  # get the text of dashboard
    print(displaytext.text)     # print the text which we verifiy that i am on dashboard page
    # compare the text of the dashboard page.
    if displaytext.is_displayed():
        print('Login to Dashboard is Successful')
    else:
        print("not present")

    time.sleep(5)

def task3():
    # ----------- Part A ----------------
    searchtext = driver.find_element(By.XPATH, '//input[@name="dashboard-header-search"]')   # get the searchbar by xpath
    searchtext.send_keys('222 East 41 Street New York USA')          # add the address through sendkeys
    time.sleep(2)
    enteredtext = searchtext.get_attribute('value')                  # get the entered text throught get attribute by value
    time.sleep(2)
    print(enteredtext)       # display the entered text
    time.sleep(2)
    driver.execute_script("arguments[0].value = '';", searchtext)   # to clear the text in search bar
    time.sleep(5)

    # ------------- Part B ----------------
    text1 = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[1]/h3').text    # to get the text of the tab, of request purchase
    print(text1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")   # to scroll down the page
    time.sleep(2)
    see_more_button = driver.find_element(By.CSS_SELECTOR,'span[tabindex="0"]')   # to click the see more text by using css selector
    time.sleep(5)
    see_more_button.click()    # click on see more button
    time.sleep(9)
    table = driver.find_element(By.TAG_NAME,'tbody')     # get the table element through css selector
    rows = table.find_elements(By.TAG_NAME, "tr")        # get the tag name of the table row

    number_of_records = len(rows)                   # no of rows in the table expect the table header
    print("Number of records in the table:",number_of_records)    # print the total no of rows

if __name__ == '__main__':
    task2()
    task3()

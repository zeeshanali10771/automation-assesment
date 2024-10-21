import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def task7():
    driver.maximize_window()                                         # to maximize the window
    driver.get("https://www.digitaltallycounter.com/")               # to open the tally counter website
    driver.execute_script("document.body.style.zoom='0.8'")          # to minimize the screen so that elements should be visible on same frame.
    increment_button = driver.find_element(By.XPATH,'//*[@id="button-plus"]')      # getting the Xpth of increment button

    # to click the button 100 time for the tally increment.
    for i in range(100):
        increment_button.click()              # to click on the increment button
        time.sleep(1)                         # for small delay to view the increment

    current_count = driver.find_element(By.XPATH,'//*[@id="current-count"]')         # getting the counter text by xpath
    counter_value = current_count.text                     # getting the text that is displayed.

    # to compare the text that is 100 or not.
    if counter_value =='100':
        print("the value is 100")
    else:
        print("the value is not 100")

    time.sleep(5)

if __name__ == '__main__':
    task7()
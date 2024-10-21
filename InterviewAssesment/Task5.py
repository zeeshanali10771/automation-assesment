import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def task5():
    driver.maximize_window()                                  # to maximize the window
    driver.get('https://demo.automationtesting.in/Alerts.html')  # to open the alert website

    click_button = driver.find_element(By.XPATH,'//*[@id="OKTab"]/button')    # to click the button by using the xpath
    click_button.click()            # to click the button
    time.sleep(3)

    switch = driver.switch_to.alert    # now, switch the driver to alert popup message
    switch.accept()                    # to click Ok button, as to accepet the popup message.

    time.sleep(5)

if __name__ == '__main__':
    task5()
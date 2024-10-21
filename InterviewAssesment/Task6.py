import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def task6():
    driver.maximize_window()                          # to maximize the window
    driver.get('https://demoqa.com/upload-download')  # to open the demoQA website

    upload_button = driver.find_element(By.ID,'uploadFile')  # to get the upload button by id
    upload_button.send_keys('C:\\Users\\Rana Zeeshan Ali\\Downloads\\sampleFile.jpeg') # send the path of file in the upload button.

    time.sleep(5)

if __name__ == '__main__':
    task6()
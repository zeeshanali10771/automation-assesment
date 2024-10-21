import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def task4():
    driver.maximize_window()                         # to maximize the window
    driver.get('https://www.globalsqa.com/demo-site/select-dropdown-menu/')  # to open the website of globalsqa
    time.sleep(3)

    dropdown_element = driver.find_element(By.TAG_NAME, "select")     # to find the dropdown by using tagname
    dropdown = Select(dropdown_element)                # to select the country from dropdown
    dropdown.select_by_visible_text('Pakistan')        # select the country by visible text
    time.sleep(3)
    appeared_text = dropdown.first_selected_option.text   # to get the country that is appeared in dropdown

    # compare the country name is it Pakistan or not.
    if appeared_text == "Pakistan":
        print("The country name is Pakistan")
    else:
        print("The country is not Pakistan")

    time.sleep(3)

if __name__ == '__main__':
    task4()
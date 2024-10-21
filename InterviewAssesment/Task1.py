from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def task1():
    driver.maximize_window()           # to maximize the window
    driver.get('https://staging.zoneomics.com')   # to open the webiste of zoneomics
    global title
    title = driver.title                   # to get the title of the webiste
    print('Title:', title)                 # now to print the website title.

def splitTitle(title):                     # split Tilte fuction, to split the title
    charachter = [char for char in title]
    print('List of Caracters:', charachter)

    if 'Zoneomics' in title and len (charachter) >= 51:    # to verify that zoneomics is present in title & length is 51 or not.
        print("Verified")
    else:
        print('Verification Failed')

if __name__ == '__main__':
    task1()
    splitTitle(title)
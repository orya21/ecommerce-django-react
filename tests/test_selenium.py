from selenium import webdriver
#pip install selenium
#pip install webdriver-manager
#for testing -
#from time import sleep
import sys
sys.stdout.reconfigure(encoding='utf8')
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chrome_service
from selenium.webdriver.firefox.service import Service as ff_service
from selenium.webdriver.common.by import By
#1.
chrome_driver_path=ChromeDriverManager().install()
chrome_driver_service=chrome_service(chrome_driver_path)
chrome_driver=webdriver.Chrome(service=chrome_driver_service)

def test_title():
    # Start the WebDriver (in this example, we'll use Chrome)
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Open the homepage of your Django application
        driver.get("http://ecommerce-django-react.herokuapp.com")  
      
      # Verify the title of the page
        expected_title = "Your Expected Title"  
        assert expected_title in driver.title

    finally:
        # Close the WebDriver session
        driver.quit()


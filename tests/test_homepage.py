from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_homepage():
    # Start the WebDriver (in this example, we'll use Chrome)
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Open the homepage of your Django application
        driver.get("http://ecommerce-django-react.herokuapp.com)  
                   
        # Find elements on the homepage and interact with them
        # Example: Click on a link
        driver.find_element_by_link_text("About").click()

        # Example: Fill out a form
        input_element = driver.find_element_by_name("search")  # Assuming there's a search input field
        input_element.send_keys("Test search query")  # Enter a search query
        input_element.send_keys(Keys.ENTER)  # Submit the form by pressing Enter

        # Wait for the page to load (if applicable)
        # Example: WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-results")))

        # Make assertions about the state of the page
        assert "About" in driver.title  # Check if the page title contains "About"

    finally:
        # Close the WebDriver session
        driver.quit()

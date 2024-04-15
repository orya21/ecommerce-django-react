from selenium import webdriver

def test_homepage_title():
    # Start the WebDriver (in this example, we'll use Chrome)
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Open the homepage of your Django application
        driver.get("http://ecommerce-django-react.herokuapp.com")  # Fixed the URL

        # Check if the page title is correct
        assert "Ecommerce Django React" in driver.title

    finally:
        # Close the WebDriver session
        driver.quit()

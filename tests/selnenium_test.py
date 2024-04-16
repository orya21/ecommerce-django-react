from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# פתיחת דפדפן חדש
driver = webdriver.Chrome()

# פתיחת אתר
driver.get("https://orya21.github.io/ecommerce-django-react/")

# בדיקת כותרת הדף
assert "E-commerce" in driver.title

# מציגה את כל הלינקים בדף הבית
links = driver.find_elements_by_tag_name('a')
print("All links on the page:")
for link in links:
    print(link.get_attribute('href'))

# מציגה את רשימת המוצרים בדף הבית
products = driver.find_elements_by_class_name('product')
print("\nProducts on the page:")
for product in products:
    print(product.text)

# מציגה את הקטגוריות בתפריט
categories = driver.find_elements_by_class_name('dropdown-menu')
print("\nCategories in the menu:")
for category in categories:
    print(category.text)

# סגירת הדפדפן
driver.close()

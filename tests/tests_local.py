# Imports the important libraries we are using
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Creates a variable "options" with the Options() class attributes
options = Options()
# Sets the headless (Starts a window without ever opening the browser) option to True
options.headless = True

# Variable with PATH and the headless option that later starts a chrome window
driver = webdriver.Chrome(chrome_options=options)

# Locates the parent directory of tests aka "frisorhemsida"
parentPath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

# Where we want to go from the parent directory => index
desiredPath = "\\public\\index.html"

# Loads in the website
driver.get(parentPath+desiredPath)

# Variable which will look for the specified text ("//*[contains(text(), 'Desired text here')]")
element = driver.find_element_by_xpath("//*[contains(text(), 'Öppettider')]")

# Prints out the element that wasn't found on the website
print(element) 
# If all elements are present the code is excellent
print("Code is working excellent")

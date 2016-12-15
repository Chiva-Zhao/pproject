from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path="D:\\phantomjs211\\bin\\phantomjs.exe")
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
try:
    ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loadedButton")))
finally:
    print(driver.find_element_by_id("content").text)
    driver.close()

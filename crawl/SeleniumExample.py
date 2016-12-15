from selenium import webdriver
import time
driver = webdriver.PhantomJS(executable_path="D:\\phantomjs211\\bin\\phantomjs.exe")
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(1)
print(driver.find_element_by_id("content").text)
driver.close()
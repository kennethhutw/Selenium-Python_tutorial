from selenium import webdriver

url="C:\\Programs\\Python36\\BrowersDriver\\chromedriver.exe"
driver=webdriver.Chrome(url)

driver.get("http://www.google.com")

# print current url
print(driver.current_url)
# print current page title
print(driver.title)

# go to Yahoo page
driver.get("http://www.yahoo.com")

# print current url
print(driver.current_url)
# print current page title
print(driver.title)

# go back previous page
driver.back()

# print current url
print(driver.current_url)
# print current page title
print(driver.title)

# loads the next URL in the history list as same as  window.history.forward() method.
driver.forward()

# print current url
print(driver.current_url)
# print current page title
print(driver.title)

# refresh current page
driver.refresh()

# Close the browser window that the driver has focus of
driver.close()
# Call Dispose() => Release all resource.
driver.quit()
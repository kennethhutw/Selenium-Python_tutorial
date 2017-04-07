from selenium import webdriver

url="C:\\Programs\\Python36\\BrowersDriver\\chromedriver.exe"
driver=webdriver.Chrome(url)

driver.get("http://www.google.com")

# print current url
print(driver.current_url)
# print current page title
print(driver.title)

# Close the browser window that the driver has focus of
driver.close()
# Call Dispose() => Release all resource.
driver.quit()
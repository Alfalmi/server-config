from selenium import webdriver

options = webdriver.ChromeOptions()
driver = webdriver.Remote(
    command_executor='ssh -i "TESTSERVER.pem" ubuntu@ec2-18-191-29-44.us-east-2.compute.amazonaws.com',
    options=options
)
driver.get("http://www.google.com")
driver.quit()

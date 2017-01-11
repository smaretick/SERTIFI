from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {'browser': 'chrome', 'build': 'GA buildSAT1', 'browserstack.debug': 'true' }

driver = webdriver.Remote(
                          command_executor='http://scottmaretick2:MDKicy4nya2192zewKpz@hub.browserstack.com:80/wd/hub',
                          desired_capabilities=desired_cap)

#driver.get("http://www.google.com")
#driver.get("https://analytics.google.com/analytics/web/#home/a39099721w75626535p78130152/")
driver.get("https://www.google.com/analytics/#?modal_active=none/analytics/#?modal_active=none")
    #if not "Google" in driver.title:
#raise Exception("Unable to load google page!")
#elem = driver.find_element_by_name("q")
#elem.send_keys("BrowserStack")
#elem.submit()
print driver.title

driver.find_element_by_link_text("Sign in").click()
driver.find_element_by_link_text("Analytics").click()
driver.find_element_by_id("Passwd").clear()
driver.find_element_by_id("Passwd").send_keys("sm110751")
driver.find_element_by_id("account-chooser-link").click()
driver.find_element_by_id("choose-account-0").click()
driver.find_element_by_id("Passwd").clear()
driver.find_element_by_id("Passwd").send_keys("sm110751")
driver.find_element_by_id("signIn").click()


#driver.find_element_by_id("Email").clear();
#driver.find_element_by_id("Email").send_keys("scottmaretick51@gmail.com");
#driver.find_element_by_id("next").click();
#driver.find_element_by_id("Passwd").clear();
#driver.find_element_by_id("Passwd").send_keys("sm110751");
#driver.find_element_by_id("signIn").click();
print driver.title

driver.quit()

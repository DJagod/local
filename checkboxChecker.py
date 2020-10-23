from time import sleep
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
    "E:\ZiyaTest\pythonLessons\chromedriver.exe"
)

# driver.maximize_window()
driver.get("https://zyia.develop/distributor")

adv_btn : WebElement = driver.find_element_by_id("details-button")
adv_btn.click()

prcd_btn: WebElement = driver.find_element_by_id("proceed-link")
prcd_btn.click()

agrmnts_chckbx: WebElement = driver.find_element_by_id("MasterContentBody1_chk_agreements")
agrmnts_chckbx.click()

sleep(1)

representative: WebElement = driver.find_element_by_id("MasterContentBody1_txt_username")
password: WebElement = driver.find_element_by_id("MasterContentBody1_txt_password")
login_btn: WebElement = driver.find_element_by_id ("MasterContentBody1_btnLogin")

representative.send_keys("16000")
password.send_keys("1q2w3e4r")
login_btn.click()


if login_btn.is_enabled():
    print("Test Failed")
else:
    print("Test Passed")

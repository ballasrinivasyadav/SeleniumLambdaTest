
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:

    def __init__(self, driver):
        self.driver = driver

                                    # Scenario1

    demo = (By.XPATH, "//a[normalize-space()='Simple Form Demo']")
    enterMessage = (By.XPATH, "//input[@id='user-message']")

    def getDemo(self):
        return self.driver.find_element(*HomePage.demo)

    def setenter(self):
        return self.driver.find_element(*HomePage.enterMessage)

    def getOneScreenShot(self):
        return self.driver.save_screenshot("First.png")

                                    # Scenario 3

    form = (By.XPATH, "//a[normalize-space()='Input Form Submit']")
    name = (By.ID, "name")
    email = (By.ID, "inputEmail4")
    password = (By.ID, "inputPassword4")
    company = (By.ID, "company")
    website = (By.ID, "websitename")
    country = (By.XPATH, "//select[@name='country']")
    city = (By.ID, "inputCity")
    address1 = (By.CSS_SELECTOR, "#inputAddress1")
    address2 = (By.CSS_SELECTOR, "#inputAddress2")
    state = (By.ID, "inputState")
    pincode = (By.CSS_SELECTOR, "#inputZip")

    def getInputform(self):
        return self.driver.find_element(*HomePage.form)

    def getName(self):
        return self.driver.find_element(*HomePage.name).send_keys("Srinivas")

    def getEmail(self):
        return self.driver.find_element(*HomePage.email).send_keys("Srinivasballa07@gmail.com")

    def getPassword(self):
        return self.driver.find_element(*HomePage.password).send_keys("Srinivasballa07")

    def getCompany(self):
        return self.driver.find_element(*HomePage.company).send_keys("Srinivasballa.com")

    def getWebsite(self):
        return self.driver.find_element(*HomePage.website).send_keys("Srinivas.com")

    def getCountry(self):
        sel = Select(self.driver.find_element(*HomePage.country))
        sel.select_by_visible_text("United States")

    def getCity(self):
        return self.driver.find_element(*HomePage.city).send_keys("Hyderabad")

    def getAddressOne(self):
        return self.driver.find_element(*HomePage.address1).send_keys("Hyderabad")

    def getAddressTwo(self):
        return self.driver.find_element(*HomePage.address2).send_keys("Hyderabad")

    def getState(self):
        return self.driver.find_element(*HomePage.state).send_keys("Telangana")

    def getPincode(self):
        return self.driver.find_element(*HomePage.pincode).send_keys("500012")

    def getThreeScreenShot(self):
        return self.driver.save_screenshot("Three.png")

    def getSuccess(self):
        success = self.driver.find_element(By.XPATH, "//p[@class='success-msg hidden']").text
        assert "Thanks for contacting us, we will get back to you shortly" in success
        print(success)



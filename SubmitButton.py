
                                        #Scenario 3

from selenium.webdriver.common.by import By

class SubmitButton:

    def __init__(self, driver):
        self.driver = driver

    submit = (By.XPATH, "//button[normalize-space()='Submit']")
    name = (By.ID,"name")

    def getSubmit(self):
        return self.driver.find_element(*SubmitButton.submit)

    def getFillout(self):

        result = self.driver.find_element(*SubmitButton.name)
        res = result.get_attribute("validationMessage")
        assert "Please fill out this field." in res
        print(res)

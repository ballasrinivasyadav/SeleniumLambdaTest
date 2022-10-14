
                                            # Scenario 1

from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    checkout = (By.ID, "showInput")
    textMessage = (By.XPATH, "//p[@id='message']")

    def getcheckoutpage(self):
        return self.driver.find_element(*CheckoutPage.checkout)

    def getmessage(self):
        return self.driver.find_element(*CheckoutPage.textMessage).text

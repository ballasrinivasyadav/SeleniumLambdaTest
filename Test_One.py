                                        #  Scenario 1
import pytest
from CheckoutPage import CheckoutPage
from HomePage import HomePage

@pytest.mark.usefixtures
class TestOne:
    def testone(self, setup):
        #HomePage
        simpleform = HomePage(self.driver)
        simpleform.getDemo().click()

        #HomePage
        simpleform.setenter().send_keys("Welcome Lambda Test")

        #CheckoutPage
        check = CheckoutPage(self.driver)
        check.getcheckoutpage().click()

        # Get ScreenShot
        simpleform.getOneScreenShot()

        message = check.getmessage()
        assert ("Welcome Lambda Test" in message)
        print(message)



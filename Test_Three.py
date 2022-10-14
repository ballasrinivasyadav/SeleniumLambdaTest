
                                            #Scenario 3
import pytest
from HomePage import HomePage
from SubmitButton import SubmitButton


@pytest.mark.usefixture
class TestThree:

    def testthree(self, setup):

        home = HomePage(self.driver)
        home.getInputform().click()

        submitbutton = SubmitButton(self.driver)
        submitbutton.getSubmit().click()
        # time.sleep(1)
        submitbutton.getFillout()

        # time.sleep(1)
        home.getName()

        home.getEmail()

        home.getPassword()

        home.getCompany()

        home.getWebsite()

        # time.sleep(1)
        home.getCountry()

        home.getCity()

        home.getAddressOne()

        home.getAddressTwo()

        home.getState()

        home.getPincode()

        submitbutton.getSubmit().click()

        home.getSuccess()




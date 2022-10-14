
                                # Scenario 2

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class DragDrop:

    def __init__(self, driver):
        self.driver = driver

    dragdrop = (By.XPATH, "//a[normalize-space()='Drag & Drop Sliders']")
    slid = (By.XPATH, '//input[@value=15]')

    def getDragDrop(self):
        self.driver.find_element(*DragDrop.dragdrop).click()

    def getSlider(self):
        slider = self.driver.find_element(*DragDrop.slid)
        ActionChains(self.driver).drag_and_drop_by_offset(slider, 105, 0).perform()

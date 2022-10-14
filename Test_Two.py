                                       #Scenario 2
import pytest
from dragDrop import DragDrop

@pytest.mark.usefixtures
class TestTwo:

    def test_two(self, setup):

        # Drag&Drop
        dragDrop = DragDrop(self.driver)
        dragDrop.getDragDrop()

        # Drag&Drop Slider
        dragDrop.getSlider()



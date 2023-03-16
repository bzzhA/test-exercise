from pom.pages.main_page import MainPage
from pom.pages.elements_page import ElementsPage
class TestDemoQA:
    def test_elements_page(self, driver_factory):
        main_page = MainPage(driver_factory)
        main_page.open()
        main_page.click_elements()

    def test_checkbox_page(self, driver_factory):
        elements_page = ElementsPage(driver_factory)
        elements_page.check_box_click()
        elements_page.home_toggle_click()
        elements_page.downloads_toggle_click()
        elements_page.word_file_select()
        assert elements_page.get_text_file() == 'wordFile', "Text doesn't match"


from base.base import Base
from pom.locators.elements_page_locators import ElementsPageLocators


class ElementsPage(Base):
    elements_page_locators = ElementsPageLocators

    def check_box_click(self):
        self.element_is_visible(self.elements_page_locators.CHECK_BOX).click()

    def home_toggle_click(self):
        self.element_is_visible(self.elements_page_locators.TOGGLE_HOME).click()

    def downloads_toggle_click(self):
        self.element_is_visible(self.elements_page_locators.TOGGLE_DOWNLOADS).click()

    def word_file_select(self):
        self.element_is_visible(self.elements_page_locators.WORD_FILE_CHECKBOX).click()

    def get_text_file(self):
        return self.get_text(self.elements_page_locators.CHECK_SELECT_FILE)

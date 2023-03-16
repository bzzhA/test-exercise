from base.base import Base
from pom.locators.main_page_locators import MainPageLocators


class MainPage(Base):
    main_locators = MainPageLocators

    def click_elements(self):
        self.element_is_visible(self.main_locators.ELEMENTS).click()

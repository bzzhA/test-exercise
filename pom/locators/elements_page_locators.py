from selenium.webdriver.common.by import By


class ElementsPageLocators:
    CHECK_BOX = (By.XPATH, "//ul[@class='menu-list']//li[@id='item-1']//span[text()='Check Box']")
    TOGGLE_HOME = (By.XPATH, "//div[@id='tree-node']//ol[1]//li//button")
    TOGGLE_DOWNLOADS = (By.XPATH, "//div[@id='tree-node']//ol//li[3]//button")
    WORD_FILE_CHECKBOX = (By.XPATH, "//div[@id='tree-node']//ol//li[3]//ol//li//label[@for='tree-node-wordFile']//span[1]")
    CHECK_SELECT_FILE = (By.XPATH, "//span[contains(text(), 'wordFile')]")

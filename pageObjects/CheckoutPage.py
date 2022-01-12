from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver=driver
    CardTitle=(By.XPATH, "//div[@class='card h-100']")
    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.CardTitle)
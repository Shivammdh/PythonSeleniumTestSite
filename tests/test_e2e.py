import time
from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homepage=HomePage(self.driver)
        homepage.shopItem().click()
        checkoutpage=CheckOutPage(self.driver)
        cards=checkoutpage.getCardTitles()
        # //div[@class='card h-100']/div/h4/a
        # product =//div[@class='card h-100']
        time.sleep(3)
        log.info("Getting All the card title")
        for product in cards:
            productName = product.find_element(By.XPATH,"div/h4/a").text
            log.info(productName)
            if productName == "Blackberry":
                # Add item into cart
                product.find_element(By.XPATH,"div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        log.info("Entring country IND")
        self.driver.find_element(By.ID, "country").send_keys("ind")
        self.verifywait(By.LINK_TEXT, "India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("Text massege assertion"+successText)
        assert "Success! Thank you!" in successText

        self.driver.get_screenshot_as_file("screen.png")
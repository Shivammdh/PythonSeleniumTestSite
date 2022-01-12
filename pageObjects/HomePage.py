from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver=driver
    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkButton = (By.ID, "exampleCheck1")
    redio = (By.ID, "inlineRadio2")
    gender = (By.ID, "exampleFormControlSelect1")

    def shopItem(self):
        return self.driver.find_element(*HomePage.shop)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPass(self):
        return self.driver.find_element(*HomePage.password)

    def chek(self):
        return self.driver.find_element(*HomePage.checkButton)

    def radioclick(self):
        return self.driver.find_element(*HomePage.redio)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)


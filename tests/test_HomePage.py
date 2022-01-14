import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage=HomePage(self.driver)
        log.info("first Name is "+getData['Name'])
        homepage.getName().send_keys(getData['Name'])
        log.info("Email is " + getData['Email'])
        homepage.getEmail().send_keys(getData['Email'])
        homepage.getPass().send_keys("Shivam@0105")
        homepage.chek().click()
        log.info("Gender is " + getData['Gender'])
        self.selectOptionByText(homepage.getGender(),getData['Gender'])
        homepage.radioclick().click()
        self.driver.find_element(By.CSS_SELECTOR, "input.btn-success").click()
        succes_msg = self.driver.find_element(By.XPATH, "/html/body/app-root/form-comp/div/div[2]/div")
        # print(succes_msg.text)
        # print("×\nSuccess! The Form has been submitted successfully!")
        # assert succes_msg.text=="×\nSuccess! The Form has been submitted successfully!.","fail"
        # or
        assert 'success' in succes_msg.text, 'fail'
        print("pass")
        self.driver.refresh()
        time.sleep(3)

    @pytest.fixture(params=HomePageData.getTestData("Testcase1"))
    def getData(self,request):
        return request.param

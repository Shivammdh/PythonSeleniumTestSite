import inspect

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):

        loggerName=inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        # logger.setLevel(logging.CRITICAL)
        # logger.debug("A debug statement is executed")
        # logger.info("Information statement")
        # logger.debug("A debug statement is executed")
        # logger.warning("Something is in warning mode")
        # logger.error("A Major error has happend")
        # logger.critical("Critical issue")
        logger.setLevel(logging.DEBUG)
        return logger
    def verifywait(self,locator,text):
        self.locator=locator
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((locator,text)))

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
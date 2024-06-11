from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
  """
  The Purpose Of A BasePage Is To Contain Methods Common To All Page Objects
  """
  def __init__(self, driver):
    self.driver = driver

  def find(self, *locator):
    return self.driver.find_element(*locator)

  def click(self, *locator):
    self.find(*locator).click()


  def set(self, locator, value):
    self.find(*locator).clear()
    self.find(*locator).send_keys(value)

  def get_text(self, locator):
    return self.find(*locator).text

  def get_title(self):
    return self.driver.title

  def assert_content_contains(self, locator, value):
    element_text = self.find(*locator).text
    assert value in element_text


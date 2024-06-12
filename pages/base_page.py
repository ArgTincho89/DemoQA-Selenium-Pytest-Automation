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
    return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))

  def click(self, *locator):
    WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator)).click()


  def set(self, locator, value):
    self.find(*locator).clear()
    self.find(*locator).send_keys(value)

  def get_text(self, locator):
    return self.find(*locator).text

  def get_title(self):
    return self.driver.title

  def assert_content_contains(self, locator, *values):
    element_text = self.find(*locator).text
    for value in values:
        assert value in element_text
    
  def assert_text(self, locator, value):
    element_text = self.find(*locator).text
    assert value == element_text

  def assert_element_visibility(self, locator):
    element = self.find(*locator)
    assert element.is_displayed()
    
  def assert_element_not_present(self, locator):
    elements = self.driver.find_elements(*locator)
    assert len(elements) == 0
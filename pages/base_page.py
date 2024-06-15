from selenium.webdriver import ActionChains
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
    self.find(*locator).click()

  def double_click(self, *locator):
    element = self.find(*locator)
    action_chains = ActionChains(self.driver)
    action_chains.double_click(element).perform()

  def right_click(self, *locator):
    element = self.find(*locator)
    action_chains = ActionChains(self.driver)
    action_chains.context_click(element).perform()

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
    
  def upload_file(self, locator, file_path):
    # Method for uploading file using a custom locator
    upload_element = self.find(*locator)
    upload_element.send_keys(file_path)
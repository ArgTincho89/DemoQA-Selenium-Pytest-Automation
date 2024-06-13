import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


from utilities.test_data import TestData


@pytest.fixture(params=["chrome" ,# "firefox", "edge"
                        ])
def initialize_driver(request):
  if request.param == "chrome":
    chrome_options = ChromeOptions()
  #  chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
  #elif request.param == "firefox":
  #  firefox_options = FirefoxOptions()
  #   # firefox_options.add_argument("--headless")
  #   driver = webdriver.Firefox(options=firefox_options)
  #elif request.param == "edge":
  #   edge_options = EdgeOptions()
    # edge_options.add_argument("--headless")
  #   driver = webdriver.Edge(options=edge_options)
  request.cls.driver = driver
  print("Browser: ", request.param)
  driver.get(TestData.url)
  driver.maximize_window()
  yield
  print("Close Driver")
  driver.close()


"""@pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_driver(request):
  if request.param == "chrome":
    driver = webdriver.Chrome()
  elif request.param == "firefox":
    driver = webdriver.Firefox()
  elif request.param == "edge":
    driver = webdriver.Edge()
  request.cls.driver = driver
  print("Browser: ", request.param)
  driver.get(TestData.url)
  driver.maximize_window()
  yield
  print("Close Driver")
  driver.close()"""



from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ElementsPage(BasePage):
    # Text Box element locators
    text_box_section_button = (By.CSS_SELECTOR, "div.element-group:nth-of-type(1) #item-0")
    full_name_field = (By.CSS_SELECTOR, "div#userName-wrapper input")
    email_field = (By.CSS_SELECTOR, "div#userEmail-wrapper input")
    current_address = (By.CSS_SELECTOR, "div#currentAddress-wrapper textarea")
    permanent_address = (By.CSS_SELECTOR, "textarea#permanentAddress")
    text_box_submit_button = (By.ID, "submit")
    registered_name_field = (By.ID, "name")
    registered_email_field = (By.ID, "email")
    registered_current_address_field = (By.CSS_SELECTOR, "p#currentAddress")
    registered_permanent_address_field = (By.CSS_SELECTOR, "p#permanentAddress")
    #Check Box element locators
    check_box_section_button  = (By.CSS_SELECTOR, "div.element-group:nth-of-type(1) #item-1")
    check_box_section_title = (By.CSS_SELECTOR, "h1.text-center")
    
    def __init__(self, driver):
        super().__init__(driver)
        
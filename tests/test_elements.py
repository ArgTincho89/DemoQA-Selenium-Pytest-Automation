import time
from pages import elements_page
from pages.elements_page import ElementsPage
from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.test_data import TestData



class TestElements(BaseTest):
    
    def test_01_Complete_Text_Box_Fields(self):
        """ Accessing to the Text Box section, completing the form and submitting"""
        home_page = HomePage(self.driver)
        # Navigate to Elements page
        elements_link = home_page.find(*home_page.Elements)
        self.driver.execute_script("arguments[0].click();", elements_link)
        # Creation of an Elements Page instance
        elements_page = ElementsPage(self.driver)
        # Navigate to Text Box section
        text_box_section_button = elements_page.find(*elements_page.text_box_section_button)
        text_box_section_button.click() 
        # Complete Full Name Field
        elements_page.set(elements_page.full_name_field, "John Doe")
        # Complete Email Address Field
        elements_page.set(elements_page.email_field, "johndoe@gmail.com")
        # Complete Current Address field
        elements_page.set(elements_page.current_address, "Address 123")
         # Complete Permanent Address field
        elements_page.set(elements_page.permanent_address, "Address 456")
        # Scroll down to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Click Submit button
        submit_button = elements_page.find(*elements_page.text_box_submit_button)
        submit_button.click()
        # Check that the data was correctly submited by asserting the form response
        elements_page.assert_content_contains(elements_page.registered_name_field, "John Doe")
        elements_page.assert_content_contains(elements_page.registered_email_field, "johndoe@gmail.com")
        elements_page.assert_content_contains(elements_page.registered_current_address_field, "Address 123")
        elements_page.assert_content_contains(elements_page.registered_permanent_address_field, "Address 456")
        self.driver.close
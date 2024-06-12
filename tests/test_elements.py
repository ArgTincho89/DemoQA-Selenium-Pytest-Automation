import time
from pages import elements_page
from pages.elements_page import ElementsPage
from pages.home_page import HomePage
from tests.base_test import BaseTest
from utilities.test_data import TestData



class TestElements(BaseTest):
    
    """def test_01_Complete_Text_Box_Fields(self):
        # Accessing to the Text Box section, completing the form, submitting and asserting results
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
        self.driver.close"""
        
    def test_02_check_box_section(self):
        """Interacting with the elements of the check box section"""
        home_page = HomePage(self.driver)
        # Navigate to Elements page
        elements_link = home_page.find(*home_page.Elements)
        self.driver.execute_script("arguments[0].click();", elements_link)
        # Creation of an Elements Page instance
        elements_page = ElementsPage(self.driver)
        # Navigate to check Box section
        check_box_section_button = elements_page.find(*elements_page.check_box_section_button)
        check_box_section_button.click()
        # Asserting that the tittle of the section corresponds to Check Box
        elements_page.assert_text(elements_page.check_box_section_title, "Check Box")
        # Checking that, when clicking the Expand All button, all the elements are displayed
        elements_page.click(*elements_page.button_expand_all)
        elements_page.assert_element_visibility(elements_page.home_check_box)
        elements_page.assert_element_visibility(elements_page.desktop_check_box)
        elements_page.assert_element_visibility(elements_page.desktop_notes_checkbox)
        elements_page.assert_element_visibility(elements_page.desktop_commands_checkbox)
        elements_page.assert_element_visibility(elements_page.documents_check_box)
        elements_page.assert_element_visibility(elements_page.documents_workspace_checkbox)
        elements_page.assert_element_visibility(elements_page.documents_workspace_react_checkbox)
        elements_page.assert_element_visibility(elements_page.documents_workspace_angular_checkbox)
        elements_page.assert_element_visibility(elements_page.documents_workspace_vue_checkbox)
        elements_page.assert_element_visibility(elements_page.documents_office_checkbox)
        elements_page.assert_element_visibility(elements_page.documents_office_public_checkbox)
        elements_page.assert_element_visibility(elements_page.documents_office_private_checkbox)
        elements_page.assert_element_visibility(elements_page.documents_office_classified_checkbox)
        elements_page.assert_element_visibility(elements_page.documents_office_general_checkbox)
        elements_page.assert_element_visibility(elements_page.downloads_check_box)
        elements_page.assert_element_visibility(elements_page.downloads_wordfile_checkbox)
        elements_page.assert_element_visibility(elements_page.downloads_excelfile_checkbox)
        # Checking that when clicking the Collapse All button, all the elements are hidden, except for Home
        elements_page.click(*elements_page.button_collapse_all)
        elements_page.assert_element_visibility(elements_page.home_check_box)
        elements_page.assert_element_not_present(elements_page.desktop_check_box)
        elements_page.assert_element_not_present(elements_page.desktop_notes_checkbox)
        elements_page.assert_element_not_present(elements_page.desktop_commands_checkbox)
        elements_page.assert_element_not_present(elements_page.documents_check_box)
        elements_page.assert_element_not_present(elements_page.documents_workspace_checkbox)
        elements_page.assert_element_not_present(elements_page.documents_workspace_react_checkbox)
        elements_page.assert_element_not_present(elements_page.documents_workspace_angular_checkbox)
        elements_page.assert_element_not_present(elements_page.documents_workspace_vue_checkbox)
        elements_page.assert_element_not_present(elements_page.documents_office_checkbox)
        elements_page.assert_element_not_present(elements_page.documents_office_public_checkbox)
        elements_page.assert_element_not_present(elements_page.documents_office_private_checkbox)
        elements_page.assert_element_not_present(elements_page.documents_office_classified_checkbox)
        elements_page.assert_element_not_present(elements_page.documents_office_general_checkbox)
        elements_page.assert_element_not_present(elements_page.downloads_check_box)
        elements_page.assert_element_not_present(elements_page.downloads_wordfile_checkbox)
        elements_page.assert_element_not_present(elements_page.downloads_excelfile_checkbox)
        # Clicking each check box and asserting that the results correctly displays the adherence
        elements_page.click(*elements_page.home_expand_button)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scrolls down to avoid adds intercepting clicks
        elements_page.click(*elements_page.desktop_check_box)
        elements_page.assert_content_contains(elements_page.check_box_results, "desktop", "notes", "commands")
        elements_page.click(*elements_page.documents_check_box)
        elements_page.assert_content_contains(elements_page.check_box_results, "documents", "workspace", "react",
                                              "angular", "veu", "office", "public", "private", "classified", "general")
        elements_page.click(*elements_page.downloads_check_box)
        elements_page.assert_content_contains(elements_page.check_box_results, "downloads", "wordFile", "excelFile")
        self.driver.close
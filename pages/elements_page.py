
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ElementsPage(BasePage):
    
    # Text Box elements locators
    text_box_section_button = (By.CSS_SELECTOR, "div.element-group:nth-of-type(1) #item-0")
    text_box_section_title = (By.CSS_SELECTOR, "h1.text-center")
    full_name_field = (By.CSS_SELECTOR, "div#userName-wrapper input")
    email_field = (By.CSS_SELECTOR, "div#userEmail-wrapper input")
    current_address = (By.CSS_SELECTOR, "div#currentAddress-wrapper textarea")
    permanent_address = (By.CSS_SELECTOR, "textarea#permanentAddress")
    text_box_submit_button = (By.ID, "submit")
    registered_name_field = (By.ID, "name")
    registered_email_field = (By.ID, "email")
    registered_current_address_field = (By.CSS_SELECTOR, "p#currentAddress")
    registered_permanent_address_field = (By.CSS_SELECTOR, "p#permanentAddress")
    
    # Check Box elements locators
    check_box_section_button  = (By.CSS_SELECTOR, "div.element-group:nth-of-type(1) #item-1")
    check_box_section_title = (By.CSS_SELECTOR, "h1.text-center")
    button_expand_all = (By.CSS_SELECTOR, "button[title='Expand all']")
    button_collapse_all = (By.CSS_SELECTOR, "button[title='Collapse all']")
    home_check_box = (By.CSS_SELECTOR, "#tree-node > ol > li > span > label > span.rct-checkbox > svg")
    desktop_check_box = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(1) > span > label > span.rct-checkbox > svg")
    desktop_notes_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(1) > span > label > span.rct-checkbox")
    desktop_commands_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(2) > span > label > span.rct-checkbox")
    documents_check_box = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > span > label > span.rct-checkbox > svg")
    documents_workspace_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(1) > span > label > span.rct-checkbox")
    documents_workspace_react_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(1) > span > label > span.rct-checkbox > svg")
    documents_workspace_angular_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(2) > span > label > span.rct-checkbox > svg")
    documents_workspace_vue_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(3) > span > label > span.rct-checkbox > svg")
    documents_office_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(2) > span > label > span.rct-checkbox")
    documents_office_public_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(2) > ol > li:nth-child(1) > span > label > span.rct-checkbox > svg")
    documents_office_private_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(2) > ol > li:nth-child(2) > span > label > span.rct-checkbox > svg")
    documents_office_classified_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(2) > ol > li:nth-child(3) > span > label > span.rct-checkbox > svg")
    documents_office_general_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > ol > li:nth-child(2) > ol > li:nth-child(4) > span > label > span.rct-checkbox > svg")
    downloads_check_box = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(3) > span > label > span.rct-checkbox > svg")
    downloads_wordfile_checkbox = (By.CSS_SELECTOR,"#tree-node > ol > li > ol > li:nth-child(3) > ol > li:nth-child(1) > span > label > span.rct-checkbox")
    downloads_excelfile_checkbox = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(3) > ol > li:nth-child(2) > span > label > span.rct-checkbox")
    home_expand_button = (By.CSS_SELECTOR, "#tree-node > ol > li > span > button")
    desktop_expand_button = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(1) > span > label > span.rct-checkbox > svg")
    documents_expand_button = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(2) > span > button")
    downloads_expand_button = (By.CSS_SELECTOR, "#tree-node > ol > li > ol > li:nth-child(3) > span > button")
    check_box_results = (By.CSS_SELECTOR,"div#result")
    
    # Radio Button elements locations
    radio_button_section_button  = (By.CSS_SELECTOR, "div.element-group:nth-of-type(1) #item-2")
    radio_button_section_title = (By.CSS_SELECTOR, "h1.text-center")
    radio_button_yes_button = (By.CSS_SELECTOR, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div:nth-child(3) > div:nth-child(2) > label")
    radio_button_impressive_button = (By.CSS_SELECTOR, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div:nth-child(3) > div:nth-child(3)")
    radio_button_no_option = (By.CSS_SELECTOR, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div:nth-child(3) > div:nth-child(4)")
    radio_button_selection_result = (By.CSS_SELECTOR, "#app > div > div > div > div.col-12.mt-4.col-md-6 > div:nth-child(3) > p > span")
    
    
    def __init__(self, driver):
        super().__init__(driver)
        
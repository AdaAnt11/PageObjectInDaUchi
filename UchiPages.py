from BaseApp import BasePage
from selenium.webdriver.common.by import By

class UchiSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.ID, "login")
    LOCATOR_PASSWORD_FIELD = (By.ID, "password")
    LOCATOR_LOGIN_BUTTON = (By.CLASS_NAME, "login-form__submit")
    LOCATOR_UCHI_MAIN_PAGE = (By.ID, "root")

class LoginStudent(BasePage):

    def enter_login_data(self, login, password):
        login_field = self.find_element(UchiSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.click()
        login_field.send_keys(login)
        password_field = self.find_element(UchiSearchLocators.LOCATOR_PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(password)
        return login_field, password_field

    def click_on_the_login_button(self):
        return self.find_element(UchiSearchLocators.LOCATOR_LOGIN_BUTTON,time=2).click()

    def check_login_on_main_student_page(self):
        main_page_uchi_student = self.find_elements(UchiSearchLocators.LOCATOR_UCHI_MAIN_PAGE,time=2)
        return main_page_uchi_student
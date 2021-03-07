from SampleProject.POMDemo.Locators.locators import locators
class LoginPage():
        def __init__(self,driver):
            self.driver=driver

            self.username_textbox_id=locators.username_textbox_id
            self.password_textbox_id = locators.password_textbox_id
            self.login_button_id = locators

        def enter_username(self,username):
            self.driver.find_element_by_id(self.username_textbox_id).clear()
            self.driver.find_element_by_id(locators.username_textbox_id).send_keys(username)

        def enter_password(self,password):
            self.driver.find_element_by_id(self.password_textbox_id).clear()
            self.driver.find_element_by_id(locators.password_textbox_id).send_keys(password)

        def click_login(self):
            self.driver.find_element_by_id(locators.login_button_id).click()


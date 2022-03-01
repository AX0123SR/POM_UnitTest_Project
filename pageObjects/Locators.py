class Locators():
    # Adding locators for the page
    user_name = "txtUsername"
    pass_word = "txtPassword"
    login_button_id = "btnLogin"
    logout_profile = "/html/body/div[1]/div[1]/a[2]"
    logout_linktext = "Logout"

   #Initialises a constructor
    def __init__(self,driver):
        self.driver = driver

    #Action methods
    def setUsername(self,username):
        self.driver.find_element_by_name(self.user_name).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_name(self.pass_word).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def clickWelcome(self):
        self.driver.find_element_by_xpath(self.logout_profile).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.logout_linktext).click()
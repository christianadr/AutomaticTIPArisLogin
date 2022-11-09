from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class InputCredentials():
    
    def __init__(self, stud_num, username, password):
       
       self.driver = webdriver.Chrome()
       self.url = 'https://webqc2.tip.edu.ph/portal/student/new/public/login.php'
       
       self.stud_num = stud_num
       self.username = username
       self.password = password
       
    # Function to click login col 
    def click_login(self):
        button = self.driver.find_element(By.XPATH, "//div[@id='login-button-container']")
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).move_to_element(button).click(button).perform()    
          
    # Function to enter credentials
    def input_text(self):
        stud_num = self.driver.find_element(By.XPATH, "//input[@placeholder='Student Number']")
        username = self.driver.find_element(By.XPATH, "//input[@placeholder='User ID']")
        password = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        
        # Send keys to each element
        stud_num.send_keys(self.stud_num)
        username.send_keys(self.username)
        password.send_keys(self.password)
    
    # Function to submit credentials
    def proceed_btn(self):
        prcd_btn = self.driver.find_element(By.XPATH, "//input[@type='submit']")
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).move_to_element(prcd_btn).click(prcd_btn).perform() 
        
    def launch_(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

        # Automate process using given functions
        self.click_login()
        self.input_text()
        self.proceed_btn()
        
        # For the program not to end
        while True:
            pass

    # def quit_browser(self):
    #     self.driver.quit()

if __name__ == "__main__":
    credentials = {} # storage for values in the credentials.txt
    
    # Read credentials.txt line by line and split keys and values
    # and store it in credentials dictonary
    with open('credentials.txt') as f:
        for line in f:
            credential = line.split('=') # Split key and value
            credentials[credential[0].strip("' ")] = credential[1].strip()
    
    # Assign values to their respective variables
    student_number, username, password = "", "", ""
    locals().update(credentials)
    
    # Run browser with given url
    auto_input = InputCredentials(student_number, username, password)
    auto_input.launch_()
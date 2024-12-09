import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options


class UserLogin(unittest.TestCase):
    def __init__(self, platform_name, platform_version, device_name, app_package, app_activity):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.platform_version = platform_version  # Your device's API level
        options.device_name = device_name  # Your device ID
        # options.app = "D:\\m_project\\AutomationAppiumPython\\ShudokkhoAutomation\\Shudokkho_QA_Debug_1.9.6.apk" # Path to your APK
        options.no_reset = True  # Ensures app data isn't reset
        options.app_package = app_package
        options.app_activity = app_activity
        # options.full_reset = False  # Ensures app isn't reinstalled

        self.driver = webdriver.Remote(command_executor="http://localhost:4723", options=options)

    def close(self):
        self.driver.quit()

    def lsp_login(self):
        try:

            self.driver.find_element("xpath", '//android.widget.Button[@text="লগ ইন"]').click()
            self.driver.find_element("xpath", '//android.widget.EditText[@resource-id="com.mpower.android.app.lpin.crm:id/etUserId"]').send_keys('01100000000')

            self.driver.find_element("xpath", '//android.widget.Button[@text="লগ ইন"]').click()

            otp_code = input("Enter the OTP received: ") #4817

            # Locate the OTP input field and enter the OTP
            self.driver.find_element("id", "com.mpower.android.app.lpin.crm:id/etSMSCode").send_keys(otp_code)
            self.driver.find_element("xpath", '//android.widget.Button[@text="নিশ্চিত করুন"]').click()

            print("User successfully logged in")

        except Exception as e:
            print(f"An error occurred: {e}")


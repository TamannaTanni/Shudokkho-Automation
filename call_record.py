import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

class RecordInformation:
    def __init__(self):
        self.farmer_name = None
        self.farmer_mobile = None
        self.farmer_address = None
        self.days_to_go = 0
        self.scheduled_day = None
        self.scheduled_hour = None
        self.scheduled_minute = None
        self.scheduled_ampm = None

class CallRecord(unittest.TestCase):
    def __init__(self, app_package, app_activity, platform_version, device_name, platform_name):

        # APP_PACKAGE = "com.mpower.android.app.lpin.crm"
        # APP_ACTIVITY = "com.mpower.android.lpincrm.views.activities.NewVisitActivity"

        options = UiAutomator2Options()
        options.platform_name = platform_name
        options.platform_version = platform_version  # Your device's API level
        options.device_name = device_name  # Your device ID
        # options.app = "D:\\m_project\\AutomationAppiumPython\\ShudokkhoAutomation\\Shudokkho_QA_Debug_1.9.6.apk" # Path to your APK
        options.app_package = app_package
        options.app_activity = app_activity
        options.no_reset = True  # Ensures app data isn't reset
        # options.full_reset = False  # Ensures app isn't reinstalled

        self.driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=options)
        time.sleep(5)

    def wait_for_element(self, locator_type, locator_value):
        """Wait for an element to be present and visible."""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((locator_type, locator_value))
        )

    def click_element(self, locator_type, locator_value):
        """Wait and click an element."""
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((locator_type, locator_value))
        )
        element.click()

    def input_text(self, locator_type, locator_value, text):
        """Wait and input text into an element."""
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((locator_type, locator_value))
        )
        element.send_keys(text)

    def close(self):
        self.driver.quit()

    def newCallRecording(self):

        #creating a object of RecordInformation
        record_info = RecordInformation()
        try:
            #click on the 'new call record'
            self.click_element(
                "xpath",
                '//android.widget.TextView[@text="নতুন কল রেকর্ড"]'
            )

            #fill farmer details
            record_info.farmer_name = "Hum"
            self.input_text(By.ID,
                            'com.mpower.android.app.lpin.crm:id/acactvFarmerNameNewVisit',
                            record_info.farmer_name
                            )

            record_info.farmer_mobile = "01100000010"
            self.input_text(By.ID,
                            'com.mpower.android.app.lpin.crm:id/acactvMobileNewVisit',
                            record_info.farmer_mobile
                            )

            record_info.farmer_address = "xyz"
            self.input_text(By.ID,
                            'com.mpower.android.app.lpin.crm:id/acactvAddressNewVisit',
                            record_info.farmer_address
                            )


            #change to different date
            record_info.days_to_go = 1
            for _ in range(record_info.days_to_go):
                self.click_element(By.ID, "com.mpower.android.app.lpin.crm:id/acivNextNewVisit")

            record_info.scheduled_day = self.driver.find_element("id",'com.mpower.android.app.lpin.crm:id/actvDateNewVisit').get_attribute("text")

            record_info.scheduled_hour = self.driver.find_element("xpath", "//android.widget.Spinner[@resource-id='com.mpower.android.app.lpin.crm:id/acsTimeNewVisit']//android.widget.TextView[@resource-id='android:id/text1']").text


            # record_info.scheduled_hour = '11'

            self.driver.find_element("xpath", '//android.widget.EditText[@resource-id="com.mpower.android.app.lpin.crm:id/etMinutesNextVisit"]').clear()

            record_info.scheduled_minute = '50'

            self.input_text(By.XPATH,
                            '//android.widget.EditText[@resource-id="com.mpower.android.app.lpin.crm:id/etMinutesNextVisit"]',
                            record_info.scheduled_minute
                            )

            record_info.scheduled_ampm = self.driver.find_element("xpath",
                                                          "//android.widget.Spinner[@resource-id='com.mpower.android.app.lpin.crm:id/acsMidDayNewVisit']//android.widget.TextView[@resource-id='android:id/text1']").text

            # record_info.scheduled_ampm = 'AM'

            self.click_element(By.XPATH,'//android.widget.Button[@resource-id="com.mpower.android.app.lpin.crm:id/mbSubmitNewVisit"]')

            # Handle advertisement dialog
            try:
                self.click_element(By.ID, "com.mpower.android.app.lpin.crm:id/btnDialogClose")
            except Exception:
                print("Advertisement dialog not found. Skipping...")

            # Pause for 2-3 seconds
            time.sleep(3)


            # self.click_element(By.XPATH,'//android.widget.ImageButton[@content-desc="Navigate up"]')

            print("New call has been recorded")

            return record_info

        except Exception as e:
            print(f"An error occurred: {e}")
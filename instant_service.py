import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class AddService(unittest.TestCase):
    def __init__(self, app_package, app_activity, platform_version, device_name):
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.platform_version = platform_version
        options.device_name = device_name
        options.app_package = app_package
        options.app_activity = app_activity
        options.no_reset = True  # Ensures app data isn't reset

        self.driver = webdriver.Remote(
            command_executor="http://127.0.0.1:4723", options=options)
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

    def perform_action(self):
        try:
            # Click on "instant service"
            self.click_element(
                "xpath",
                '//android.widget.FrameLayout[@resource-id="com.mpower.android.app.lpin.crm:id/cvTreatment"]/android.widget.LinearLayout',
            )

            # Select service type dropdown
            self.click_element(
                By.XPATH,
                "//android.widget.TextView[@text='সেবার ধরন']/parent::android.widget.LinearLayout//android.widget.TextView[@text='বাছাই করুন']",
            )

            # Select a specific service type
            self.click_element(By.XPATH, "//android.widget.TextView[@text='অসুস্থতার সেবা']")

            # Define the number of days to go back
            days_to_go_back = 3
            for _ in range(days_to_go_back):
                self.click_element(By.ID, "com.mpower.android.app.lpin.crm:id/acivBackTreatment")

            # Fill in form details
            self.input_text(By.ID,"com.mpower.android.app.lpin.crm:id/acactvNameTreatment",'Abdul Malik')
            self.input_text(By.ID, "com.mpower.android.app.lpin.crm:id/acactvMobileTreatment", '01122223035')
            self.input_text(By.ID, "com.mpower.android.app.lpin.crm:id/acactvAddressTreatment", 'Shulov Majhir Bari, Harganga')

            # self.input_text(By.XPATH, "//android.widget.AutoCompleteTextView[@text='খামারির নাম']", 'Abdul Malik')
            # self.input_text(By.XPATH, "//android.widget.AutoCompleteTextView[@text='মোবাইল']", '01122223035')
            # self.input_text(By.XPATH, "//android.widget.AutoCompleteTextView[@text='ঠিকানা']",
            #                 'Shulov Majhir Bari, Harganga')

            # Select animal type
            self.click_element(
                By.XPATH,
                "//android.widget.TextView[@text='প্রাণী']/parent::android.widget.LinearLayout//android.widget.TextView[@text='বাছাই করুন']",
            )
            self.click_element(By.XPATH, "//android.widget.TextView[@text='গরু']")

            # Select animal category
            self.click_element(
                By.XPATH,
                "//android.widget.TextView[@text='প্রাণীর ধরন']/parent::android.widget.LinearLayout//android.widget.TextView[@text='বাছাই করুন']",
            )
            self.click_element(By.XPATH, "//android.widget.CheckedTextView[@text='বকনা']")

            # Select pregnancy status
            self.click_element(
                By.XPATH,
                "//android.widget.TextView[@text='গর্ভবতী']/parent::android.widget.LinearLayout//android.widget.TextView[@text='বাছাই করুন']",
            )
            self.click_element(By.XPATH, "//android.widget.TextView[@text='না']")

            # Add medicine
            self.click_element(By.ID, "com.mpower.android.app.lpin.crm:id/fabMedicine")
            self.click_element(By.XPATH, "//android.widget.TextView[@text='বাছাই করুন']")
            self.click_element(By.XPATH, "//android.widget.TextView[@text='কিটোসিস']")
            self.click_element(By.XPATH, "//android.widget.TextView[@text='Calcium preparation']")
            self.click_element(By.XPATH, "//android.widget.TextView[@text='Liq. Calplex']")
            self.click_element(By.ID, "com.mpower.android.app.lpin.crm:id/acivSubmitDialog")

            # Add second medicine
            self.click_element(By.XPATH, "//android.widget.TextView[@text='Saline & Electrolytes']")
            self.click_element(By.XPATH, "//android.widget.TextView[@text='Inj. Calcimax']")
            self.click_element(By.ID, "com.mpower.android.app.lpin.crm:id/acivSubmitDialog")

            # Scroll and submit medicines
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(1);'
            )
            self.click_element(By.ID, "com.mpower.android.app.lpin.crm:id/mbSubmitMedicine")

            # Pause for 2-3 seconds
            time.sleep(3)

            # Handle advertisement dialog
            try:
                self.click_element(By.ID, "com.mpower.android.app.lpin.crm:id/btnDialogClose")
            except Exception:
                print("Advertisement dialog not found. Skipping...")

            # Pause for 2-3 seconds
            time.sleep(3)

            # Debugging: Print the current page source
            # print("Debug: Fetching page source after closing ad dialog.")
            # print(self.driver.page_source)

            # Scroll and finalize treatment
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(1);'
            )

            # Scroll and finalize treatment
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().resourceId("com.mpower.android.app.lpin.crm:id/mbCollectionTreatment"));'
            )

            # Wait and click on 'সেবা ফি গ্রহণ করুন' button
            self.click_element(By.ID, "com.mpower.android.app.lpin.crm:id/mbCollectionTreatment")

            self.input_text(By.ID, "com.mpower.android.app.lpin.crm:id/acetBillCollection", '500')
            self.input_text(By.ID, "com.mpower.android.app.lpin.crm:id/acetPaymentCollection", '500')

            # Scroll and finalize treatment
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(1);'

            )
            # normal flow - cancle the sms and then service should be submitted
            self.click_element(By.ID, "com.mpower.android.app.lpin.crm:id/mbSubmitTreatment")
            self.click_element(By.ID, "com.mpower.android.app.lpin.crm:id/actvNegCustomDialog")

            # alternate flow - click the save to confirm
            self.click_element(By.ID, "com.mpower.android.app.lpin.crm:id/mbSubmitTreatment")
            self.click_element(By.ID, "com.mpower.android.app.lpin.crm:id/actvNegCustomDialog")

            print("Service successfully added")

        except Exception as e:
            print(f"An error occurred: {e}")

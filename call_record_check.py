from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from translate import EnglishToBangla
import time


class RecordCheck:
    def __init__(self, app_package, app_activity, platform_version, device_name, platform_name):

        options = UiAutomator2Options()
        options.platform_name = platform_name
        options.platform_version = platform_version  # Your device's API level
        options.device_name = device_name  # Your device ID
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


    def validate_a_record(self,schedule_information):
        try:
            # Click on "Your Schedule"
            self.click_element(
                By.XPATH,
                '//android.widget.FrameLayout[@resource-id="com.mpower.android.app.lpin.crm:id/cvRoutine"]/android.widget.LinearLayout'
            )

            print(
                f"\nfarmer name: {schedule_information.farmer_name}\nfarmer's mobile: {schedule_information.farmer_mobile}\nfarmer address: {schedule_information.farmer_address}\ndays_to_go: {schedule_information.days_to_go}\nscheduled day: {schedule_information.scheduled_day}\nscheduled hour: {schedule_information.scheduled_hour}\nscheduled minute: {schedule_information.scheduled_minute}\nscheduled AM/PM: {schedule_information.scheduled_ampm}")

            bangla_translate = EnglishToBangla()

            bangla_hour = bangla_translate.translate_number(schedule_information.scheduled_hour)

            bangla_minute = bangla_translate.translate_number(schedule_information.scheduled_minute)

            bangla_ampm = bangla_translate.translate_ampm(schedule_information.scheduled_hour, schedule_information.scheduled_ampm)

            print(f"{bangla_ampm} {bangla_hour}টা {bangla_minute}")

            # Define the number of days to go after
            days_to_go_after = schedule_information.days_to_go
            for _ in range(days_to_go_after):
                self.click_element(By.ID, "com.mpower.android.app.lpin.crm:id/acivNextRoutine")

            active_date = self.driver.find_element("id",'com.mpower.android.app.lpin.crm:id/actvDateRoutine').get_attribute("text")

            if schedule_information.scheduled_day == active_date:

                print(f"\n{schedule_information.scheduled_day} ={active_date}")

                # Locate the schedule list class
                try:

                    name_xpath = f"//android.widget.TextView[@text='{schedule_information.farmer_name}']"

                    print(name_xpath)

                    card_view_xpath = f"{name_xpath}/ancestor::androidx.cardview.widget.CardView"

                    print(card_view_xpath)

                    card_view = self.driver.find_element(AppiumBy.XPATH, card_view_xpath)

                    print(f"{card_view.text}")

                    # time_xpath = f"{card_view_xpath}//android.widget.TextView[contains(@text, '{bangla_hour}টা ')]"
                    time_xpath = f"{card_view_xpath}//android.widget.TextView[contains(@resource-id, 'com.mpower.android.app.lpin.crm:id/actvTimeRoutineItem')]"

                    print(time_xpath)

                    timing = self.driver.find_element(AppiumBy.XPATH, time_xpath).text

                except Exception as e:
                    print(f"An error occurred: {str(e)}")

                time_string = f"{bangla_ampm} {bangla_hour}টা {bangla_minute}"

                print(time_string)
                print(timing)

                assert timing ==time_string, "scheduled time didnot match"

                try:
                    farmer_name_xpath = f"{card_view_xpath}//android.widget.TextView[contains(@resource-id, 'com.mpower.android.app.lpin.crm:id/actvTimeRoutineItem')]"

                    print(time_xpath)

                except Exception as e:
                    print(f"An error occurred: {str(e)}")

            else:
                    print("Date didn't match")

            print("again checking")

            self.click_element(By.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
        except Exception as e:
            print(f"An error occurred: {e}")


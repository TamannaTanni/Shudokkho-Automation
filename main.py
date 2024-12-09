from instant_service import AddService
from login import UserLogin
from call_record import CallRecord
from call_record_check import RecordCheck

# Define app details
APP_PACKAGE = "com.mpower.android.app.lpin.crm"
APP_ACTIVITY = "com.mpower.android.lpincrm.views.activities.SplashActivity"
PLATFORM_VERSION = "11"  # Your device's API level
DEVICE_NAME = "emulator-5554"  # Your device ID
PLATFORM_NAME = "Android"


# Main script
if __name__ == "__main__":
    try:
        # appium_client = AddService(
        #     app_package=APP_PACKAGE,
        #     app_activity=APP_ACTIVITY,
        #     platform_version=PLATFORM_VERSION,
        #     device_name=DEVICE_NAME,
        # )
        # appium_client.perform_action()

        # login_test = UserLogin(
        #     app_package=APP_PACKAGE,
        #     app_activity=APP_ACTIVITY,
        #     platform_name = PLATFORM_NAME,
        #     platform_version=PLATFORM_VERSION,
        #     device_name=DEVICE_NAME,
        # )
        # login_test.lsp_login()

        record_a_call = CallRecord(
                app_package=APP_PACKAGE,
                app_activity=APP_ACTIVITY,
                platform_name = PLATFORM_NAME,
                platform_version=PLATFORM_VERSION,
                device_name=DEVICE_NAME,
        )
        schedule_information = record_a_call.newCallRecording()

        call_record_check = RecordCheck(
            app_package=APP_PACKAGE,
            app_activity=APP_ACTIVITY,
            platform_name=PLATFORM_NAME,
            platform_version=PLATFORM_VERSION,
            device_name=DEVICE_NAME,
        )
        recorded_information = call_record_check.validate_a_record(schedule_information)

    finally:
        # appium_client.close()
        # login_test.close()
        record_a_call.close()
        call_record_check.close()


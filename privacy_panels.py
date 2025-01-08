import subprocess
import platform
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PrivacyPanels:
    def __init__(self):
        self.os = platform.system()
        if self.os != "Windows":
            raise EnvironmentError("PrivacyPanels is only compatible with Windows operating systems.")
        logging.info("PrivacyPanels initialized for Windows.")

    def disable_telemetry(self):
        """Disable Windows telemetry to enhance privacy."""
        try:
            logging.info("Disabling telemetry...")
            subprocess.run(
                ["reg", "add", "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection", "/v", "AllowTelemetry", "/t", "REG_DWORD", "/d", "0", "/f"],
                check=True
            )
            logging.info("Telemetry disabled successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to disable telemetry: {e}")

    def configure_location_settings(self, enable=False):
        """Configure location tracking settings."""
        try:
            logging.info(f"{'Enabling' if enable else 'Disabling'} location services...")
            subprocess.run(
                ["reg", "add", "HKLM\\SYSTEM\\CurrentControlSet\\Services\\lfsvc\\Service\\Configuration", "/v", "Status", "/t", "REG_DWORD", "/d", "1" if enable else "0", "/f"],
                check=True
            )
            logging.info(f"Location services {'enabled' if enable else 'disabled'} successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to configure location settings: {e}")

    def configure_advertising_id(self, enable=False):
        """Manage the advertising ID setting."""
        try:
            logging.info(f"{'Enabling' if enable else 'Disabling'} advertising ID...")
            subprocess.run(
                ["reg", "add", "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\AdvertisingInfo", "/v", "Enabled", "/t", "REG_DWORD", "/d", "1" if enable else "0", "/f"],
                check=True
            )
            logging.info(f"Advertising ID {'enabled' if enable else 'disabled'} successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to configure advertising ID: {e}")

    def apply_all_settings(self):
        """Apply all privacy settings."""
        logging.info("Applying all privacy settings...")
        self.disable_telemetry()
        self.configure_location_settings(enable=False)
        self.configure_advertising_id(enable=False)
        logging.info("All privacy settings applied.")

if __name__ == "__main__":
    pp = PrivacyPanels()
    pp.apply_all_settings()
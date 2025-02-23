import subprocess
import os
from dotenv import load_dotenv

class GetBattery:
    @staticmethod
    def get_battery(serial_number: str):
        try:
            command = ["adb", "-s", serial_number, "shell", "dumpsys", "battery"]
            result = subprocess.run(command, capture_output=True, text=True, check=True)

            if result.returncode != 0:
                print(f"Error: {result.stderr}")
                return None  # Mengembalikan None jika perintah gagal

            battery = {"output": result.stdout}
            return battery

        except subprocess.SubprocessError as e:
            print(f"Ada error pada subprocess: {e}")
            return None  # Pastikan fungsi tetap mengembalikan nilai

        except Exception as e:
            print(f"Ada error ketika mendapatkan status battery: {e}")
            return None  # Sama seperti di atas

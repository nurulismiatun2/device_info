from datetime import datetime
from app.service.get_battery_service import GetBattery
from fastapi import APIRouter

router = APIRouter()

@router.get("/Device-Information/{serial_number}")
def Device_Information(serial_number: str):
    try:
        start_time = datetime.now()

        battery_info = GetBattery.get_battery(serial_number)

        if battery_info is None:
            return {
                "Time": start_time.isoformat(),
                "Status": "failed",
                "Message": "Gagal mendapatkan informasi baterai"
            }

        message = {
            "Time": start_time.isoformat(),  # Menggunakan format ISO untuk JSON
            "Status": "success",
            "Battery": battery_info
        }
        return message

    except Exception as e:
        print(f"Ada masalah di endpoint /Device-Information: {e}")
        return {
            "Time": datetime.now().isoformat(),
            "Status": "error",
            "Message": "Terjadi kesalahan saat memproses permintaan"
        }

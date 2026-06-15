from datetime import datetime

from utils.file_helper import create_log_dir
from core.geo_calculator import calculate_distance
from core.time_estimator import predict_eta


shipments = [
    {"id": "TRK-001", "from_lat": 21.0285, "from_lon": 105.8542, "to_lat": 10.8231, "to_lon": 106.6297, "depart": "2026-06-10 08:00:00", "deadline": "2026-06-11 12:00:00"}, # Đúng chuẩn
    {"id": "TRK-002", "from_lat": 21.0285, "from_lon": 105.8542, "to_lat": 16.0544, "to_lon": 108.2022, "depart": "2026-06-10 09:30:00", "deadline": "2026-06-10 15:00:00"}, # Quá hạn ETA
]

print("\n====== HỆ THỐNG ĐIỀU PHỐI RIKKEI LOGISTICS =======")

create_log_dir("logs")

print("[INFO] Khởi tạo hệ thống lưu trữ log hành trình... Thành công.")
print("---------------------------------------------------------------------------")
for shipment in shipments:
    distance = calculate_distance(shipment["from_lat"], shipment["from_lon"], shipment["to_lat"], shipment["to_lon"])

    eta = predict_eta(shipment["depart"],distance)

    deadline = datetime.strptime(shipment["deadline"],"%Y-%m-%d %H:%M:%S")

    print(f"\n[CHUYẾN XE "f"{shipment['id']}]")
    print(f" + Khoảng cách vận chuyển: "f"{distance:.2f} km")
    print(f" + Thời gian khởi hành: "f"{shipment['depart']}")
    print(f" + Dự kiến cập bến (ETA): "f"{eta}")

    if eta <= deadline:
        print(" + Trạng thái: 🟢 AN TOÀN (Kịp tiến độ trước deadline)")
    else:
        print(f" + Trạng thái: 🔴 CẢNH BÁO (Trễ hạn! Deadline yêu cầu lúc {deadline.time()})")

print("========================================================")
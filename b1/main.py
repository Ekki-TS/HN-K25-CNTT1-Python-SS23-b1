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

"""
1. Tại sao from math import * là Anti-pattern?

=> Vì import * sẽ import toàn bộ hàm và biến trong thư viện math vào chương trình.

Tác hại:
- Ô nhiễm namespace.
- Dễ trùng tên hàm với code tự viết.
- Khó đọc và khó bảo trì.
- Tốn tài nguyên hơn khi chỉ dùng vài hàm.

Cách import an toàn:
import math
distance = math.sqrt(25) hoặc from math import sqrt
=> dùng gì thì import nấy.

2. Để biến thư mục thành Package cần tệp nào?
=> Cần tạo file:
__init__.py
Vai trò:
- Đánh dấu thư mục là Package.
- Cho phép import module bên trong.
- Có thể dùng để gom hoặc khởi tạo package.

"""

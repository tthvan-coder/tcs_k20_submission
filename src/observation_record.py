from datetime import datetime

# 1. Nhập 4 trường dữ liệu quan sát
ma_quan_sat = input("Nhập mã quan sát: ")
dai_luong = input("Nhập tên đại lượng: ")
gia_tri_do = float(input("Nhập giá trị đo: "))
don_vi = input("Nhập đơn vị: ")
observer = input("Nhập người quan sát: ")

# 2. Lấy thời điểm hiện tại và định dạng chuỗi
thoi_diem = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 3. Xuất bản ghi hoàn chỉnh bằng f-string
print(f"Mã quan sát : {ma_quan_sat}")
print(f"Đại lượng   : {dai_luong}")
print(f"Giá trị     : {gia_tri_do:.2f} {don_vi}")
print(f"Thời điểm   : {thoi_diem}")
print(f"Người quan sát: {observer}")
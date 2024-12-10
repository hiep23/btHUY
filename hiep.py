from sense_emu import SenseHat
import time

# Khởi tạo Sense HAT
sense = SenseHat()

# Màu sắc cho LED
DO = [255, 0, 0]
DEN = [0, 0, 0]

# Hiển thị chữ "HIEP" trên ma trận LED
def hien_thi_HIEP():
    sense.clear()  # Xóa màn hình
    sense.show_message("HIEP", text_colour=DO, back_colour=DEN, scroll_speed=0.1)

# Hàm đọc và in dữ liệu cảm biến
def doc_du_lieu_cam_bien():
    # Đọc nhiệt độ và độ ẩm
    nhiet_do = sense.get_temperature()
    do_am = sense.get_humidity()
    
    # Đọc trạng thái của joystick
    su_kien = sense.stick.get_events()
    for sk in su_kien:
        if sk.action == "pressed":
            print(f"Joystick: {sk.direction} được nhấn")
    
    # In dữ liệu ra màn hình console
    print(f"Nhiệt độ: {nhiet_do:.1f}°C, Độ ẩm: {do_am:.1f}%")

# Vòng lặp chính
def main():
    while True:
        doc_du_lieu_cam_bien()
        hien_thi_HIEP()
        time.sleep(2)  # Chờ 2 giây trước khi lặp lại

# Chạy chương trình
if __name__ == "__main__":
    main()
import cv2
import time
import pyrebase

config ={
    "apiKey": "AIzaSyDQu3Tgdnq9mhFPffs-VsLifMar6_GlxQQ",
    "authDomain": "khangg-f59cf.firebaseapp.com",
    "projectId": "khangg-f59cf",
    "storageBucket": "khangg-f59cf.appspot.com",
    "messagingSenderId": "317057763179",
    "appId": "1:317057763179:web:7f54d5ba47874f768b6e2e",
    "measurementId": "G-YL09MMTC3T",
    "serviceAccount": "service.json",
    "databaseURL": "https://khangg-f59cf-default-rtdb.firebaseio.com/"
}

def capture_and_save_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Không thể mở webcam.")
        return

    current_hour = time.localtime().tm_hour
    while current_hour >= 0 and current_hour <= 1:
        ret, frame = cap.read()
        if not ret:
            print("Không thể chụp ảnh.")
            break

        timestamp = time.strftime("%Y%m%d_%H%M%S")
        file_name = f"image_{timestamp}.jpg"
        save_path = "C:\\Users\\Khang Nguyen\\Desktop\\" + file_name
        cv2.imwrite(save_path, frame)
        print(f"Đã chụp và lưu ảnh {file_name}")

        time.sleep(10)

        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        storage.child(file_name).put(save_path)

        current_hour = time.localtime().tm_hour

    cap.release()
    cv2.destroyAllWindows()

# Gọi hàm để bắt đầu chụp ảnh
capture_and_save_image()

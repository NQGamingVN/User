import requests
import json
import sys
import os
from packaging import version

# Cấu hình
VERSION = 1.1  # Version hiện tại của tool
UPDATE_URL = "https://raw.githubusercontent.com/NQGamingVN/User/refs/heads/main/update"

def check_for_updates():
    try:
        # Lấy thông tin update từ GitHub
        response = requests.get(UPDATE_URL)
        response.raise_for_status()
        update_info = json.loads(response.text)
        
        # So sánh version
        if version.parse(str(VERSION)) < version.parse(str(update_info["version"])):
            print(f"⚠️ Phiên bản mới {update_info['version']} đã có sẵn!")
            print(f"Thay đổi:\n{update_info['changelog']}")
            
            # Hỏi người dùng có muốn update không
            choice = input("Bạn có muốn cập nhật không? (y/n): ").lower()
            if choice == 'y':
                download_update(update_info['update_url'])
            else:
                print("Bỏ qua cập nhật.")
        else:
            print("✅ Bạn đang dùng phiên bản mới nhất.")
            
    except Exception as e:
        print(f"❌ Không thể kiểm tra bản cập nhật: {e}")

def download_update(url):
    try:
        print(f"🔍 Đang tải bản cập nhật từ {url}...")
        
        # Lấy tên file từ URL
        filename = url.split('/')[-1]
        
        # Tải file
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Lưu file
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"✅ Tải thành công: {filename}")
        print("Vui lòng chạy file mới tải về để cập nhật.")
        
    except Exception as e:
        print(f"❌ Lỗi khi tải bản cập nhật: {e}")

def main():
    print(f"🛠️ Tool của bạn - Phiên bản {VERSION}")
    # ... code chính của tool ...
    
    # Kiểm tra update
    check_for_updates()

if __name__ == "__main__":
    main()
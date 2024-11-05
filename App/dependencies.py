# dependencies.py
from fastapi import Depends, HTTPException, Request

# กำหนดรายการ IP ที่ได้รับอนุญาต
TRUSTED_IPS = {"127.0.0.1", "192.168.250..197"}  # เปลี่ยนเป็น IP ที่ต้องการอนุญาต

# สร้างฟังก์ชัน Dependency สำหรับตรวจสอบ IP
async def verify_ip_whitelist(request: Request):
    client_ip = request.client.host
    if client_ip not in TRUSTED_IPS:
        raise HTTPException(status_code=403, detail="Access forbidden: IP not allowed")
    return True

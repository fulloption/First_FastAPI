from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

# ข้อมูลจำลอง (Mock Data)
mock_users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

@router.post("/", status_code=201)
def create_user(user: dict):  # ไม่ต้องใช้ Pydantic model ในตัวอย่างนี้
    # ในสถานการณ์จริง คุณจะบันทึกข้อมูลลง Database ที่นี่
    # แต่ในตัวอย่างนี้ เราแค่แสดงผลข้อมูลที่ได้รับ
    print("ได้รับข้อมูล user:", user)
    return {"message": "User created successfully"}

@router.get("/{user_id}")
def read_user(user_id: int):
    for user in mock_users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
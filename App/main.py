from fastapi import FastAPI, Depends, Request
from .routers import users
from fastapi.openapi.docs import get_swagger_ui_html
from .dependencies import verify_ip_whitelist


app = FastAPI()

app.include_router(users.router)

# ใช้ dependency ที่กำหนด IP Whitelisting กับ /docs
@app.get("/docs", dependencies=[Depends(verify_ip_whitelist)])
async def get_documentation(request: Request):
    return get_swagger_ui_html(openapi_url=app.openapi_url, title="docs")

# ตัวอย่างการใช้ dependency กับ endpoint อื่น ๆ
@app.get("/api/example", dependencies=[Depends(verify_ip_whitelist)])
async def example_endpoint():
    return {"message": "This endpoint is protected by IP whitelist"}

@app.get("/")
def read_root():
    return {"Hello": "World"}
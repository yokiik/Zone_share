from fastapi import FastAPI,Depends,File,UploadFile
from sqlalchemy.orm import Session
from models import UserRead,UserCreate
from database import get_db,User
from typing import Annotated
from pathlib import Path

app = FastAPI()

Path("upload").mkdir(exist_ok=True)

# @app.post("/",response_model=UserRead)
# def create_user(data : UserCreate,db:Session = Depends(get_db)):
#     user = User(login = data.login,password = data.password)
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user

@app.post("/files/uploadfile/")
async def upload_file(file:UploadFile):
    with open(f"upload/{file.filename}","wb") as f:
        while True:    
            data = await file.read(1024)
            if not data:
                break    
            f.write(data)
    return {"filename": file.filename,"filesize":file.size,"filetype":file.content_type}

if __name__ == "__main__":
    pass

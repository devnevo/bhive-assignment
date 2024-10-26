import os
import logging
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from models import User
from dotenv import load_dotenv


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__) 

load_dotenv()

user_name = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
token = os.getenv("TOKEN")

router = APIRouter()

@router.post("/login")
def login(user: User):
    if user.username == user_name and user.password == password:
        return {
            "message": "Login successful!",
            "access_token": token,
            "user": {
                "username": user.username
            }
        }
    raise HTTPException(status_code=400, detail="Invalid credentials")


@router.post("/logout")
def logout():
    return {"message": "Logout successful!"}

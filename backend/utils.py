import os
import logging
from fastapi import HTTPException, Header
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__) 

ACCESS_TOKEN = os.getenv('TOKEN')

def verify_access_token(Authorization: str = Header(...)):
    logger.info(Authorization)
    if not Authorization.startswith("Bearer "):
        raise HTTPException(status_code=400, detail="Invalid authorization scheme")

    # Extract the token from the Authorization header
    token = Authorization.split(" ")[1]
    logger.info(ACCESS_TOKEN)
    if token != ACCESS_TOKEN:
        raise HTTPException(status_code=400, detail="Invalid credentials")

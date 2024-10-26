import os
import requests
import logging
from fastapi import APIRouter, Depends, HTTPException, Header
from pydantic import BaseModel
from models import User, Scheme
from utils import verify_access_token
from dotenv import load_dotenv
from cachetools import cached, TTLCache



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__) 

cache = TTLCache(maxsize=100, ttl=3000)

load_dotenv()
router = APIRouter()

RAPID_API_HOST = os.getenv("RAPID_API_HOST")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")

@cached(cache)
def fetch_schemes_from_api():
    headers = {
        'x-rapidapi-key': RAPID_API_KEY,
        'x-rapidapi-host': RAPID_API_HOST 
    }
    url = f'https://{RAPID_API_HOST}/latest'
    params = {"Scheme_Type": "Open"}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch schemes!")

@router.get("/list-all-schemes/", dependencies=[Depends(verify_access_token)])
async def get_schemes_list():
    data = fetch_schemes_from_api()  # Fetch from cache or API
    logger.info(data[0])  # Log the first item for debugging
    return {"results": [Scheme(**item).dict() for item in data]}


@cached(cache)
def fetch_fund_family_from_api(fund_family: str):
    headers = {
        'x-rapidapi-key': RAPID_API_KEY,
        'x-rapidapi-host': RAPID_API_HOST 
    }
    url = f'https://{RAPID_API_HOST}/latest'
    params = {"Scheme_Type": "Open", "Mutual_Fund_Family": fund_family}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch fund family!")

@router.post("/fund-family", dependencies=[Depends(verify_access_token)])
async def get_fund_family(fund_family: str = Header(...)):
    data = fetch_fund_family_from_api(fund_family)
    return {"results": [Scheme(**item).dict() for item in data]}
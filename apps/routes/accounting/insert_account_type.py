from fastapi import APIRouter, Body, HTTPException, Depends, Request, Response, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Union, List, Optional
from pydantic import BaseModel
from bson import ObjectId


from pymongo import  DESCENDING


from datetime import datetime, timedelta, date
from apps.authentication.authenticate_user import get_current_user
from apps.base_model.type_of_account_bm import AccountTypeBM




api_job_order = APIRouter()
templates = Jinja2Templates(directory="apps/templates")









@api_job_order.post('/api-insert-account-type')
async def insert_job_order(items:AccountTypeBM, username: str = Depends(get_current_user)):
    
    return {"message":"Data has been save"} 




  





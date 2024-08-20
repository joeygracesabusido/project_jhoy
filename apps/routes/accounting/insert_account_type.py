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
from apps.views.accounting.account_type_views import TypeofAccountViews



api_account_type = APIRouter()
templates = Jinja2Templates(directory="apps/templates")


@api_account_type.post('/api-insert-account-type')
async def insert_account_type(items:AccountTypeBM, username: str = Depends(get_current_user)):

    
    try:
        TypeofAccountViews.insert_type_of_account(items)
        return {"message": "Account type added successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    



  





from fastapi import APIRouter, Body, HTTPException, Depends, Request, Response, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Union, List, Optional
from pydantic import BaseModel
from bson import ObjectId


from pymongo import  DESCENDING


from datetime import datetime, timedelta, date
from apps.authentication.authenticate_user import get_current_user
from apps.base_model.chart_of_account_bm import ChartofAccountBM
from apps.views.accounting.chart_of_account_views import ChartofAccountViews



api_chart_of_account = APIRouter()
templates = Jinja2Templates(directory="apps/templates")


@api_chart_of_account.post('/api-insert-chart-of-account/')
async def insert_account_type(items:ChartofAccountBM, username: str = Depends(get_current_user)):

    
    try:
        ChartofAccountViews.insert_chart_of_account(items)
        return {"message": "Account type added successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    



  





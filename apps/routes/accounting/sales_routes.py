from fastapi import APIRouter, Body, HTTPException, Depends, Request, Response, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Union, List, Optional, Dict
from pydantic import BaseModel
from bson import ObjectId





from datetime import datetime, timedelta, date
from apps.authentication.authenticate_user import get_current_user
from apps.base_model.sales_bm import SalesBM
from apps.views.accounting.sales_views import SalesViews



api_sales = APIRouter()
templates = Jinja2Templates(directory="apps/templates")

@api_sales.get("/sales/", response_class=HTMLResponse)
async def api_chart_of_account_template(request: Request,
                                        username: str = Depends(get_current_user)):
 
    return templates.TemplateResponse("accounting/sales.html", 
                                      {"request": request})


@api_sales.post("/api-create-sales/", response_model=None)
async def create_sales(item: SalesBM, username: str = Depends(get_current_user)):
    try:
        SalesViews.insert_sales(item, user=username)
        return {"message": "Sales Transaction created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating profile: {e}")

@api_sales.get("/api-get-sales-list/", response_model=List[SalesBM])
async def get_sales(username: str = Depends(get_current_user)):
    try:
        profiles = SalesViews.sales_list()
        return profiles
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error retrieving profiles: {e}")

@api_sales.put("/api-update-sales-transaction/", response_model=None)
async def update_sales_trans(profile_id: int, item: SalesBM,username: str = Depends(get_current_user)):
    item.id = profile_id
    updated_profile = SalesViews.update_sales(item, user=username,date_update=datetime.now)
    if updated_profile:
        return {"message": "Sales Transaction updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Profile not found")
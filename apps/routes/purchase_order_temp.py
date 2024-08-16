from fastapi import APIRouter, Body, HTTPException, Depends, Request, Response, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Union, List, Optional
from datetime import datetime, date , timedelta
from fastapi.responses import JSONResponse

from pydantic import BaseModel

from  ..database.mongodb import create_mongo_client
mydb = create_mongo_client()

from bson import ObjectId

from  ..authentication.authenticate_user import get_current_user

api_purchase_ord_temp= APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="apps/templates")


@api_purchase_ord_temp.get("/api-purchase-order-temp/", response_class=HTMLResponse)
async def api_ticketing(request: Request,username: str = Depends(get_current_user)):
    return templates.TemplateResponse("purchase_order/po.html", {"request": request})

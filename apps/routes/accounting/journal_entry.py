from fastapi import APIRouter, Body, HTTPException, Depends, Request, Response, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Union, List, Optional
from pydantic import BaseModel
from bson import ObjectId





from datetime import datetime, timedelta, date
from apps.authentication.authenticate_user import get_current_user
from apps.base_model.journal_entry_bm import JournalEntryBM
from apps.views.accounting.journal_entry_views import JournalEntryViews



api_journale_entry = APIRouter()
templates = Jinja2Templates(directory="apps/templates")


@api_journale_entry.get('/api-get-journal-entry-list/', response_model=List[JournalEntryBM])
async def get_journal_entry(username: str = Depends(get_current_user)):
    try:

        if username:
           
            # Call the method to get the list of chart of accounts
            jorunal_entry = JournalEntryViews.get_journal_entry()
            return jorunal_entry
        
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not Authorized",
            # headers={"WWW-Authenticate": "Basic"},
            )
                

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@api_journale_entry.get('/api-get-journal-entry-by-ref/', response_model=List[JournalEntryBM])
async def get_jorunal_entry_by_ref(ref: str, username: str = Depends(get_current_user)):
    try:
        # Call the method to get the list of chart of accounts
        jv_list = JournalEntryViews.get_journal_entry_by_ref(journal_type=ref)
        
        if jv_list is None:
            raise HTTPException(status_code=404, detail="No journal voucher found")
        
        return [jv_list]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    



  





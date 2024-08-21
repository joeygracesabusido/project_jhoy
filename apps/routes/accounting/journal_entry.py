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
async def get_journal_entry(sername: str = Depends(get_current_user)):
    try:
        # Call the method to get the list of chart of accounts
        jorunal_entry = JournalEntryViews.get_journal_entry()
        
        if jorunal_entry is None:
            raise HTTPException(status_code=404, detail="No chart of accounts found")
        
        return jorunal_entry

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    



  





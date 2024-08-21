from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class JournalEntryBM(BaseModel):
    id: Optional[int] 
    transdate: date
    journal_type: str 
    reference: str 
    description: str
    chart_of_account_code: str 
    chart_of_account: str 
    account_code_id: Optional[int] 
    debit: float 
    credit: float 
    user: str 
    date_updated: Optional[datetime]
    date_created: Optional[datetime]
   

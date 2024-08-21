from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class ChartofAccountBM(BaseModel):
    
    transdate: date 
    journal_type: str
    reference: str 
    description: str 
    chart_of_account_code: str
    chart_of_account: str 
    account_code_id: int
    debit: float 
    credit: float 
    user: Optional[str]
    date_updated: Optional[datetime]
    date_created: Optional[datetime]
   
   
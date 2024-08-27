from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class ChartofAccountBM(BaseModel):

    id: Optional[int] 
    chart_of_account_code: str 
    chart_of_account: str 
    accoun_type_id: Optional[int]
    description: str 
    user: str 
    date_updated: Optional[datetime] 
    date_created: Optional[datetime] 
    
   
   
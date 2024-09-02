from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class BranchBM(BaseModel):

    id:  Optional[int] = None
    branch_name: str 
    address: str 
    user: str 
    date_updated: Optional[datetime] 
    date_created: Optional[datetime]

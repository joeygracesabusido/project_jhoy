from pydantic import BaseModel
from typing import Optional

from datetime import datetime

class UserBM(BaseModel):
    
    id: Optional[int] = None
    username: str 
    hashed_password: str 
    email_add: Optional[str] = None
    full_name: str 
    role: str 
    is_active: bool 
    date_updated: Optional[datetime] = None
    
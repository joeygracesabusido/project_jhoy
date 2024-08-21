from fastapi import APIRouter, Body, HTTPException, Depends, Request, Response, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Union, List, Optional
from datetime import datetime, date , timedelta
from fastapi.responses import JSONResponse

from pydantic import BaseModel



from bson import ObjectId

from ...authentication.authenticate_user import get_current_user

from apps.views.accounting.journal_entry_views import JournalEntryViews

api_accounting_temp= APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="apps/templates")


@api_accounting_temp.get("/api-accounting-temp/", response_class=HTMLResponse)
async def api_ticketing(request: Request):
    return templates.TemplateResponse("accounting/insert_journal_entry.html", {"request": request})

@api_accounting_temp.get("/api-journal-entry-list-temp/", response_class=HTMLResponse)
async def api_ticketing(request: Request):
    return templates.TemplateResponse("accounting/journal_entry_list.html", {"request": request})




@api_accounting_temp.post("/api-accounting-temp/", response_class=HTMLResponse)
async def insert_journal_entry(request: Request,username: str = Depends(get_current_user)):
    """This function is for posting accounting entries."""
    form = await request.form()

    trans_date = form.get('trans_date')
    journal_type = form.get('journal_type')
    reference = form.get('reference')
    description = form.get('description')

    
    account_title = []
    debitAmount = []
    creditAmount = []
    account_code_id = []
    account_code = []
    index = 1

    while form.get(f'accountTitle{index}') is not None:
        account_title.append(form.get(f'accountTitle{index}'))
        debitAmount.append(form.get(f'amount{index}'))
        creditAmount.append(form.get(f'credit_amount{index}'))
        account_code_id.append(form.get(f'chart_of_account_id{index}'))
        account_code.append(form.get(f'account_code{index}'))
        index += 1

    # Prepare the data for insertion
    totalD = 0
    totalC = 0
    result = []

    for i in range(len(account_title)):
        debit2 = float(debitAmount[i].replace(',', '')) if debitAmount[i] else 0
        credit2 = float(creditAmount[i].replace(',', '')) if creditAmount[i] else 0
        totalD += debit2
        totalC += credit2
        result.append({
            "transdate": trans_date, 
            "journal_type": journal_type,
            "reference": reference,
            "reference": reference,
            "description": description, 
            "chart_of_account": account_title[i],
            "account_code_id": account_code_id[i],
            "chart_of_account_code": account_code[i],
            "debit": debit2,
            "credit": credit2,
            "user": username
            
          
        })

    totalAmount = totalD - totalC


    # print(result)

    if totalAmount == 0:
        for entry in result:
            try:
                # Insert the entry into the database
                JournalEntryViews.insert_journal_entry(**entry)
            except Exception as e:
                messeges = [str(e)]
                return templates.TemplateResponse("accounting/insert_journal_entry.html", 
                                                  {"request": request, "messeges": messeges})

        messeges = ["Data has been saved"]
    else:
        messeges = ["Debit and Credit Not Balanced"]

    return templates.TemplateResponse("accounting/insert_journal_entry.html", 
                                      {"request": request, "messeges": messeges})


from fastapi import APIRouter, Body, HTTPException, Depends, Request, Response, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Union, List, Optional
from datetime import datetime, date , timedelta
from fastapi.responses import JSONResponse

from pydantic import BaseModel



from bson import ObjectId

from ...authentication.authenticate_user import get_current_user

api_accounting_temp= APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="apps/templates")


@api_accounting_temp.get("/api-accounting-temp/", response_class=HTMLResponse)
async def api_ticketing(request: Request):
    return templates.TemplateResponse("accounting/accounting.html", {"request": request})


@api_accounting_temp.post("/insert-journal-entry/", response_class=HTMLResponse)
async def insert_journal_entry(request: Request):
    """This function is for posting accounting"""
    form = await request.form()

    trans_date = form.get('trans_date')
    journal = form.get('trasactionType')
    reference = form.get('reference')
    journal_memo = form.get('journal_memo')
    

    date_time_obj_to = datetime.strptime(trans_date, '%Y-%m-%d')

    account_title =[]
    debitAmount = []
    craditAmount =[]
    index = 1

    while form.get(f'accountTitle{index}')!= None:
        account_title.append(form.get(f'accountTitle{index}'))
        debitAmount.append(form.get(f'amount{index}'))
        craditAmount.append(form.get(f'credit_amount{index}'))
        index+=1
        

    
    res = []
    
    for val in account_title:
        if val != None :
            res.append(val)


    res2 = []
   
    for val in debitAmount:
        if val != None :
            res2.append(val)

    res3 = []
   
    for val in craditAmount:
        if val != None :
            res3.append(val)
            
   
    data= {}

    data.update({
        "accountTitle":res,
        "debit":res2,
        "credit":res3
    })

    entry = len(data['accountTitle'])
   

    result = []
    for i in range(entry):
        # print(i)
        d={}
        for j,k in enumerate(data.items()):
            if j == 0:
                d['accountTitle']= (k[1][i])

            if j == 1:
                d['debit']= (k[1][i])
               
            if j == 2:   
                d['credit']= (k[1][i])

        result.append(d)
    # print(result)
    
    totalD = 0
    totalC = 0
    accountTitle2 = ''
    debit2 = 0
    credit2 = 0
    totalAmount = 0
    messeges = []
    for r in result:
       
        
        accountTitle2 = r['accountTitle']
        debit2 = r['debit']
        credit2 = r['credit']
        totalD += float(debit2)
        totalC += float(credit2)
        total_debit = '{:.2f}'.format(totalD)
        total_credit = '{:.2f}'.format(totalC)

    totalAmount = float(total_debit)-float(total_credit)
    if totalAmount == 0:
   
        for r in result:
           
        
            accountTitle2 = r['accountTitle']
            debit2 = r['debit']
            credit2 = r['credit']
            totalD += float(debit2)
            totalC += float(credit2)

            try:

                token = request.cookies.get('access_token')

                all_chart_of_account = chartofAccounts(mydb.chart_of_account.find().sort('accountTitle', 1))
                if token is None:

                    messeges.append("Please log in first to validated credentials ")
                    return templates.TemplateResponse("journal_entry_zamboanga2.html", 
                                                            {"request":request,'all_chart_of_account':all_chart_of_account,
                                                            "messeges":messeges})

                    
                else:
                    scheme, _, param = token.partition(" ")
                    payload = jwt.decode(param, JWT_SECRET, algorithms=ALGORITHM)
                
                    username = payload.get("sub")
                

                    user =  mydb.login.find({"username":username})

                    if user is not None:
                        items = chartofAccounts(mydb.chart_of_account.find({'accountTitle':accountTitle2}))
                        for i in items:
                            accountNumber = i['accountNum']
                            bsType = i['bsClass']

                            

                            dataInsert = [{
                                
                                'date_entry': date_time_obj_to,
                                'journal': journal,
                                'ref': reference,
                                'descriptions': journal_memo,
                                'acoount_number': accountNumber,
                                'account_disc': accountTitle2,
                                'bsClass': bsType,
                                'debit_amount': float(debit2),
                                'credit_amount': float(credit2),
                                'due_date_apv': "",
                                'terms_days': "",
                                'supplier/Client': "",
                                'user': username,
                                'created':datetime.now()
                                
                                }]

                            
                                
                            # print(dataInsert)

                            
                            mydb.journal_entry_zambo.insert_many(dataInsert)

                    
            
            except Exception as e:
                messeges.append(e)
                return templates.TemplateResponse("journal_entry_zamboanga2.html", 
                                                        {"request":request,'all_chart_of_account':all_chart_of_account,
                                                        "messeges":messeges})
    else:
        messeges.append("Debit and Credit Not Balance")
        all_chart_of_account = chartofAccounts(mydb.chart_of_account.find().sort('accountTitle', 1))
        return templates.TemplateResponse("journal_entry_zamboanga2.html", 
                                            {"request":request,"all_chart_of_account":all_chart_of_account,
                                            "messeges":messeges})


    

            
   

    messeges.append("Data has been save")
    all_chart_of_account = chartofAccounts(mydb.chart_of_account.find().sort('accountTitle', 1))
    return templates.TemplateResponse("journal_entry.html", 
                                        {"request":request,"all_chart_of_account":all_chart_of_account,
                                        "messeges":messeges})





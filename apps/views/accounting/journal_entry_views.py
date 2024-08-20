from sqlmodel import Field, Session,  create_engine,select,func,funcfilter,within_group,Relationship,Index

from apps.models.accounting.chart_of_account import ChartofAccount
from apps.database.databases import connectionDB
from typing import Optional
from datetime import date, datetime


from apps.base_model.chart_of_account_bm import ChartofAccountBM

engine = connectionDB.conn()


class ChartofAccountViews(): # this class is for Type of Account

    @staticmethod
    def insert_chart_of_account(item: ChartofAccountBM,username: str): # this is for inserting type of Account 
        
         # Create a dictionary from the item
        item_data = item.dict()  # Assuming item is a Pydantic model
        item_data['user'] = username  # Insert the username
        
        # Create an instance of Journal Entry using ** unpacking
        insertData = ChartofAccount(**item_data)
        

        session = Session(engine)

        session.add(insertData)
        
        session.commit()

        session.close()

    @staticmethod
    def get_chart_of_account(): # this function is to get a list of type of account
        with Session(engine) as session:
            try:
                statement = select(ChartofAccount).order_by(ChartofAccount.chart_of_account_code)

               
                            
                results = session.exec(statement) 

                data = results.all()
                
                return data
            except :
                return None
            
   
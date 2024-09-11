from sqlmodel import Field, Session,  create_engine,select,func,funcfilter,within_group,Relationship,Index

from apps.models.accounting.sales import Sales
from apps.models.accounting.journal_entry import JournalEntry
from apps.database.databases import connectionDB
from typing import Optional
from datetime import date, datetime

from sqlalchemy import and_


from apps.base_model.sales_bm import SalesBM

engine = connectionDB.conn()


class SalesViews(): # this class is for Customer

    @staticmethod
    def insert_sales(item: SalesBM, user: str): # this is for inserting Sales
        
         # Create a dictionary from the item
        item_data = item.dict()  # Assuming item is a Pydantic model
        item_data['user'] = user
        # Create an instance of AccountType using ** unpacking
        insertJournal = JournalEntry(**kwargs)
        
        insertData = Sales(**item_data)


        session = Session(engine)

        session.add(insertJournal)
        session.flush()
        #modify insert add journal ID
        insertData.journal_entry_code_id = insertJournal.id
        session.add(insertData)

        
        session.commit()

        session.close()

    @staticmethod
    def sales_list(): # this function is to get a list of Sales
        with Session(engine) as session:
            try:
                statement = select(Sales)

               
                            
                results = session.exec(statement) 

                data = results.all()
                
                return data
            except :
                return None
            
   
    
    
            
    @staticmethod
    def update_sales(item: SalesBM,user:str,date_update:datetime):
      
        with Session(engine) as session:
            try:
                # Find the record to update
                statement = select(Sales).where(Sales.id == item.id)
                
                result = session.exec(statement).one_or_none()
                
                if result:
                    # Update the record's account_type
                   
                    result.journal_entry_code_id = item.journal_entry_code_id
                    result.customer_profile_id = item.customer_profile_id
                    result.user = user
                    result.date_updated = date_update
                    
                    # Commit the changes
                    session.add(result)
                    session.commit()
                    
                    # Optionally refresh the instance
                    session.refresh(result)
                    return True  # Update was successful
                else:
                    return False  # Record not found
            except Exception as e:
                # Handle any exceptions that occur
                print(f"An error occurred: {e}")
                return None

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
    def insert_sales(item: SalesBM, **kwargs):  # Accepts a Pydantic model instance and other kwargs
        session = Session(engine)

        # Create an instance of JournalEntry using **kwargs
        insertJournal = JournalEntry(**kwargs)

        # Add and commit the JournalEntry to get its ID
        session.add(insertJournal)
        session.commit()

        # Retrieve the ID of the inserted JournalEntry
        journal_entry_id = insertJournal.id

        # Prepare Sales data with the journal_entry_id as a foreign key
        sales_data = item.dict()  # Convert the Pydantic model to a dictionary
        sales_data['journal_entry_code_id'] = journal_entry_id  # Set foreign key
        sales_data['customer_profile_id'] = item.customer_profile_id  # Set additional fields if necessary

        # Create an instance of Sales with the prepared data
        insertData = Sales(**sales_data)

        # Add Sales to the session and commit
        session.add(insertData)
        session.commit()

        # Close the session
        session.close()
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

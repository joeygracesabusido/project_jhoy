from sqlmodel import Field, Session,  create_engine,select,func,funcfilter,within_group,Relationship,Index

from apps.models.accounting.journal_entry import JournalEntry
from apps.database.databases import connectionDB
from typing import Optional
from datetime import date, datetime


from apps.base_model.journal_entry_bm import JournalEntryBM

engine = connectionDB.conn()


class JournalEntryViews(): # this class is for Type of Account

    @staticmethod
    def insert_journal_entry(**kwargs): # this is for inserting type of Account 
        
        

        # Create an instance of JournalEntry using ** unpacking
        insertData = JournalEntry(**kwargs)
        

        session = Session(engine)

        session.add(insertData)
        
        session.commit()

        session.close()

    @staticmethod
    def get_journal_entry(): # this function is to get a list of type of account
        with Session(engine) as session:
            try:
                statement = select(JournalEntry)

               
                            
                results = session.exec(statement) 

                data = results.all()
                
                return data
            except :
                return None
            
   
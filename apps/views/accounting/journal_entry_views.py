from sqlmodel import Field, Session,  create_engine,select,func,funcfilter,within_group,Relationship,Index

from apps.models.accounting.journal_entry import JournalEntry
from apps.database.databases import connectionDB
from typing import Optional
from datetime import date, datetime

from sqlalchemy import desc


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
            
    @staticmethod
    def get_journal_entry_by_journal_type(journal_type):
        with Session(engine) as session:
            try:
                statement = select(JournalEntry).where(JournalEntry.journal_type == journal_type).order_by(desc(JournalEntry.reference))
                latest_entry = session.exec(statement).first()

                if latest_entry:
                    return latest_entry
                return None
            except Exception as e:
                print(f"An error occurred: {e}")
                return None
            
    @staticmethod
    def get_journal_entry_by_ref(reference):
        with Session(engine) as session:
            try:
                statement = select(JournalEntry).where(JournalEntry.reference.like(f'%{reference}%'))
                data = session.exec(statement).all()

                if data:
                    return data
                return None
            except Exception as e:
                print(f"An error occurred: {e}")
                return None
            
    @staticmethod
    def delete_journal_entry_by_ref(reference):
        with Session(engine) as session:
            try:
                # Query to find the entries matching the reference
                statement = select(JournalEntry).where(JournalEntry.reference.like(f'%{reference}%'))
                entries_to_delete = session.exec(statement).all()

                if entries_to_delete:
                    # Delete the found entries
                    for entry in entries_to_delete:
                        session.delete(entry)
                    session.commit()
                    return True  # Return True if deletion was successful
                return False  # Return False if no entries were found to delete
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
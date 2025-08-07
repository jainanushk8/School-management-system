import pymysql
import sqlalchemy
from sqlalchemy import create_engine, text
import pandas as pd
import logging

class DatabaseConfig:
    def __init__(self, host='localhost', user='root', password='my@jain07', database='school_management'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.engine = None
        self.connection = None
        
    def create_database(self):
        """Create the school_management database if it doesn't exist"""
        try:
            # Connect without specifying database to create it
            temp_engine = create_engine(f'mysql+pymysql://{self.user}:{self.password}@{self.host}')
            with temp_engine.connect() as conn:
                conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {self.database}"))
                conn.commit()
            print(f"✅ Database '{self.database}' created successfully!")
            return True
        except Exception as e:
            print(f"❌ Error creating database: {e}")
            return False
    
    def connect(self):
        """Establish connection to the database"""
        try:
            connection_string = f'mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.database}'
            self.engine = create_engine(connection_string)
            self.connection = self.engine.connect()
            print(f"✅ Connected to MySQL database: {self.database}")
            return True
        except Exception as e:
            print(f"❌ Connection failed: {e}")
            return False
    
    def test_connection(self):
        """Test database connection"""
        try:
            result = self.connection.execute(text("SELECT 1 as test"))
            print("✅ Database connection test successful!")
            return True
        except Exception as e:
            print(f"❌ Connection test failed: {e}")
            return False
    
    def close_connection(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
            print("✅ Database connection closed")

# Global database instance
db_config = DatabaseConfig()

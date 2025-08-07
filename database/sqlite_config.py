import sqlite3
import pandas as pd
import os
from typing import Optional

class SQLiteConfig:
    def __init__(self, db_path='school_management.db'):
        self.db_path = db_path
        self.connection: Optional[sqlite3.Connection] = None
        
    def connect(self) -> bool:
        """Connect to SQLite database"""
        try:
            self.connection = sqlite3.connect(self.db_path)
            # Enable foreign key constraints
            self.connection.execute("PRAGMA foreign_keys = ON")
            print(f"✅ Connected to SQLite database: {self.db_path}")
            return True
        except Exception as e:
            print(f"❌ SQLite connection failed: {e}")
            return False
    
    def execute_script(self, script_path: str) -> bool:
        """Execute SQL script file with proper error handling"""
        if not self.connection:
            print("❌ No database connection available")
            return False
            
        try:
            with open(script_path, 'r', encoding='utf-8') as file:
                sql_script = file.read()
            
            # Temporarily disable foreign key constraints during table creation
            self.connection.execute("PRAGMA foreign_keys = OFF")
            
            # Split by semicolon and execute each command
            commands = sql_script.split(';')
            for i, command in enumerate(commands):
                command = command.strip()
                if command and not command.startswith('--') and command != '':
                    try:
                        self.connection.execute(command)
                        print(f"✅ Executed command {i+1}")
                    except Exception as cmd_error:
                        print(f"⚠️  Warning on command {i+1}: {cmd_error}")
                        continue
            
            # Re-enable foreign key constraints
            self.connection.execute("PRAGMA foreign_keys = ON")
            self.connection.commit()
            print("✅ Database tables created successfully!")
            return True
        except Exception as e:
            print(f"❌ Error executing script: {e}")
            return False
    
    def test_connection(self) -> bool:
        """Test database connection and list tables"""
        if not self.connection:
            print("❌ No database connection available")
            return False
            
        try:
            cursor = self.connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
            tables = cursor.fetchall()
            table_names = [table[0] for table in tables]
            print(f"✅ Database test successful! Found {len(tables)} tables:")
            for table in table_names:
                print(f"  📋 {table}")
            return True
        except Exception as e:
            print(f"❌ Connection test failed: {e}")
            return False
    
    def close(self) -> None:
        """Close database connection"""
        if self.connection:
            self.connection.close()
            print("✅ Database connection closed")

# Global SQLite instance
sqlite_config = SQLiteConfig()

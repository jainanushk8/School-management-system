from database.sqlite_config import sqlite_config
import os

def setup_database():
    """Setup complete database with tables"""
    print("🚀 Starting SQLite Database Setup (Fixed Version)...")
    
    # Step 1: Connect to database
    if not sqlite_config.connect():
        print("❌ Failed to connect to database. Exiting...")
        return False
    
    # Step 2: Execute table creation script
    script_path = 'database/create_tables_sqlite.sql'
    if not os.path.exists(script_path):
        print(f"❌ Script file not found: {script_path}")
        return False
        
    if not sqlite_config.execute_script(script_path):
        print("❌ Failed to create tables. Exiting...")
        return False
    
    # Step 3: Test connection and show tables
    if not sqlite_config.test_connection():
        print("❌ Database test failed. Exiting...")
        return False
    
    print("\n🎉 Phase 1 Complete! Database foundation ready!")
    print("📊 Database: SQLite with 12 essential tables")
    print("📋 Next: Ready for Phase 2 - Excel data processing")
    return True

if __name__ == "__main__":
    print("=" * 60)
    print("🏫 SCHOOL MANAGEMENT SYSTEM - DATABASE SETUP")
    print("=" * 60)
    
    success = setup_database()
    if success:
        print("\n" + "=" * 60)
        print("✅ PHASE 1 COMPLETED SUCCESSFULLY!")
        print("✅ Ready to move to Phase 2 - Excel Processing!")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("❌ SETUP FAILED - Please check error messages above")
        print("=" * 60)

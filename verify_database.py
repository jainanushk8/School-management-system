from database.sqlite_config import sqlite_config
import sqlite3

def verify_database():
    """Verify database tables were created properly"""
    print("🔍 Verifying Database Setup...")
    
    try:
        # Connect directly to check tables
        conn = sqlite3.connect('school_management.db')
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        tables = cursor.fetchall()
        
        expected_tables = [
            'schools', 'grades', 'sections', 'subjects', 'teachers', 
            'students', 'teacher_subjects', 'attendance', 'homework', 
            'class_diary', 'fees', 'salary'
        ]
        
        if len(tables) == 0:
            print("❌ No tables found. Re-executing table creation...")
            # Re-execute the script
            with open('database/create_tables_sqlite.sql', 'r') as file:
                sql_script = file.read()
            
            commands = sql_script.split(';')
            for command in commands:
                command = command.strip()
                if command and not command.startswith('--'):
                    conn.execute(command)
            
            conn.commit()
            
            # Check again
            cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
            tables = cursor.fetchall()
        
        table_names = [table[0] for table in tables]
        print(f"✅ Found {len(tables)} tables:")
        for table in table_names:
            print(f"  📋 {table}")
        
        conn.close()
        
        if len(tables) == 12:
            print("✅ Database verification successful! All 12 tables found.")
            return True
        else:
            print(f"⚠️ Expected 12 tables, found {len(tables)}")
            return False
        
    except Exception as e:
        print(f"❌ Verification failed: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("🔍 DATABASE VERIFICATION")
    print("=" * 50)
    success = verify_database()
    
    if success:
        print("\n" + "=" * 50)
        print("✅ VERIFICATION PASSED!")
        print("🚀 Ready for Phase 2 - Excel Processing!")
        print("=" * 50)
    else:
        print("\n" + "=" * 50)
        print("⚠️ VERIFICATION ISSUES FOUND")
        print("=" * 50)

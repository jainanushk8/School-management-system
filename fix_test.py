import sqlite3

def debug_database_tables():
    """Debug and fix database table count issue"""
    print("🔍 Debugging database table count...")
    
    conn = sqlite3.connect('school_management.db')
    
    # Get all tables (including system tables)
    all_tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    print(f"📊 Total tables found: {len(all_tables)}")
    
    # Get only our application tables (non-system tables)
    app_tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'").fetchall()
    print(f"📋 Application tables found: {len(app_tables)}")
    
    expected_tables = [
        'schools', 'grades', 'sections', 'subjects', 'teachers', 
        'students', 'teacher_subjects', 'attendance', 'homework', 
        'class_diary', 'fees', 'salary'
    ]
    
    print(f"📌 Expected tables: {len(expected_tables)}")
    print("✅ Application tables:")
    for table in app_tables:
        print(f"  📋 {table[0]}")
    
    # Check if all expected tables exist
    existing_table_names = [table[0] for table in app_tables]
    missing_tables = [table for table in expected_tables if table not in existing_table_names]
    extra_tables = [table for table in existing_table_names if table not in expected_tables]
    
    if missing_tables:
        print(f"❌ Missing tables: {missing_tables}")
    else:
        print("✅ All expected tables present!")
    
    if extra_tables:
        print(f"ℹ️ Extra tables: {extra_tables}")
    
    conn.close()
    
    # The test should pass if we have all 12 expected tables
    return len(existing_table_names) >= 12 and len(missing_tables) == 0

if __name__ == "__main__":
    print("=" * 60)
    print("🔧 DATABASE TABLE INTEGRITY CHECK")
    print("=" * 60)
    
    success = debug_database_tables()
    
    if success:
        print("\n✅ Database integrity is actually GOOD!")
        print("✅ The test failure was likely due to counting logic")
    else:
        print("\n❌ Database integrity issues found")
    
    print("=" * 60)

import sqlite3
import os

def create_database_manually():
    """Manually create database with direct SQL execution"""
    print("🔧 Creating database tables manually...")
    
    # Remove existing database file if exists
    if os.path.exists('school_management.db'):
        os.remove('school_management.db')
        print("🗑️ Removed existing database file")
    
    # Create new connection
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()
    
    # Enable foreign keys
    cursor.execute("PRAGMA foreign_keys = OFF")
    
    # Create tables one by one
    tables = [
        """CREATE TABLE schools (
            school_id INTEGER PRIMARY KEY AUTOINCREMENT,
            school_name VARCHAR(200) NOT NULL,
            school_code VARCHAR(50) UNIQUE NOT NULL,
            address TEXT,
            contact_number VARCHAR(20),
            email VARCHAR(100),
            principal_name VARCHAR(100),
            established_date DATE,
            status VARCHAR(20) DEFAULT 'Active',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )""",
        
        """CREATE TABLE grades (
            grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
            school_id INTEGER,
            grade_name VARCHAR(50) NOT NULL,
            grade_level INTEGER,
            description TEXT,
            status VARCHAR(20) DEFAULT 'Active'
        )""",
        
        """CREATE TABLE sections (
            section_id INTEGER PRIMARY KEY AUTOINCREMENT,
            school_id INTEGER,
            grade_id INTEGER,
            section_name VARCHAR(10) NOT NULL,
            capacity INTEGER DEFAULT 30,
            status VARCHAR(20) DEFAULT 'Active'
        )""",
        
        """CREATE TABLE subjects (
            subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
            school_id INTEGER,
            subject_name VARCHAR(100) NOT NULL,
            subject_code VARCHAR(20),
            description TEXT,
            status VARCHAR(20) DEFAULT 'Active'
        )""",
        
        """CREATE TABLE teachers (
            teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            school_id INTEGER,
            teacher_name VARCHAR(100) NOT NULL,
            employee_id VARCHAR(50) UNIQUE,
            phone VARCHAR(20),
            email VARCHAR(100),
            address TEXT,
            qualification VARCHAR(200),
            joining_date DATE,
            salary DECIMAL(10,2),
            status VARCHAR(20) DEFAULT 'Active',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )""",
        
        """CREATE TABLE students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            school_id INTEGER,
            grade_id INTEGER,
            section_id INTEGER,
            student_name VARCHAR(100) NOT NULL,
            student_roll VARCHAR(50),
            phone VARCHAR(20),
            email VARCHAR(100),
            address TEXT,
            parent_name VARCHAR(100),
            parent_phone VARCHAR(20),
            admission_date DATE,
            status VARCHAR(20) DEFAULT 'Active',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )""",
        
        """CREATE TABLE teacher_subjects (
            mapping_id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_id INTEGER,
            subject_id INTEGER,
            grade_id INTEGER,
            section_id INTEGER,
            academic_year VARCHAR(10),
            status VARCHAR(20) DEFAULT 'Active'
        )""",
        
        """CREATE TABLE attendance (
            attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            teacher_id INTEGER,
            subject_id INTEGER,
            attendance_date DATE,
            status VARCHAR(20) DEFAULT 'Present',
            remarks TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )""",
        
        """CREATE TABLE homework (
            homework_id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_id INTEGER,
            subject_id INTEGER,
            grade_id INTEGER,
            section_id INTEGER,
            title VARCHAR(200) NOT NULL,
            description TEXT,
            assigned_date DATE,
            due_date DATE,
            status VARCHAR(20) DEFAULT 'Active',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )""",
        
        """CREATE TABLE class_diary (
            diary_id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_id INTEGER,
            subject_id INTEGER,
            grade_id INTEGER,
            section_id INTEGER,
            diary_date DATE,
            topic_covered TEXT,
            homework_given TEXT,
            remarks TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )""",
        
        """CREATE TABLE fees (
            fee_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            fee_type VARCHAR(100),
            amount DECIMAL(10,2),
            due_date DATE,
            paid_amount DECIMAL(10,2) DEFAULT 0,
            paid_date DATE,
            status VARCHAR(20) DEFAULT 'Pending',
            academic_year VARCHAR(10),
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )""",
        
        """CREATE TABLE salary (
            salary_id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_id INTEGER,
            month VARCHAR(20),
            year INTEGER,
            basic_salary DECIMAL(10,2),
            allowances DECIMAL(10,2) DEFAULT 0,
            deductions DECIMAL(10,2) DEFAULT 0,
            net_salary DECIMAL(10,2),
            paid_date DATE,
            status VARCHAR(20) DEFAULT 'Pending',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )"""
    ]
    
    table_names = ['schools', 'grades', 'sections', 'subjects', 'teachers', 'students', 
                   'teacher_subjects', 'attendance', 'homework', 'class_diary', 'fees', 'salary']
    
    # Execute each table creation
    for i, (table_sql, table_name) in enumerate(zip(tables, table_names)):
        try:
            cursor.execute(table_sql)
            print(f"✅ Created table {i+1}/12: {table_name}")
        except Exception as e:
            print(f"❌ Error creating {table_name}: {e}")
            return False
    
    # Commit all changes
    conn.commit()
    
    # Verify tables were created
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    tables_created = cursor.fetchall()
    
    print(f"\n🎉 Database creation complete!")
    print(f"✅ Successfully created {len(tables_created)} tables:")
    for table in tables_created:
        print(f"  📋 {table[0]}")
    
    conn.close()
    
    if len(tables_created) == 12:
        print("\n🚀 Phase 1 FINALLY Complete! Ready for Phase 2!")
        return True
    else:
        print(f"\n❌ Expected 12 tables, got {len(tables_created)}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🔧 MANUAL DATABASE CREATION - GUARANTEED FIX")
    print("=" * 60)
    
    success = create_database_manually()
    
    if success:
        print("\n" + "=" * 60)
        print("✅ SUCCESS! DATABASE READY!")
        print("🚀 MOVING TO PHASE 2 - EXCEL PROCESSING!")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("❌ MANUAL CREATION FAILED")
        print("=" * 60)

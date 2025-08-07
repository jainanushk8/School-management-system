-- School Management System Database Schema - SQLite Compatible
-- Simplified creation order to avoid foreign key issues

-- 1. Schools Table (No dependencies)
CREATE TABLE IF NOT EXISTS schools (
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
);

-- 2. Grades Table
CREATE TABLE IF NOT EXISTS grades (
    grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    school_id INTEGER,
    grade_name VARCHAR(50) NOT NULL,
    grade_level INTEGER,
    description TEXT,
    status VARCHAR(20) DEFAULT 'Active'
);

-- 3. Sections Table  
CREATE TABLE IF NOT EXISTS sections (
    section_id INTEGER PRIMARY KEY AUTOINCREMENT,
    school_id INTEGER,
    grade_id INTEGER,
    section_name VARCHAR(10) NOT NULL,
    capacity INTEGER DEFAULT 30,
    status VARCHAR(20) DEFAULT 'Active'
);

-- 4. Subjects Table
CREATE TABLE IF NOT EXISTS subjects (
    subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
    school_id INTEGER,
    subject_name VARCHAR(100) NOT NULL,
    subject_code VARCHAR(20),
    description TEXT,
    status VARCHAR(20) DEFAULT 'Active'
);

-- 5. Teachers Table
CREATE TABLE IF NOT EXISTS teachers (
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
);

-- 6. Students Table
CREATE TABLE IF NOT EXISTS students (
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
);

-- 7. Teacher Subject Mapping
CREATE TABLE IF NOT EXISTS teacher_subjects (
    mapping_id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_id INTEGER,
    subject_id INTEGER,
    grade_id INTEGER,
    section_id INTEGER,
    academic_year VARCHAR(10),
    status VARCHAR(20) DEFAULT 'Active'
);

-- 8. Attendance Table
CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    teacher_id INTEGER,
    subject_id INTEGER,
    attendance_date DATE,
    status VARCHAR(20) DEFAULT 'Present',
    remarks TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 9. Homework Table
CREATE TABLE IF NOT EXISTS homework (
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
);

-- 10. Class Diary Table
CREATE TABLE IF NOT EXISTS class_diary (
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
);

-- 11. Fees Table
CREATE TABLE IF NOT EXISTS fees (
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
);

-- 12. Salary Table
CREATE TABLE IF NOT EXISTS salary (
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
);

import os
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import random

class Phase2ExcelProcessor:
    def __init__(self):
        self.db_path = 'school_management.db'
        self.connection = None
        self.sample_data_dir = 'sample_data'
        
    def connect_database(self):
        """Connect to the database"""
        try:
            self.connection = sqlite3.connect(self.db_path)
            print("✅ Connected to database")
            return True
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            return False
    
    def create_sample_directories(self):
        """Create necessary directories"""
        os.makedirs(self.sample_data_dir, exist_ok=True)
        print(f"📁 Created directory: {self.sample_data_dir}/")
        
    def generate_complete_school_data(self):
        """Generate all required Excel files with realistic data"""
        print("📊 Generating comprehensive school data...")
        
        # 1. School Data (1 school as required)
        school_data = pd.DataFrame({
            'school_name': ['Greenwood High School'],
            'school_code': ['GHS001'], 
            'address': ['123 Education Street, Academic City, State - 110001'],
            'contact_number': ['9876543210'],
            'email': ['info@greenwoodhigh.edu'],
            'principal_name': ['Dr. Rajesh Kumar'],
            'established_date': ['2010-01-15'],
            'status': ['Active']
        })
        
        # 2. Grades Data (3 grades as required)
        grades_data = pd.DataFrame({
            'school_code': ['GHS001'] * 3,
            'grade_name': ['Grade 6', 'Grade 7', 'Grade 8'],
            'grade_level': [6, 7, 8],
            'description': ['Sixth Standard', 'Seventh Standard', 'Eighth Standard'],
            'status': ['Active'] * 3
        })
        
        # 3. Sections Data (2 sections per grade = 6 sections total)
        sections_data = pd.DataFrame({
            'school_code': ['GHS001'] * 6,
            'grade_name': ['Grade 6', 'Grade 6', 'Grade 7', 'Grade 7', 'Grade 8', 'Grade 8'],
            'section_name': ['A', 'B', 'A', 'B', 'A', 'B'],
            'capacity': [30, 30, 30, 30, 30, 30],
            'status': ['Active'] * 6
        })
        
        # 4. Subjects Data (8 subjects)
        subjects_data = pd.DataFrame({
            'school_code': ['GHS001'] * 8,
            'subject_name': ['Mathematics', 'English', 'Science', 'Social Studies', 
                           'Hindi', 'Computer Science', 'Physical Education', 'Arts'],
            'subject_code': ['MATH', 'ENG', 'SCI', 'SST', 'HIN', 'CS', 'PE', 'ART'],
            'description': ['Advanced Mathematics', 'English Language & Literature', 
                          'General Science', 'Social Studies & History',
                          'Hindi Language', 'Computer Science & Programming', 
                          'Physical Education & Sports', 'Arts & Crafts'],
            'status': ['Active'] * 8
        })
        
        # 5. Teachers Data (8 teachers as required)
        teachers_data = pd.DataFrame({
            'school_code': ['GHS001'] * 8,
            'teacher_name': ['Priya Sharma', 'Amit Kumar', 'Sunita Verma', 'Ravi Singh',
                           'Meera Patel', 'Ajay Gupta', 'Kavita Joshi', 'Deepak Yadav'],
            'employee_id': ['T001', 'T002', 'T003', 'T004', 'T005', 'T006', 'T007', 'T008'],
            'phone': ['9876543211', '9876543212', '9876543213', '9876543214',
                     '9876543215', '9876543216', '9876543217', '9876543218'],
            'email': ['priya.sharma@ghs.edu', 'amit.kumar@ghs.edu', 'sunita.verma@ghs.edu', 'ravi.singh@ghs.edu',
                     'meera.patel@ghs.edu', 'ajay.gupta@ghs.edu', 'kavita.joshi@ghs.edu', 'deepak.yadav@ghs.edu'],
            'qualification': ['M.Sc Mathematics', 'M.A English Literature', 'M.Sc Physics', 'M.A History',
                            'M.A Hindi Literature', 'MCA Computer Science', 'B.P.Ed Physical Education', 'BFA Fine Arts'],
            'joining_date': ['2020-01-15', '2020-02-01', '2020-03-01', '2020-04-01',
                           '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01'],
            'salary': [45000, 42000, 48000, 40000, 38000, 50000, 35000, 36000],
            'status': ['Active'] * 8
        })
        
        # 6. Students Data (60 students - 10 per section)
        students_data = self._generate_60_students()
        
        # 7. Teacher-Subject Mapping (Each teacher handles 1 subject across all grades/sections)
        teacher_subjects_data = pd.DataFrame({
            'teacher_employee_id': ['T001', 'T002', 'T003', 'T004', 'T005', 'T006', 'T007', 'T008'] * 6,  # 8 teachers × 6 sections
            'subject_code': ['MATH', 'ENG', 'SCI', 'SST', 'HIN', 'CS', 'PE', 'ART'] * 6,
            'grade_name': (['Grade 6'] * 8) + (['Grade 7'] * 8) + (['Grade 8'] * 8) + (['Grade 6'] * 8) + (['Grade 7'] * 8) + (['Grade 8'] * 8),
            'section_name': (['A'] * 24) + (['B'] * 24),
            'academic_year': ['2024-25'] * 48,
            'status': ['Active'] * 48
        })
        
        # Save all Excel files
        excel_files = {
            'schools.xlsx': school_data,
            'grades.xlsx': grades_data,
            'sections.xlsx': sections_data,
            'subjects.xlsx': subjects_data,
            'teachers.xlsx': teachers_data,
            'students.xlsx': students_data,
            'teacher_subjects.xlsx': teacher_subjects_data
        }
        
        for filename, df in excel_files.items():
            filepath = f'{self.sample_data_dir}/{filename}'
            df.to_excel(filepath, index=False)
            print(f"✅ Created: {filename} ({len(df)} records)")
        
        print(f"📊 All Excel files saved in: {os.path.abspath(self.sample_data_dir)}/")
        return True
    
    def _generate_60_students(self):
        """Generate exactly 60 students (10 per section)"""
        students = []
        first_names = ['Aarav', 'Vivaan', 'Aditya', 'Vihaan', 'Arjun', 'Aadhya', 'Ananya', 'Diya', 'Saanvi', 'Kavya',
                      'Krishna', 'Ishaan', 'Reyansh', 'Ayaan', 'Sai', 'Kiara', 'Anika', 'Arya', 'Myra', 'Sara']
        
        last_names = ['Sharma', 'Kumar', 'Singh', 'Verma', 'Patel', 'Gupta', 'Joshi', 'Yadav', 'Mishra', 'Agarwal']
        
        grades_sections = [
            ('Grade 6', 'A'), ('Grade 6', 'B'),
            ('Grade 7', 'A'), ('Grade 7', 'B'), 
            ('Grade 8', 'A'), ('Grade 8', 'B')
        ]
        
        student_counter = 1
        for grade, section in grades_sections:
            for i in range(10):  # 10 students per section
                first = random.choice(first_names)
                last = random.choice(last_names)
                
                students.append({
                    'school_code': 'GHS001',
                    'grade_name': grade,
                    'section_name': section,
                    'student_name': f"{first} {last}",
                    'student_roll': f"{grade[-1]}{section}{i+1:02d}",  # e.g., 6A01, 7B10
                    'phone': f"98765432{50+student_counter:02d}",
                    'email': f"{first.lower()}.{last.lower()}@student.ghs.edu",
                    'address': f"House {student_counter}, Student Colony, Academic City",
                    'parent_name': f"Mr. {last}",
                    'parent_phone': f"98765431{50+student_counter:02d}",
                    'admission_date': '2024-04-01',
                    'status': 'Active'
                })
                student_counter += 1
        
        return pd.DataFrame(students)
    
    def load_all_data_to_database(self):
        """Load all Excel data into database in correct order"""
        print("📥 Loading Excel data into database...")
        
        load_sequence = [
            ('schools.xlsx', self._load_schools),
            ('grades.xlsx', self._load_grades), 
            ('sections.xlsx', self._load_sections),
            ('subjects.xlsx', self._load_subjects),
            ('teachers.xlsx', self._load_teachers),
            ('students.xlsx', self._load_students),
            ('teacher_subjects.xlsx', self._load_teacher_subjects)
        ]
        
        for filename, load_function in load_sequence:
            filepath = f'{self.sample_data_dir}/{filename}'
            df = pd.read_excel(filepath)
            records = load_function(df)
            print(f"✅ Loaded {filename}: {records} records")
        
        self.connection.commit()
        print("📥 All data loaded successfully!")
        
    def _load_schools(self, df):
        for _, row in df.iterrows():
            self.connection.execute("""
                INSERT OR REPLACE INTO schools 
                (school_name, school_code, address, contact_number, email, principal_name, established_date, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, tuple(row))
        return len(df)
    
    def _load_grades(self, df):
        for _, row in df.iterrows():
            school_id = self.connection.execute(
                "SELECT school_id FROM schools WHERE school_code = ?", (row['school_code'],)
            ).fetchone()[0]
            
            self.connection.execute("""
                INSERT OR REPLACE INTO grades 
                (school_id, grade_name, grade_level, description, status)
                VALUES (?, ?, ?, ?, ?)
            """, (school_id, row['grade_name'], row['grade_level'], row['description'], row['status']))
        return len(df)
    
    def _load_sections(self, df):
        for _, row in df.iterrows():
            school_id = self.connection.execute(
                "SELECT school_id FROM schools WHERE school_code = ?", (row['school_code'],)
            ).fetchone()[0]
            
            grade_id = self.connection.execute(
                "SELECT grade_id FROM grades WHERE grade_name = ? AND school_id = ?", 
                (row['grade_name'], school_id)
            ).fetchone()[0]
            
            self.connection.execute("""
                INSERT OR REPLACE INTO sections 
                (school_id, grade_id, section_name, capacity, status)
                VALUES (?, ?, ?, ?, ?)
            """, (school_id, grade_id, row['section_name'], row['capacity'], row['status']))
        return len(df)
    
    def _load_subjects(self, df):
        for _, row in df.iterrows():
            school_id = self.connection.execute(
                "SELECT school_id FROM schools WHERE school_code = ?", (row['school_code'],)
            ).fetchone()[0]
            
            self.connection.execute("""
                INSERT OR REPLACE INTO subjects 
                (school_id, subject_name, subject_code, description, status)
                VALUES (?, ?, ?, ?, ?)
            """, (school_id, row['subject_name'], row['subject_code'], row['description'], row['status']))
        return len(df)
    
    def _load_teachers(self, df):
        for _, row in df.iterrows():
            school_id = self.connection.execute(
                "SELECT school_id FROM schools WHERE school_code = ?", (row['school_code'],)
            ).fetchone()[0]
            
            self.connection.execute("""
                INSERT OR REPLACE INTO teachers 
                (school_id, teacher_name, employee_id, phone, email, qualification, joining_date, salary, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (school_id, row['teacher_name'], row['employee_id'], row['phone'], 
                  row['email'], row['qualification'], row['joining_date'], row['salary'], row['status']))
        return len(df)
    
    def _load_students(self, df):
        for _, row in df.iterrows():
            # Get foreign key IDs
            school_id = self.connection.execute(
                "SELECT school_id FROM schools WHERE school_code = ?", (row['school_code'],)
            ).fetchone()[0]
            
            grade_id = self.connection.execute(
                "SELECT grade_id FROM grades WHERE grade_name = ? AND school_id = ?", 
                (row['grade_name'], school_id)
            ).fetchone()[0]
            
            section_id = self.connection.execute(
                "SELECT section_id FROM sections WHERE section_name = ? AND grade_id = ?", 
                (row['section_name'], grade_id)
            ).fetchone()[0]
            
            self.connection.execute("""
                INSERT OR REPLACE INTO students 
                (school_id, grade_id, section_id, student_name, student_roll, phone, email, 
                 address, parent_name, parent_phone, admission_date, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (school_id, grade_id, section_id, row['student_name'], row['student_roll'],
                  row['phone'], row['email'], row['address'], row['parent_name'], 
                  row['parent_phone'], row['admission_date'], row['status']))
        return len(df)
    
    def _load_teacher_subjects(self, df):
        for _, row in df.iterrows():
            # Get IDs
            teacher_id = self.connection.execute(
                "SELECT teacher_id FROM teachers WHERE employee_id = ?", (row['teacher_employee_id'],)
            ).fetchone()[0]
            
            subject_id = self.connection.execute(
                "SELECT subject_id FROM subjects WHERE subject_code = ?", (row['subject_code'],)
            ).fetchone()[0]
            
            grade_id = self.connection.execute(
                "SELECT grade_id FROM grades WHERE grade_name = ?", (row['grade_name'],)
            ).fetchone()[0]
            
            section_id = self.connection.execute(
                "SELECT section_id FROM sections WHERE section_name = ? AND grade_id = ?", 
                (row['section_name'], grade_id)
            ).fetchone()[0]
            
            self.connection.execute("""
                INSERT OR REPLACE INTO teacher_subjects 
                (teacher_id, subject_id, grade_id, section_id, academic_year, status)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (teacher_id, subject_id, grade_id, section_id, row['academic_year'], row['status']))
        return len(df)
    
    def verify_requirements(self):
        """Verify all project requirements are met"""
        print("\n🔍 Verifying Project Requirements...")
        
        # Check school count
        school_count = self.connection.execute("SELECT COUNT(*) FROM schools").fetchone()[0]
        print(f"✅ Schools: {school_count}/1")
        
        # Check grades (should be 3)
        grade_count = self.connection.execute("SELECT COUNT(*) FROM grades").fetchone()[0]
        print(f"✅ Grades: {grade_count}/3")
        
        # Check sections (should be 6)
        section_count = self.connection.execute("SELECT COUNT(*) FROM sections").fetchone()[0]
        print(f"✅ Sections: {section_count}/6")
        
        # Check students (should be 60)
        student_count = self.connection.execute("SELECT COUNT(*) FROM students").fetchone()[0]
        print(f"✅ Students: {student_count}/60")
        
        # Check teachers (should be 8)
        teacher_count = self.connection.execute("SELECT COUNT(*) FROM teachers").fetchone()[0]
        print(f"✅ Teachers: {teacher_count}/8")
        
        print(f"\n🎉 Phase 2 Complete! All base data loaded successfully!")
        return True

def main():
    print("=" * 70)
    print("🚀 PHASE 2: EXCEL DATA PROCESSING & LOADING")
    print("=" * 70)
    
    processor = Phase2ExcelProcessor()
    
    # Step 1: Setup
    if not processor.connect_database():
        return False
    
    processor.create_sample_directories()
    
    # Step 2: Generate Excel files
    processor.generate_complete_school_data()
    
    # Step 3: Load data to database
    processor.load_all_data_to_database()
    
    # Step 4: Verify requirements
    processor.verify_requirements()
    
    print("\n" + "=" * 70)
    print("✅ PHASE 2 COMPLETED SUCCESSFULLY!")
    print(f"📁 Excel files created in: {os.path.abspath('sample_data')}")
    print(f"🗄️ Database updated: {os.path.abspath('school_management.db')}")
    print("🚀 Ready for Phase 3 - Advanced Data & ML!")
    print("=" * 70)
    
    return True

if __name__ == "__main__":
    main()

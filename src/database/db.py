from src.database.config import supabase
import bcrypt
import httpx
import ssl
import time


def execute_with_retries(request, retries=5, delay=1):
    last_error = None
    for attempt in range(retries):
        try:
            return request.execute()
        except (httpx.ConnectError, httpx.ConnectTimeout, httpx.ReadTimeout, ssl.SSLError) as exc:
            last_error = exc
            if attempt == retries - 1:
                raise
            time.sleep(delay)

    raise last_error

def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

def check_pass(pwd, hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())


def check_teacher_exist(username):
    # Check  for unique username, returns true when username is already taken
    response = execute_with_retries(
        supabase.table("teachers").select("username").eq("username", username)
    )
    return len(response.data)

def create_teacher(username, password, name):
    data = {"username" : username, "password" : hash_pass(password), "name" : name}
    response = execute_with_retries(supabase.table("teachers").insert(data))
    return response.data

def teacher_login(username, password):
    response = execute_with_retries(
        supabase.table("teachers").select("*").eq("username", username)
    )
    if response.data: 
        teacher = response.data[0]
        if check_pass(password, teacher["password"]):
            return teacher

    return None

def get_all_students():
    response = execute_with_retries(supabase.table("students").select("*"))
    return response.data

def create_student(new_name, face_embedding=None, voice_embedding=None):
    data = {
        "name" : new_name,
        "face_embedding" : face_embedding,
        "voice_embedding" : voice_embedding
    }

    response = execute_with_retries(supabase.table("students").insert(data))
    return response.data

def create_subject(subject_code, name, section, teacher_id):
    data = {
        "subject_code" : subject_code,
        "name" : name,
        "section" : section,
        "teacher_id" : teacher_id
    }

    response = execute_with_retries(supabase.table("subjects").insert(data))
    return response.data

# AI function undestance this later
def get_teacher_subjects(teacher_id):
    response = execute_with_retries(supabase.table("subjects").select("*, subject_students(count), attendance_logs(timestamp)").eq("teacher_id", teacher_id))
    subjects = response.data

    for sub in subjects:
        sub["total_students"] = sub.get("subject_students", [{}])[0].get("count", 0) if sub.get("subject_students") else 0
        attendance = sub.get("attendance_logs", [])
        unique_sessions = len(set(log["timestamp"] for log in attendance))
        sub["total_classes"] = unique_sessions

        sub.pop("subject_student", None)
        sub.pop("attendance_logs", None)

    return subjects


def enroll_student_to_subject(student_id, subject_id):
    data = {
        "student_id" : student_id,
        "subject_id" : subject_id
        }

    response = execute_with_retries(supabase.table("subject_students").insert(data))
    return response.data


def unenroll_student_to_subject(student_id, subject_id):
    response = execute_with_retries(supabase.table("subject_students").delete().eq("student_id", student_id).eq("subject_id", subject_id))
    return response.data



def get_student_subjects(student_id):
    response = execute_with_retries(supabase.table("subject_students").select("*, subjects(*)").eq("student_id", student_id))
    return response.data


def get_student_attendance(student_id):
    response = execute_with_retries(supabase.table("attendance_logs").select("*, subjects(*)").eq("student_id", student_id))
    return response.data


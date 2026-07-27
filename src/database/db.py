from src.database.config import supabase
import bcrypt

def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

def check_teacher_exists(username):
    # Check  for unique username, returns true when username is already taken
    response = supabase.table("teachers").select("username").eq("username", username).execute(0)
    return len(response.data)

def create_teacher(username, password, name):
    data = {"username" : username, "password" : hash_pass(password), "name" : name}
    response = supabase.table("teachers").insert(data).execute()
    return response.data

def teacher_login(username, password):
    response = supabase.table("teachers").select("").eq("username", username).execute()
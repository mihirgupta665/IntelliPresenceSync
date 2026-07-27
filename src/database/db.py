from src.database.config import supabase
import bcrypt

def check_teacher_exists(username):
    # Check  for unique username, returns true when username is already taken
    response = supabase.table("teachers").select("username").eq("username", username).execute(0)
    return len(response.data)

def create_teacher(username, password, name):
    data = {"username" : username, "password" : hash_pass(password), "name" : name}
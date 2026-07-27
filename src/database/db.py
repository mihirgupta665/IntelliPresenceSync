from src.database.config import supabase
import bcrypt

def check_teacher_exists(username):
    # Check  for unique username, returns false when username is already taken
    response = supabase.table("teachers").select("username")
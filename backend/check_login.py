import os
import getpass
from dotenv import load_dotenv
from supabase import create_client


load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

client = create_client(url, key)

email = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")
response = client.auth.sign_in_with_password({"email": email, "password": password})

print(response.user.email)
print(response.session is not None)
print(client.table("projects").select("*").execute().data)


# client.table("projects").insert({"name": "From Python", "user_id": response.user.id}).execute()


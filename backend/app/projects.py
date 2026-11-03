from flask import Blueprint, request
from .supabase_client import create_supabase_client

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/api/projects')
def get_projects():
    auth_header = request.headers.get('Authorization')

    if auth_header is None or not auth_header.startswith('Bearer '):
        return { "error": "Missing Token"}, 401

    token = auth_header.split(' ', 1)[1]

    client = create_supabase_client()

    try:
        result = client.auth.get_user(token)
    except Exception:
        return { "error": "Invalid Token"}, 401

    client.postgrest.auth(token)
    projects_result = client.table("projects").select("*").execute()
    
    return { "user_id": result.user.id, "projects": projects_result.data }
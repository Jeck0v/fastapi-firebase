import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase app
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def signup_user(email: str, password: str):
    user = auth.create_user(
        email=email,
        password=password,
    )
    return user.uid

def login_user(email: str, password: str):
    try:
        # This will only verify the email, actual login logic would be managed by Firebase client SDK
        user = auth.get_user_by_email(email)
        return user.uid
    except auth.AuthError as e:
        raise ValueError(f"Failed to login: {str(e)}")

def verify_user_token(id_token: str):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token['uid']
    except auth.InvalidIdTokenError:
        raise ValueError("Invalid ID token")

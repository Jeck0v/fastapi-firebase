from fastapi import FastAPI, HTTPException
from models import AuthData, TokenData, UserResponse
from firebase import signup_user, login_user, verify_user_token

app = FastAPI()

@app.post("/signup", response_model=UserResponse)
async def signup(auth_data: AuthData):
    try:
        user_id = signup_user(auth_data.email, auth_data.password)
        return UserResponse(user_id=user_id, message="Signup successful")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/login", response_model=UserResponse)
async def login(auth_data: AuthData):
    try:
        user_id = login_user(auth_data.email, auth_data.password)
        return UserResponse(user_id=user_id, message="Login successful")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/me")
async def me(token_data: TokenData):
    try:
        user_id = verify_user_token(token_data.token)
        return {"user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

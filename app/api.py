from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

origins = [
    "https://dashboard-client-phi.vercel.app/",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#Create a Model
class User(BaseModel):
    id: str
    user_name: str
    model: str
    type: str
    usage: str
    rate: str
    spend: str
    date: str
 
users = []

@app.get('/users')
def get_users():
   return users

@app.post('/user')
def save_user(updatedUsers: List[User]):
    users.extend(updatedUsers)
    return users

@app.put('/user/{id}')
def update_user(id: str, update_user: User):
    for idx, user in enumerate(users):
        if user.id == id:
           users[idx] = update_user
           return users




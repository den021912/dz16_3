from fastapi import FastAPI,  Body


app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
def Users() -> dict:
    return users

@app.post('/user/{username}/{age}')
def create_message(username: str, message: str, age: int, user_id: int) -> str:
    current_index = str(int(max(users, key = int)) + 1)
    users[current_index] = message
    return f'User {user_id} is registered'

@app.put("/user/{user_id}/{username}/{age}")
def update_message(users: int, user_id: int, message: str = Body()) -> str:
    edit_message = users[user_id]
    edit_message.text = message
    return f'The user {user_id} is registered'

@app.delete("/user/{user_id}")
def delete_message(user_id: int) -> str:
    users.pop(user_id)
    return f"Message ID = {user_id} deleted"

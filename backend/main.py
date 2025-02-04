from fastapi import FastAPI, Request
import sqlite3

app = FastAPI()

# Подключение к базе данных
conn = sqlite3.connect("game.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, balance INTEGER, per_click INTEGER)")
conn.commit()

def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = cursor.fetchone()
    if not user:
        cursor.execute("INSERT INTO users (id, balance, per_click) VALUES (?, ?, ?)", (user_id, 0, 1))
        conn.commit()
        return (user_id, 0, 1)
    return user

@app.get("/get_balance/")
async def get_balance(user_id: str):
    user = get_user(user_id)
    return {"balance": user[1], "per_click": user[2]}

@app.post("/update_balance/")
async def update_balance(request: Request):
    data = await request.json()
    user_id, balance, per_click = data["user_id"], data["balance"], data["per_click"]
    cursor.execute("UPDATE users SET balance=?, per_click=? WHERE id=?", (balance, per_click, user_id))
    conn.commit()
    return {"status": "ok"}

# Запуск сервера
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

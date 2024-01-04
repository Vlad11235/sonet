# # метод для создания нового пользователя
# # def create_user(email: str, password: str, first_name: str, last_name: str):
# #     hashed_password = pwd_context.hash(password)
# #     client.execute(f"INSERT INTO users (email, password, first_name, last_name) VALUES ('{email}', '{hashed_password}', '{first_name}', '{last_name}')")

# # метод для получения информации о пользователе по email
# def get_user_by_email(email: str):
#     result = client.execute(f"SELECT * FROM users WHERE email='{email}'")
#     if len(result) == 0:
#         return None
#     return result[0]

# # метод для проверки пароля пользователя
# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# # метод для генерации токена доступа
# def create_access_token(data: dict, expires_delta: timedelta):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + expires_delta
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt
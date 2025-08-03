# import os
# from dotenv import load_dotenv

# load_dotenv()

# class Config:
#     # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://user:password@localhost/mogadishu_port')
#     SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/mogadishu_port"

#     JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super-secret-key')
#     # JWT_SECRET_KEY = SECRET_KEY
#     JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hour

# app/config.py

import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    JWT_SECRET_KEY = SECRET_KEY     # <- add this line
    SQLALCHEMY_DATABASE_URI = (
        os.getenv("DATABASE_URL")
        or "mysql+pymysql://root:password@localhost:3306/seaport_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

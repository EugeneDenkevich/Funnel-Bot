from dotenv import load_dotenv
import os


load_dotenv()


DB_PASS = os.getenv('DB_PASS')
DB_USER = os.getenv('DB_USER')
TOKEN_SENDER = os.getenv('TOKEN_SENDER')

EXPERT_URL = 'https://t.me/bo123t_test_test_bot'
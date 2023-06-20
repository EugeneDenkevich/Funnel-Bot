from dotenv import load_dotenv
import os


load_dotenv()


DB_PASS = os.getenv('DB_PASS')
DB_USER = os.getenv('DB_USER')
TOKEN_CLIENT = os.getenv('TOKEN_CLIENT')
EXPERT_URL = 'link/to/expert/profile/in/telegram'

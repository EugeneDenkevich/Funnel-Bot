# Funnel-Bot
This is a game funnel that implemented on Telegram platform.

### Used:
- Aiogram
- SQLAlchemy
- Telethon
- SQLite3
- APScheduler

### Done:
- Registration
- Logging in
- Logging out
- Parser and sender bots
- Client’s and admin’s parts

## Launching
Before lanching paste the necessary data in .env-example file
```bash
python -m venv .venv
pip install -r requirements.txt
cd .venv/Scripts
.\activate
cd ../..
cp .env.example .env
cd src
```
Next step you can start some bot that you need:
```bash
python admin.py
python client.py
python sender.py
```
Or you can alse parse some users from some group:
```bash
python parse.py
```
For client unit-testing:
```bash
python test_client.py
```

### Project in development.

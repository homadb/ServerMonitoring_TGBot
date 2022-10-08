<img src="https://github.com/homadb/ServerMonitoring_TGBot/blob/main/picture.jpg?raw=true" alt="Alt text">

# Server Monitoring Telegram Bot

SMTB is a Python script for monitoring your server and get report with telegram bot.
With SMTB you can checking your server on your smartphone.

### Create Telegram Bot
Create account on telegram and create a bot with @BotFather and get the token to 
access.

## Installation

Use the package manager `pip` to install `requirements.txt`

```bash
pip install -r requirements.txt
```

## Add Token
Edit the `.env` file and add your telegram bot token

## Run the Script
```python
python smtb.py
```
## Make the program auto-run
```bash
crontab -e
* * * * * $(which python3) /root/serverreporter/main.py >> ~/cron.log 2>&1
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss 
what you would like to change.


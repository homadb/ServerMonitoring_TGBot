
# Github: https://github.com/homadb
# Website: https://divband.com

import psutil
import subprocess
import os
import telebot
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start','help'])
def help(message):
    msg = '''
SMTB Manager
---------
1. Disk Usage → /disk
2. CPU and RAM Usage → /sysinfo
3. Uptime Server → /uptime
4. Server Description → /server
Help → /help

"github/homadb"
---------
    '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=['check'])
def check(message):
    bot.send_message(message.chat.id, "The server is alive")

@bot.message_handler(commands=['disk'])
def disk(message):
    diskTotal = int(psutil.disk_usage('/').total/(1024*1024*1024))
    diskUsed = int(psutil.disk_usage('/').used/(1024*1024*1024))
    diskAvail = int(psutil.disk_usage('/').free/(1024*1024*1024))
    diskPercent = psutil.disk_usage('/').percent

    msg = '''
Disk Info
---------
Total = {} GB
Used = {} GB
Avail = {} GB
Usage = {} %\n'''.format(diskTotal,diskUsed,diskAvail,diskPercent)
    bot.send_message(message.chat.id,msg)

@bot.message_handler(commands=['sysinfo'])
def sysinfo(message):
    cpuUsage = psutil.cpu_percent(interval=1)
    ramTotal = int(psutil.virtual_memory().total/(1024*1024)) #GB
    ramUsage = int(psutil.virtual_memory().used/(1024*1024)) #GB
    ramFree = int(psutil.virtual_memory().free/(1024*1024)) #GB
    ramUsagePercent = psutil.virtual_memory().percent
    msg = '''
CPU & RAM 
---------
CPU Usage = {} %
RAM
Total = {} MB
Usage = {} MB
Free  = {} MB
Used = {} %\n'''.format(cpuUsage,ramTotal,ramUsage,ramFree,ramUsagePercent)
    bot.send_message(message.chat.id,msg)

@bot.message_handler(commands=['uptime'])
def uptime(message):
    upTime = subprocess.check_output(['uptime','-p']).decode('UTF-8')
    msg = upTime
    bot.send_message(message.chat.id,msg)

@bot.message_handler(commands=['server'])
def server(message):
    uname = subprocess.check_output(['uname','-rsoi']).decode('UTF-8')
    host = subprocess.check_output(['hostname']).decode('UTF-8')
    ipAddr = subprocess.check_output(['hostname','-I']).decode('UTF-8')
    msg ='''
Server Desc
---------
OS = {}
Hostname = {} 
IP Addr = {}'''.format(uname,host,ipAddr)
    bot.send_message(message.chat.id,msg)

bot.polling()
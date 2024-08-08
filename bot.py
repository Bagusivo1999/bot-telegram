import telebot
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
from datetime import datetime

# Membuat file requirements.txt
with open("requirements.txt", "w") as file:
    file.write("telebot\n")
    file.write("watchdog\n")

# Menginstal dependensi dari requirements.txt
os.system("pip install -r requirements.txt")

# Replace 'YOUR_API_KEY' with your actual API key from BotFather
API_KEY = '7444819647:AAGXD1dWDlIkne4EdlKyRgJEZHyCvPtIpog'
bot = telebot.TeleBot(API_KEY)

# Get the bot's username
bot_info = bot.get_me()
BOT_USERNAME = bot_info.username

# Path to the files (adjust as necessary)
FILE_PATH = '/storage/emulated/0/ganas/hamster/hamster.php'
FILE_PATH1 = '/storage/emulated/0/ganas/pixel/pixel.php'
FILE_PATH2 = '/storage/emulated/0/ganas/tomarket/tomarket.php'
FILE_PATH3 = '/storage/emulated/0/blum/blum.py'
USER_ID_FILE = '/storage/emulated/0/ganas/anon/user_ids.txt'
PASSWORD_FILE = '/storage/emulated/0/ganas/anon/password.txt'

# Export user ID to a file
def export_user_id(user_id, username):
    if not os.path.exists(USER_ID_FILE):
        with open(USER_ID_FILE, 'w') as file:
            file.write(f'{user_id} {username}\n')
    else:
        with open(USER_ID_FILE, 'r') as file:
            existing_ids = file.read().splitlines()
        if str(user_id) not in existing_ids:
            with open(USER_ID_FILE, 'a') as file:
                file.write(f'{user_id} {username}\n')

# Mapping of English days to Indonesian
day_mapping = {
    'Monday': 'Senin',
    'Tuesday': 'Selasa',
    'Wednesday': 'Rabu',
    'Thursday': 'Kamis',
    'Friday': 'Jumat',
    'Saturday': 'Sabtu',
    'Sunday': 'Minggu'
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name
    bot.send_message(
        message.chat.id,
        f"Halo {username}\nID : {user_id} tap perintah dibawah ini untuk melihat list file\n\n/list"
    )
    print(f'\033[1;36mUser \033[1;33m{username} \033[1;34m{user_id} \033[1;32mGas Bot')
    export_user_id(user_id, username)

@bot.message_handler(commands=['list'])
def send_welcome(message):
    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name
    bot.send_message(
        message.chat.id,
        f"Hai {username}\nTap perintah dibawah ini untuk mendapatkan file\n\n1. /hamster\n2. /pixeltap\n3. /tomarket\n4. /blum"
    )
    print(f'\033[1;36mUser \033[1;33m{username} \033[1;34m{user_id} \033[1;32mGas Bot')

@bot.message_handler(commands=['hamster'])
def send_hamster_file(message):
    send_file(message, FILE_PATH, "Ini Dia Filenya Bang🔥")

@bot.message_handler(commands=['pixeltap'])
def send_pixeltap_file(message):
    send_file(message, FILE_PATH1, "Ini Dia Filenya Bang🔥")

@bot.message_handler(commands=['tomarket'])
def send_tomarket_file(message):
    send_file(message, FILE_PATH2, "Ini Dia Filenya Bang🔥")

@bot.message_handler(commands=['blum'])
def send_blum_file(message):
    send_file(message, FILE_PATH3, "Ini Dia Filenya Bang🔥")

def send_file(message, file_path, success_message):
    try:
        with open(file_path, 'rb') as file:
            bot.send_document(message.chat.id, file)
        bot.send_message(message.chat.id, success_message)
    except FileNotFoundError:
        bot.send_message(message.chat.id, "File not found. Please check the file path.")

@bot.message_handler(commands=['next'])
def search_new_partner(message):
    user_id = message.from_user.id
    bot.send_message(
        message.chat.id,
        f"Searching for a new partner...\n\nYour user ID: {user_id}"
    )

@bot.message_handler(commands=['password'])
def send_password(message):
    day_of_week = datetime.now().strftime('%A')  # Get the current day of the week
    day_in_indonesian = day_mapping.get(day_of_week, day_of_week)  # Map to Indonesian day
    try:
        with open(PASSWORD_FILE, 'r') as file:
            passwords = file.read().strip()
            if passwords:
                bot.send_message(message.chat.id, f"Password Hari {day_in_indonesian}: \n```\n{passwords}\n```", parse_mode='Markdown')
            else:
                bot.send_message(message.chat.id, "No password found in the file.")
    except FileNotFoundError:
        bot.send_message(message.chat.id, "Password file not found. Please check the file path.")
        
@bot.message_handler(func=lambda message: message.text in ['anjing', 'hai', 'tolol', 'oke','siapa saya?','siapa nama saya?','hehe','hehehe','wkwk','wkwkwk'])
def send_acak(message):
    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name
    if message.text == 'anjing':
        bot.send_message(message.chat.id, 'lu yang anjing')
    elif message.text == 'hai':
        bot.send_message(message.chat.id, f'halo {username} love you♥️ kiw kiw wkwkwk')
    elif message.text == 'tolol':
        bot.send_message(message.chat.id, 'lu yang tolol wkwk')
    elif message.text == 'oke':
        bot.send_message(message.chat.id, f'oke bro {username}')
    elif message.text == 'siapa saya?':
        bot.send_message(message.chat.id, f'kamu adalah adalah user bot ini dengan id {user_id}')
    elif message.text == 'siapa nama saya?':
        bot.send_message(message.chat.id, f'nama kamu {username}')
    elif message.text == 'hehe':
        bot.send_message(message.chat.id, 'hehe iya')
    elif message.text == 'hehehe':
        bot.send_message(message.chat.id, 'hehe iya')
    elif message.text == 'wkwk':
        bot.send_message(message.chat.id, 'wkwk')
    elif message.text == 'wkwkwk':
        bot.send_message(message.chat.id, 'wkwk')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name
    bot.send_message(message.chat.id, f"Hallo {username} [{message.text}] tidak ada dalam perintah!!\nTap /start untuk memulai")
    print(f'\033[1;36mUser \033[1;33m{username} \033[1;34m{user_id} \033[1;32mspam')

# Function to start the file observer in a separate thread
def start_file_observer():
    observer = Observer()
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Start the file observer in a separate thread
threading.Thread(target=start_file_observer, daemon=True).start()

bot.polling(none_stop=True, interval=1)

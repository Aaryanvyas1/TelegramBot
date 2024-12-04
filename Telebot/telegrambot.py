import telebot
import csv
import webbrowser

Token = "8073459577:AAF42t9fgT9T7TXWw-1Ovk1AAynE6fKxqYU"
bot = telebot.TeleBot(Token)

def load_game_links(filename):
    game_links = {}
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            game_links[row['name']] = row['link']
    return game_links

glinks = load_game_links('games.csv')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to the Gaming Bot! Enter what game you would like to download.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, """Available commands:
/start - Greetings from the bot
/help - Help on how to use the bot
<name of the game> - Enter the name of the game you want to download.""")

@bot.message_handler(func=lambda message: True)
def custom(message):
    gname = message.text.strip()  
    
    if gname in glinks:
        bot.reply_to(message, f"Here is your link: {glinks[gname]}")
    else:
        bot.reply_to(message, "Sorry, I don't have a link for that game.")

bot.polling()
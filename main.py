import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot("7510465141:AAFTaxGZsTpRxyD8P6D5a3gaB0x3HHJ7taI") 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username, message.from_user.id)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
        bot.send_message(message.chat.id, pokemon.get_level())
        
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")


bot.infinity_polling(none_stop=True)


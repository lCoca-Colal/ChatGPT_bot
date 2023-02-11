import openai
import telebot

# Initialize the OpenAI API client with your API key
openai.api_key = "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"

# Initialize the Telegram Bot API client with your API key
bot = telebot.TeleBot("6114676979:AAFGodfKCvqZRCERkO8rAPcXW1Et3tNu0oI")

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(chat_id=message.chat.id, text="Hi there! I'm a bot that can answer questions using OpenAI. How can I help you today?")

@bot.message_handler(content_types=['text'])
def text_handler(message):
    # Get the user's message
    user_message = message.text

    # Use OpenAI's API to generate a response to the user's message
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="Answer the following question: " + user_message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text

    bot.send_message(chat_id=message.chat.id, text=response)

# Start the bot
bot.polling()
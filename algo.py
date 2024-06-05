from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram Bot Token
TOKEN = "7323141793:AAHbGgPfOEmmLUnMe-7I9X5MPjuhqiAfxYQ"

# Welcome message
welcome_message = """
Hello sir ✳️

Welcome to the Stake Payment Gateway! 🧲

💠 Get your Premium Bot 🤖 License Key 🔐

🌟 Bot Price: $487

For contact and support, please reach out to us through this channel. We're here to assist you every step of the way! 🤝

Now, let's proceed with the payment:

💳 Payment Method:

Credit/Debit Card 💳
PayPal 💸
Cryptocurrency 💰
Bank Transfer 🏦

Simply select your preferred payment method, and we'll guide you through the rest!
"""

# Handler for /start command
def start(update: Update, context: CallbackContext) -> None:
    # Send the welcome message with the inline keyboard
    keyboard = [
        [InlineKeyboardButton("Credit/Debit Card 💳", callback_data='card')],
        [InlineKeyboardButton("PayPal 💸", callback_data='paypal')],
        [InlineKeyboardButton("Cryptocurrency 💰", callback_data='crypto')],
        [InlineKeyboardButton("Bank Transfer 🏦", callback_data='bank')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(welcome_message, reply_markup=reply_markup)

# Handler for inline keyboard button
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    # Handle different button clicks
    if query.data == 'card' or query.data == 'paypal' or query.data == 'crypto' or query.data == 'bank':
        # Send the next message after clicking payment method button
        query.message.reply_text("Please select your preferred payment method.")
        # Adding QR and UPI ID buttons
        keyboard = [
            [InlineKeyboardButton("QR", callback_data='qr')],
            [InlineKeyboardButton("UPI ID", callback_data='upi')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_text("Choose one of the options below:", reply_markup=reply_markup)

    elif query.data == 'qr':
        # Send QR image
        query.message.reply_photo(open('QR.jpg', 'rb'))
        # Send the payment completion message
        send_payment_completion_message(update.message.chat_id)

    elif query.data == 'upi':
        # Send UPI ID
        query.message.reply_text("Our UPI ID: 9370162316@paytm")
        # Send the payment completion message
        send_payment_completion_message(update.message.chat_id)

def send_payment_completion_message(chat_id):
    # Send payment completion message
    message = """
    Congratulations on completing your payment! 🎉

    To receive your premium bot, please take a screenshot of the payment confirmation and share it with us here. 
    Once we verify your payment, we'll send you the user ID and the link to access your premium bot!

    Thank you for choosing Stake Payment Gateway. We're excited to have you onboard and look forward to providing you with top-notch service!
    """
    context.bot.send_message(chat_id=chat_id, text=message)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Handler for /start command
    dp.add_handler(CommandHandler("start", start))

    # Handler for inline keyboard button
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

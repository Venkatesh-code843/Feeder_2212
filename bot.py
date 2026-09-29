from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = "8967868116:AAHTdGVKWzDeV00MOJRtDtTO_pRj7Zo2WZ8"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I'm your Instagram content bot."
    )


async def follow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "Usage: /follow @username"
        )
        return

    username = context.args[0]

    await update.message.reply_text(
        f"I received the username: {username}"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("follow", follow))

    app.run_polling()


if __name__ == "__main__":
    main()

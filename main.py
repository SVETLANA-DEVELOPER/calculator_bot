from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
    ConversationHandler
)
from config import BOT_TOKEN
from commands import (
    start_command,
    ops_select,
    num_a_input,
    reply_num_a_input,
    reply_num_b_input,
    cancel_command
)
from config import (
    OP_BUTTON_STATE,
    NUM_A_INPUT_STATE,
    REPLY_NUM_A_STATE,
    REPLY_NUM_B_STATE,
    RESTART_STATE,
)


def main() -> None:
    """Run the bot"""
    updater = Updater(BOT_TOKEN)

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start_command)],
        states={
            OP_BUTTON_STATE: [CallbackQueryHandler(ops_select)],
            NUM_A_INPUT_STATE: [CallbackQueryHandler(num_a_input)],
            REPLY_NUM_A_STATE: [MessageHandler(Filters.text, reply_num_a_input)],
            REPLY_NUM_B_STATE: [MessageHandler(Filters.text, reply_num_b_input)],
            RESTART_STATE: [CommandHandler('start', start_command)],
        },
        fallbacks=[CallbackQueryHandler('cancel', cancel_command)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()

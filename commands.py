from telegram import ReplyKeyboardRemove, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
from config import (
    data,
    OP_BUTTON_STATE,
    NUM_A_INPUT_STATE,
    REPLY_NUM_A_STATE,
    REPLY_NUM_B_STATE,
    RESTART_STATE,

)


def start_command(update: Update, context: CallbackContext) -> int:
    # отобразить клавиатуру
    kb = [
        [InlineKeyboardButton("Операции с R числами", callback_data="real_nums")],
        [InlineKeyboardButton("Операции с C числами", callback_data="complex_nums")],
    ]

    reply_markup = InlineKeyboardMarkup(kb)
    update.message.reply_text("Выберите действие", reply_markup=reply_markup)

    return OP_BUTTON_STATE


def ops_select(update: Update, context: CallbackContext) -> int:
    num_type_str = update.callback_query.data    # real_nums или complex_nums
    data["num_type"] = float if num_type_str == "real_nums" else complex

    kb = [
        [InlineKeyboardButton("a + b", callback_data="+")],
        [InlineKeyboardButton("a - b", callback_data="-")],
    ]

    # отобразим клавиатуру
    reply_markup = InlineKeyboardMarkup(kb)
    update.callback_query.message.edit_text("Выберите операцию:", reply_markup=reply_markup)

    return NUM_A_INPUT_STATE


def num_a_input(update: Update, context: CallbackContext) -> int:
    data["op"] = update.callback_query.data

    update.callback_query.message.edit_text("Введите число A:")
    return REPLY_NUM_A_STATE


def reply_num_a_input(update: Update, context: CallbackContext) -> int:
    data["num_a"] = update.message.text.replace(" ", "")

    update.message.reply_text("Введите число B:")
    return REPLY_NUM_B_STATE


def reply_num_b_input(update: Update, context: CallbackContext) -> int:
    data["num_b"] = update.message.text.replace(" ", "")

    result = get_result()

    update.message.reply_text(f"Результат вычисления: {result}")
    update.message.reply_text(f"Наберите /start для запуска")

    return RESTART_STATE


def get_result():
    result = 0
    num_a = data["num_type"](data["num_a"])
    num_b = data["num_type"](data["num_b"])

    if data["op"] == "+":
        result = num_a + num_b
    elif data["op"] == "-":
        result = num_a - num_b

    return result


def cancel_command(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'Нажмите /start, чтобы сделать еще вычисление.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END

# токен бота
BOT_TOKEN = "5423907310:AAGImbekFyoo3x2RPcnTYeXQZIYq-QzVZo8"

# глобальные константы хранят состояние
(
    OP_BUTTON_STATE,
    NUM_A_INPUT_STATE,
    REPLY_NUM_A_STATE,
    REPLY_NUM_B_STATE,
    RESTART_STATE,
) = range(5)

data = {
    "num_a": 0,
    "num_b": 0,
    "op": "",
    "num_type": float
}

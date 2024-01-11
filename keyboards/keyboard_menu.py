from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


class SetNumberKey:
    first_set = InlineKeyboardButton(text='1',
                                      callback_data='1')
    second_set = InlineKeyboardButton(text='2',
                                     callback_data='2')
    third_set = InlineKeyboardButton(text='3',
                                            callback_data='3')
    fourth_set = InlineKeyboardButton(text='4',
                                            callback_data='4')
    fifth_set = InlineKeyboardButton(text='5',
                                            callback_data='5')
    keyboard: list[list[InlineKeyboardButton]] = [[first_set, second_set, third_set],
                                                  [fourth_set, fifth_set]]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)


class SizeKey:
    s_size = InlineKeyboardButton(text='S',
                                      callback_data='S')
    m_size = InlineKeyboardButton(text='M',
                                     callback_data='M')
    l_size = InlineKeyboardButton(text='L',
                                            callback_data='L')
    keyboard: list[list[InlineKeyboardButton]] = [[s_size, m_size, l_size]]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)


class PayKey:
    cash = InlineKeyboardButton(text='Наличными', callback_data='cash')
    card = InlineKeyboardButton(text='Картой', callback_data='card')
    transfer = InlineKeyboardButton(text='Перевод', callback_data='transfer')
    keyboard = [[cash], [card], [transfer]]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)


# class BasedKey:
#     b1 = KeyboardButton(text='Точно да', callback_data='1')
#     b2 = KeyboardButton(text='Скорее да', callback_data='2')
#     b3 = KeyboardButton(text='Скорее нет', callback_data='3')
#     b4 = KeyboardButton(text='Точно нет', callback_data='4')
#     b5 = KeyboardButton(text='Точно да', callback_data='0')
#
#     keyboard = ReplyKeyboardMarkup(keyboard=[[b1], [b2], [b3], [b4], [b5]], resize_keyboard=True)


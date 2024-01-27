from aiogram import Bot, Dispatcher
from aiogram.filters import Command, StateFilter, Text
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)
import os
from keyboards.keyboard_menu import SetNumberKey, SizeKey, PayKey, ColorKey, BasketKey
from lexicon.lexicon_ru import welcome_text, byby_text
from models import methods as mt
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

bot: Bot = Bot(os.environ.get('TOKEN'))
dp: Dispatcher = Dispatcher()
user_dict = {}


class Question(StatesGroup):
    starting = State()
    set_nubmer = State()
    color = State()
    size = State()
    amount_set = State()
    basket = State()
    promocode = State()
    deliv_adress = State()
    delive_time = State()
    contact_number = State()
    pay_way = State()
    comments = State()


@dp.message(Command(commands='start'), StateFilter(default_state))
async def starting_comm(msg: Message, state: FSMContext):
    await msg.answer(text=welcome_text)
    await state.set_state(Question.starting)


@dp.message(Command(commands='goods'), StateFilter(Question.starting))
async def goods_starting(msg: Message, state: FSMContext):
    await msg.answer(text='Это первая модель товара в различных цветах \n' \
                     '*тут какое то описание товара*')
    await msg.answer_photo(mt.Photos.photo_pinguin_1, caption='Название цвета 1')
    await msg.answer_photo(mt.Photos.photo_pinguin_2, caption='Название цвета 2')
    await msg.answer_photo(mt.Photos.photo_pinguin_3, caption='Название цвета 3')
    await msg.answer_photo(mt.Photos.photo_pinguin_4, caption='Название цвета 4')
    await msg.answer(text='Это вторая модель товара в различных цветах \n' \
                     '*тут какое то описание товара*')
    await msg.answer_photo(mt.Photos.photo_capybara_1, caption='Название цвета 1')
    await msg.answer_photo(mt.Photos.photo_capybara_2, caption='Название цвета 2')
    await msg.answer_photo(mt.Photos.photo_capybara_3, caption='Название цвета 3')
    await msg.answer_photo(mt.Photos.photo_capybara_4, caption='Название цвета 4')
    await msg.answer(text='Что-то понравилось? \n Скорее вводи /poll и делай заказ')
    


@dp.message(Command(commands='poll'), StateFilter(Question.starting))
async def polling_starting(msg: Message, state: FSMContext):
    user_dict[msg.from_user.id] = {}
    user_dict[msg.from_user.id]['basket'] = []
    await msg.answer(text='Выберите, пожалуйста, номер модели', reply_markup=SetNumberKey.markup)
    await state.set_state(Question.set_nubmer)


@dp.message(Command(commands='poll'), StateFilter(default_state))
async def polling_starting(msg: Message, state: FSMContext):
    user_dict[msg.from_user.id] = {}
    user_dict[msg.from_user.id]['basket'] = []
    await msg.answer(text='Выберите, пожалуйста, номер модели', reply_markup=SetNumberKey.markup)
    await state.set_state(Question.set_nubmer)


@dp.callback_query(StateFilter(Question.basket), Text(text=['add']))
async def polling_starting(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Выберите, пожалуйста, номер модели', reply_markup=SetNumberKey.markup)
    await state.set_state(Question.set_nubmer)


@dp.callback_query(StateFilter(Question.set_nubmer), Text(text=['1', '2', '3', '4', '5']))
async def do_you_like(callback: CallbackQuery, state: FSMContext):
    #await state.update_data(set_number=callback.data)
    user_dict[callback.from_user.id]['basket'].append(callback.data)
    print(user_dict)
    await callback.message.edit_text(text='Теперь выберите нужный цвет',
                                  reply_markup=ColorKey.markup)
    await state.set_state(Question.color)


@dp.callback_query(StateFilter(Question.color), Text(text=['color1', 'color2', 'color3', 'color4']))
async def do_you_like(callback: CallbackQuery, state: FSMContext):
    #await state.update_data(color=callback.data)
    user_dict[callback.from_user.id]['basket'].append(callback.data)
    print(user_dict)
    await callback.message.edit_text(text='Теперь выберите нужный размер',
                                  reply_markup=SizeKey.markup)
    await state.set_state(Question.size)


@dp.callback_query(StateFilter(Question.size), Text(text=['S', 'M', 'L']))
async def cooking_time(callback: CallbackQuery, state: FSMContext):
    #await state.update_data(size=callback.data)
    user_dict[callback.from_user.id]['basket'].append(callback.data)
    print(user_dict)
    await callback.message.edit_text(text='Сколько данных комплектов вам нужно?',
                                     reply_markup=SetNumberKey.markup)
    await state.set_state(Question.amount_set)


@dp.callback_query(StateFilter(Question.amount_set), Text(text=['1', '2', '3', '4', '5']))
async def basket_need(callback: CallbackQuery, state: FSMContext):
    #await state.update_data(amount_set=callback.data)
    user_dict[callback.from_user.id]['basket'].append(callback.data)
    print(user_dict)
    await callback.message.edit_text(text='корзина дальше?', reply_markup=BasketKey.markup)
    await state.set_state(Question.basket)


@dp.callback_query(StateFilter(Question.basket), Text(text=['continue']))
async def she_know(callback: CallbackQuery, state: FSMContext):
    #await state.update_data(amount_set=callback.data)
    #user_dict[callback.from_user.id]['basket'].append(callback.data)
    print(user_dict)   
    await callback.message.edit_text(text='Введите промокод при наличии или слово нет')
    await state.set_state(Question.promocode)


@dp.message(StateFilter(Question.promocode))
async def gender_reveal(msg: Message, state: FSMContext):
    #await state.update_data(promocode=msg.text)
    user_dict[msg.from_user.id]['promocode'] = msg.text
    print(user_dict)
    await msg.answer(text='Введите адрес доставки')
    await state.set_state(Question.deliv_adress)


@dp.message(StateFilter(Question.deliv_adress))
async def age_rev(msg: Message, state: FSMContext):
    #await state.update_data(deliv_adress=msg.text)
    user_dict[msg.from_user.id]['deliv_adress'] = msg.text
    print(user_dict)
    await msg.answer(text='Напишите желаемую дату и время доставки')
    await state.set_state(Question.delive_time)


@dp.message(StateFilter(Question.delive_time))
async def age_rev(msg: Message, state: FSMContext):
    #await state.update_data(delive_time=msg.text)
    user_dict[msg.from_user.id]['delive_time'] = msg.text
    print(user_dict)
    await msg.answer(text='Укажите ваш контактный номер телефона')
    await state.set_state(Question.contact_number)


@dp.message(StateFilter(Question.contact_number))
async def comment_from_user(msg: Message, state: FSMContext):
    #await state.update_data(contact_number = msg.text)
    user_dict[msg.from_user.id]['contact_number'] = msg.text
    print(user_dict)
    await msg.answer('Еcли у вас есть коомментарии к заказу, пожайлуйста, укажите их или напишите "нет"')
    await state.set_state(Question.comments)


@dp.message(StateFilter(Question.comments))
async def age_rev(msg: Message, state: FSMContext):
    #await state.update_data(comments=msg.text)
    user_dict[msg.from_user.id]['comments'] = msg.text
    print(user_dict)
    await msg.answer(text='Выберите желаемый способ оплаты', reply_markup=PayKey.markup)
    await state.set_state(Question.pay_way)


@dp.callback_query(StateFilter(Question.pay_way), Text(text=['cash', 'card', 'transfer']))
async def process_age_sent(callback: CallbackQuery, state: FSMContext):
    #await state.update_data(pay_way=callback.data)
    user_dict[callback.from_user.id]['pay_way'] = callback.data
    print(user_dict)
    await callback.message.answer(byby_text)
    await callback.message.delete()
    await bot.send_message(chat_id='395890972', text=mt.send_result(user_dict, callback.from_user.id))
    del user_dict[callback.from_user.id]
    #user_dict[callback.from_user.id] = await state.get_data()
    #print(user_dict)
    await state.clear()


if __name__ == '__main__':


    dp.run_polling(bot)

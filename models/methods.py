from aiogram.types.input_file import FSInputFile


def baket_unpacker(basket_list: list):
    res = ''
    res += f""" Номер комплекта: {basket_list[0]}
Название цвета: {basket_list[1]}
Размер: {basket_list[2]}
Количество: {basket_list[3]}
"""
    return res

def big_basket_unpacker(basket_list: list):
    res = ''
    for i in range(len(basket_list)// 4):
        new_basket = basket_list[i:i+4]
        res += '\n' + baket_unpacker(new_basket)
    return res



def send_result(user_dict: dict, user_id):
    res_msg = f"""Поступил заказ от пользователя {user_id}
                Корзина: {big_basket_unpacker(user_dict[user_id]['basket'])}
                Контактный номер: {user_dict[user_id]['contact_number']}
                Промокод: {user_dict[user_id]['promocode']}
                Адрес доставки: {user_dict[user_id]['deliv_adress']}
                Желаемое время доставки: {user_dict[user_id]['delive_time']}
                Способ оплаты: {user_dict[user_id]['pay_way']}
                Комментарии пользователя: {user_dict[user_id]['comments']}
                """
    return res_msg


class Photos:
    photo_pinguin_1 = FSInputFile("models/img/pinguin1.jpg")
    photo_pinguin_2 = FSInputFile("models/img/pinguin2.jpg")
    photo_pinguin_3 = FSInputFile("models/img/pinguin3.jpg")
    photo_pinguin_4 = FSInputFile("models/img/pinguin4.jpg")
    photo_capybara_1 = FSInputFile("models/img/capybara1.jpg")
    photo_capybara_2 = FSInputFile("models/img/capybara2.jpg")
    photo_capybara_3 = FSInputFile("models/img/capybara3.jpg")
    photo_capybara_4 = FSInputFile("models/img/capybara4.jpg")


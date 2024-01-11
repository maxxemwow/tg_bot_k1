def send_result(user_dict: dict, user_id):
    res_msg = f"""Поступил заказ от пользователя {user_id}
                Контактный номер: {user_dict[user_id]['contact_number']}
                Номер комплекта: {user_dict[user_id]['set_nubmer']}
                Размер: {user_dict[user_id]['size']}
                Количество: {user_dict[user_id]['amount_set']}
                Промокод: {user_dict[user_id]['promocode']}
                Адрес доставки: {user_dict[user_id]['deliv_adress']}
                Желаемое время доставки: {user_dict[user_id]['delive_time']}
                Способ оплаты: {user_dict[user_id]['pay_way']}
                Комментарии пользователя: {user_dict[user_id]['comments']}
                """
    return res_msg

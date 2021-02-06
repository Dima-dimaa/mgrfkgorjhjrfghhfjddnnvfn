import vk_api, requests, threading, fake_useragent
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor




keyboard = VkKeyboard(one_time=False)
# 1
keyboard.add_button('Звонок 📞', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Идея 💡', color=VkKeyboardColor.PRIMARY)
keyboard.add_line()
keyboard.add_button('Не работает ⛔', color=VkKeyboardColor.PRIMARY)
keyboard.add_button('Поддержка 👤', color=VkKeyboardColor.PRIMARY)
clava2 = VkKeyboard(one_time=False)
clava2.add_button('Назад ↩', color=VkKeyboardColor.SECONDARY)
clava3 = VkKeyboard(one_time=False)
clava3.add_button('Назад ↩', color=VkKeyboardColor.SECONDARY)
clava4 = VkKeyboard(one_time=False)
clava4.add_button('Назад ↩', color=VkKeyboardColor.SECONDARY)


def check(x):
    file = open('baza.txt', 'r', encoding='utf-8')
    if str(x) in file.read():
        return 1
    else:
        return 0
    file.close()


def adder(x):
    file = open('baza.txt', 'a', encoding='utf-8')
    file.write(f'{x}\n')

    file.close()


UsersId = open("baza.txt", "r")
UsersId2 = set()
for line in UsersId:
    UsersId2.add(line.strip())
UsersId.close()

suser = []
for user in UsersId2:
    suser.append(str(user))


def extract_arg(arg):
    return arg.split()[1]


def extract_arg2(arg2):
    return arg2.split()[2]

def write_message(sender, message):
    if i == 1:
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                           'keyboard': keyboard.get_keyboard()})
    if i == 2:
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                           'keyboard': clava2.get_keyboard()})
    if i == 3:
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                           'keyboard': clava3.get_keyboard()})
    if i == 4:
        authorize.method('messages.send', {'user_id': sender, 'message': message, "random_id": get_random_id(),
                                           'keyboard': clava4.get_keyboard()})


def rass(soob, xui, govno, jopa):
    if 1 == 1:
        UsersId = open("baza.txt", "r")
        UsersId2 = set()
        for line in UsersId:
            UsersId2.add(line.strip())
        UsersId.close()
        suser = []
        for user in UsersId2:
            suser.append(str(user))
        if a == 1:
            succes = 0
            fail = 0
            for user in suser:
                try:
                    i = 1
                    write_message(int(user), sms)
                    succes += 1
                except:
                    fail += 1
                    continue
            so_ob = "none"
            write_message("574170405", "Рассылку получило - " + str(succes) + " пользователей")
            write_message("574170405", "Заблокировали бота - " + str(fail) + " пользователей")



token = "6a5ba947316894f5718f7d107ce473ce6276b726f5333eb096b08b5bdb9009e3e779fbbcd2c38fc21d358"
authorize = vk_api.VkApi(token=token)
longpoll = VkLongPoll(authorize)
admin = [574170405]
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        try:
            a = open(str(event.user_id) + "c.txt", "r")
            a.close()
        except:
            a = open(str(event.user_id) + "c.txt", "w")
            a.write("1")
            a.close()
        with open(str(event.user_id) + "c.txt", "r") as ca:
            i = ca.read()
            i = int(i)
        reseived_message = event.text.lower()
        sender = event.user_id
        user = authorize.method("users.get", {"user_ids": event.user_id})  # вместо 1 подставляете айди нужного юзера
        name = user[0]['first_name']
        if reseived_message == 'начать' \
                or reseived_message == 'привет' \
                or reseived_message == 'ку' \
                or reseived_message == 'хай' \
                or reseived_message == 'здравствуйте' \
                or reseived_message == 'дарова':
            if check(sender) == 0:
                adder(sender)
            a = open(str(sender) + "c.txt", "w")
            a.write("1")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, "Привет, " + name + "! \nРады видеть тебя в нашей группе 😊")
            write_message(sender, "Выбери:")
        elif reseived_message[0:6] == 'звонок' and i == 1:
            a = open(str(sender) + "c.txt", "w")
            a.write("2")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, "Введите номер:")
        elif reseived_message[0:9] == 'поддержка' and i == 1:
            a = open(str(sender) + "c.txt", "w")
            a.write("4")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, "Опишите вашу проблему 🤔")
        elif reseived_message[0:4] == 'идея' and i == 1:
            a = open(str(sender) + "c.txt", "w")
            a.write("3")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, 'Если у вас есть идея по улучшению нашей группы к примеру: \nЯ знаю ещё сервера по отправке звонков '
                                  '\n"И пишите сервера (Сайты)"')
        elif reseived_message[0:11] == 'не работает' and i == 1:
            write_message(sender, "Если звонок не приходит значит есть 2 причины: \n1. Номер не является Российским \n2. "
                                  "Вы слишком часто его используете !!! \nНомер пишится с 7 и состоит из 11 - цифр !!!")
            write_message(sender, "Выбери:")
        elif reseived_message[0:5] == 'назад' and i == 2 or \
            reseived_message[0:5] == 'назад' and i == 3 or \
            reseived_message[0:5] == 'назад' and i == 4:
            a = open(str(sender) + "c.txt", "w")
            a.write("1")
            a.close()
            with open(str(event.user_id) + "c.txt", "r") as ca:
                i = ca.read()
                i = int(i)
            write_message(sender, "Выбери:")
        elif reseived_message[0:2] == "79" and len(reseived_message) == 11 and i == 2:
            phone = reseived_message
            try:
                s = requests.Session()
                s.proxies.update({'http': 'http://195.46.124.94'})
                s.post("https://nn-card.ru/api/1.0/register", json={"phone": phone, "password": '52883456'},)
                a = open(str(sender) + "c.txt", "w")
                a.write("1")
                a.close()
                with open(str(event.user_id) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, "Звонок отправлен ✅")
            except:
                a = open(str(sender) + "c.txt", "w")
                a.write("1")
                a.close()
                with open(str(event.user_id) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(sender, "Звонок не был отправлен ⛔")
        elif reseived_message[0:8] == "рассылка":
            if sender == 574170405:
                a = 0
                try:
                    sm = extract_arg(event.text)
                    a = 1
                except:
                    write_message(event.user_id, "Вы не указали текст для рассылки")
                if a == 1:
                    i = 1
                    write_message(event.user_id, "Рссылка началась")
                    sms = event.text[8:]
                    so_ob = sms
                    t = threading.Thread(target=rass, args=(sms, 1, 2, 3))
                    t.start()
            else:
                write_message(sender, 'Вы не являетесь администратором !!!')
        else:
            if i == 3:
                a = open(str(sender) + "c.txt", "w")
                a.write("1")
                a.close()
                with open(str(event.user_id) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                userr = authorize.method("users.get", {"user_ids": sender})
                fullname = user[0]['first_name'] + ' ' + userr[0]['last_name']
                write_message(sender, "Спасибо за идею ☺ \nНаш администратор обязательно рассмотрит её 🙃")
                write_message(574170405, f'Есть идея !!! \nПользователь: [https://vk.com/id{sender}|{fullname}] \nЧат https://vk.com/gim201840643?sel={sender}')
            elif i == 4:
                a = open(str(sender) + "c.txt", "w")
                a.write("1")
                a.close()
                with open(str(event.user_id) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                userr = authorize.method("users.get", {"user_ids": sender})
                fullname = user[0]['first_name'] + ' ' + userr[0]['last_name']
                write_message(sender, "Ожидайте ответ в течении суток 🕐")
                with open(str(event.user_id) + "c.txt", "r") as ca:
                    i = ca.read()
                    i = int(i)
                write_message(574170405,
                              f'Нужна помощь !!! \nПользователь: [https://vk.com/id{sender}|{fullname}] \nЧат https://vk.com/gim201840643?sel={sender}')
            elif i == 2:
                write_message(sender, "Номер введён не верно !!! \n\nПример: 79283335522")
            else:
                write_message(sender, "Ты в главном меню, для продолжения воспользуйся командами: \n\n- Звонок\n- Идея\n- Не работает\n- Поддержка")

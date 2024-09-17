def send_email(message, recipient, *, sender="university.help@gmail.com"):

    # Проверка корректности email (наличие @ и окончание на .com, .ru, .net)
    valid_endings = (".com", ".ru", ".net")
    if "@" not in recipient or not recipient.endswith(valid_endings) or "@" not in sender or not sender.endswith(
            valid_endings):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return

    # Проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # Проверка на отправителя по умолчанию
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

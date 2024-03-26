from instagrapi import Client

import time

accounts = []
follows = []

with open("./accounts.txt", "r") as accounts_file:
    accounts_data = accounts_file.readlines()
    accounts_data = list(map(str.strip, accounts_data))

    for account in accounts_data:
        account = account.split(":")

        accounts.append({
            "login": account[0],
            "password": account[1]
        })

with open("./follows.txt", "r") as follows_file:
    follows = follows_file.readlines()
    follows = list(map(str.strip, follows))

def info_message(user, text):
    print(f"[{user}] {text}")


try:
    for account in accounts:
        try:

            user = Client()

            user_login = account.get("login")
            user_password = account.get("password")

            user.login(username=user_login, password=user_password)

            info_message(user_login, f"Авторизовались под пользователям: {user.username}")
            info_message(user_login, f"Начинаем подписку")

            for follow in follows:
                try:
                    user_id = user.user_id_from_username(follow)
                    user.user_follow(user_id)

                    info_message(user_login, f"Подписались на: {follow}")
                except Exception as e:
                    info_message(user_login, f"Ошибка при попытке подписке на профиль ({follow}), продолжаем работу: {e}")
                    continue

            user.logout()
            time.sleep(500)

        except Exception as e:
            info_message(user_login, f"Ошибка продолжаем работу! : {e}")
            continue

except Exception as e:
    print(f"Глобальная ошибка! : {e}")

import datetime as dt
import pandas
import smtplib
import random

USER = "cejicsasa17@gmail.com"
PASSWORD = "YOUR_APP_PASSWORD"

def send_greeting_card(birthday):
    file_number = random.randint(1,3)
    with open(file=f"letter_templates/letter_{file_number}.txt", mode="r") as file:
        letter = file.read().replace("[NAME]", birthday["name"])

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        connection.sendmail(
            from_addr=USER,
            to_addrs=birthday["email"],
            msg="Subject:Happy Birthday\n\n"
                f"{letter}"
        )

df = pandas.read_csv("birthdays.csv")
birthdays_dict = df.to_dict(orient="records")

today = dt.datetime.now()

for birthday in birthdays_dict:
    if birthday["month"] == today.month and birthday["day"] == today.day:
        send_greeting_card(birthday)

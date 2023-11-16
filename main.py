import requests, smtplib, time
from datetime import datetime

my_email = "email to send from"
password = "app password"

MY_LAT = 51.507351
MY_LONG = -0.127758

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
print(time_now.hour)

while True:

    if iss_latitude >= 46.507351 and iss_latitude <= 56.507351 and time_now.hour >= sunset:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg="Subject:ISS Tracker Alert \n\n Look up now! ")
            print("Email sent")
    time.sleep(60)





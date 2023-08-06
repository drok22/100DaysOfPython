from datetime import datetime
import requests
import smtplib
import time

MY_LAT = 0 # Your latitude
MY_LONG = 0 # Your longitude
MY_EMAIL = "my_email@domain.com"
MY_PASSWORD = "myP@$$w0rD"

#------------------------------------------------------------------------
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

#------------------------------------------------------------------------
def is_night():
    parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()

    if time_now >= sunset or time_now >= sunrise:
        return True
    
#------------------------------------------------------------------------
def check_for_iss_overhead():
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up!\n\nTheISS is above you in the sky!"
        )

#------------------------------------------------------------------------
def main():
    while True:
        time.sleep(120)
        check_for_iss_overhead()
    
#------------------------------------------------------------------------
if __name__ == "__main__":
    main()
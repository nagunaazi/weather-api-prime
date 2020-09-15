from datetime import datetime
import  requests
import  json





city=input("enter a city name :")



date = input("Enter your date  : ")
bday = datetime.strptime(date, '%d-%m-%Y')
x1=( bday.day)

if x1 > 1:
    for i in range(2, x1):
        if (x1 % i) == 0:
            print( "sry the given  date is not prime number")
            break
    else:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=6f07ddc114fc1213eca9097fb580ba8b'.format(city)
        res = requests.get(url)
        details = res.json()
        temp = details['main']['temp_max']
        pressure = details['main']['pressure']
        humidity = details['main']['humidity']
        speed = details['wind']['speed']
        name = details['name']
        contex = {"temp": temp, "pressure": pressure, "humidity": humidity, "speed": speed, "name": name}
        print(contex)

else:
    print(x1, "date must be greater than 1")

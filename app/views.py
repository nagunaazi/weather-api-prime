from django.shortcuts import render
import  requests
import  json
from django.views.generic import View
from datetime import datetime



# Create your views here.
#
# city= eval(input("enter a city name:"))
#
# url='http://api.openweathermap.org/data/2.5/weather?q={}&appid=6f07ddc114fc1213eca9097fb580ba8b'.format(city)
#
# res= requests.get(url)
#
# data= res.json()
#
# print(data)
#
class WeatherDetails(View):
    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        city = request.POST.get('c1')
        date=request.POST.get('b1')
        bday = datetime.strptime(date, '%Y-%m-%d')

        x1 = (bday.day)


        if x1 > 1:
            for i in range(2, x1):
                if (x1 % i) == 0:
                    message="sorry the given date is not prime plz check another one"
                    # print("sry the given  date is not prime number")
                    return render(request, "index.html", {"error_message":message })

            else:
                  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=6f07ddc114fc1213eca9097fb580ba8b'.format(
                    city)
                  res = requests.get(url)
                  details = res.json()
                  temp = details['main']['temp_max']
                  pressure = details['main']['pressure']
                  humidity = details['main']['humidity']
                  speed = details['wind']['speed']
                  name = details['name']
                  contex = {"temp": temp, "pressure": pressure, "humidity": humidity, "speed": speed, "name": name}
                  return render(request, "index.html", {"data": contex})
        else:
            message = "sorry the date of  one  is not prime"
            return render(request, "index.html", {"error_message": message})

        # except
        #     print(x1, "date must be greater than 1")

        # print(date)
        #
        # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=6f07ddc114fc1213eca9097fb580ba8b'.format(city)
        #
        #
        # res = requests.get(url)
        #
        # details = res.json()
        # print(details)
        # temp=details['main']['temp_max']
        # pressure=details['main']['pressure']
        # humidity=details['main']['humidity']
        # speed=details['wind']['speed']
        # name=details['name']
        # contex={"temp":temp,"pressure":pressure,"humidity":humidity,"speed":speed,"name":name}
        # return render(request, "index.html", {"data": contex})
import sys
import pywapi
import string

def get_weather(zipcode):
    zipcode = str(zipcode)
    weather_com_result = pywapi.get_weather_from_weather_com(zipcode)
    return "Weather.com says: It is " + string.lower(weather_com_result['current_conditions']['text']) + " and " + weather_com_result['current_conditions']['temperature'] + "C now in " + zipcode

if __name__ == "__main__":
    try:
        print get_weather(sys.argv[1])
    except Exception,e:
        print str(e)

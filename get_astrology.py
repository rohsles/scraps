import sys
import lxml
from bs4 import BeautifulSoup
from urllib2 import urlopen

def get_astrology(sign):
    url = "http://my.horoscope.com/astrology/free-daily-horoscope-%s.html" % sign
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "lxml")
    horoscope = [horo.string for horo in soup.findAll(id="textline")]
    date = [date.string for date in soup.findAll(id="advert")]
    print date[1] + ":" + horoscope[1]

if __name__ == "__main__":
    try:
        get_astrology(sys.argv[1])
    except IndexError:
        print "Please enter a valid zodiac sign.\nUsage example: python get_astrology.py aries"

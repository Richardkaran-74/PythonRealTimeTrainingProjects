import urllib.request
import json


def printresults(data):
    thejson = json.loads(data)
    if "title" in thejson["metadata"]:
        print(thejson["metadata"]["title"])
    count = thejson["metadata"]["count"]
    print(str(count) + " events recorded")

    for i in thejson["features"]:
        print(i["properties"]["place"])
    print("---------\n")

    for i in thejson["features"]:
        if i["properties"]["mag"] >= 4.0:
            print("%2.1f" %i["properties"]["mag"], i["properties"]["place"])
    print("-------\n")

def main():
    urldata = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson"
    WebUrl = urllib.request.urlopen(urldata)
    print("result code :" + str(WebUrl.getcode()))

    if (WebUrl.getcode() == 200):
        data = WebUrl.read()
        printresults(data)
    else:
        print('Recieved error,cant parse')

if __name__ == '__main__':
    main()
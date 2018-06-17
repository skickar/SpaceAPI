from geopy.distance import geodesic

#Learning API calls, tracking the ISS for 60 seconds and estimating its speed by comparing GPS positions

import requests, json, geocoder, time
data = (requests.get("http://api.open-notify.org/astros.json")).json();print("Data Request: ",(data['message'])),print("Total humans in orbit: ",data['number'],"\nPrinting manifest:")
for i in range(len(data['people'])):
    print(("%s is currently in space aboard the %s." % ((data['people'][i]['name']), (data['people'][i]['craft']))))
g = geocoder.osm([(requests.get("http://api.open-notify.org/iss-now.json")).json()['iss_position']['latitude'], (requests.get("http://api.open-notify.org/iss-now.json")).json()['iss_position']['longitude']], method='reverse')
for i in range(6):
    if i < 1:
        print("Target acquired, tracking active: the location of the ISS is ",
              (requests.get("http://api.open-notify.org/iss-now.json")).json()['iss_position']['latitude'],
              (requests.get("http://api.open-notify.org/iss-now.json")).json()['iss_position']['longitude'])
        lastknown = ((requests.get("http://api.open-notify.org/iss-now.json")).json()['iss_position']['latitude'], (requests.get("http://api.open-notify.org/iss-now.json")).json()['iss_position']['longitude'])
        firstknown = lastknown

        time.sleep(10)
    elif i < 5:
        print("Update: the location of the ISS is ",
              (requests.get("http://api.open-notify.org/iss-now.json")).json()['iss_position']['latitude'],
              (requests.get("http://api.open-notify.org/iss-now.json")).json()['iss_position']['longitude'])
        currentknown = ((requests.get("http://api.open-notify.org/iss-now.json")).json()['iss_position']['latitude'],
                     (requests.get("http://api.open-notify.org/iss-now.json")).json()['iss_position']['longitude'])
        print("ISS has traveled approximately ",geodesic(lastknown, currentknown).miles, "miles in 10 seconds.")
        time.sleep(10)
    elif i == 5:
        print("Final round: the location of the ISS is ",
              (requests.get("http://api.open-notify.org/iss-now.json")).json()['iss_position']['latitude'],
              (requests.get("http://api.open-notify.org/iss-now.json")).json()['iss_position']['longitude'])
        currentknown = ((requests.get("http://api.open-notify.org/iss-now.json")).json()['iss_position']['latitude'],
                        (requests.get("http://api.open-notify.org/iss-now.json")).json()['iss_position']['longitude'])
        print("The ISS is traveling at approximately  ", geodesic(firstknown, currentknown).miles, "miles per minuite.")
        mile_hour = (int(geodesic(firstknown, currentknown).miles)*60)
        print("The ISS is traveling at approximately ",mile_hour," miles per hour.\n>>>discontinuing tracking>>>")

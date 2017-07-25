
# coding: utf-8

# In[60]:

import requests
import datetime


# In[61]:

base_url = 'https://api.darksky.net/forecast/bdcf2062c18dc07b00bf2552a16c730f/'
nyc_coordinates = [
    40.811264,
    -73.959016
]
nyc_url = (base_url + 
                  str(nyc_coordinates[0]) + ',' + 
                  str(nyc_coordinates[1]))
response = requests.get(nyc_url)
data = response.json()


# In[62]:

msg_temperature = str(data['currently']['temperature'])
msg_summary = data['currently']['summary'].lower()
msg_temperature_max = str(data['daily']['data'][0]['temperatureMax'])
msg_temperature_min = str(data['daily']['data'][0]['temperatureMin'])

average_temperature = (data['daily']['data'][0]['temperatureMax'] + 
                           data['daily']['data'][0]['temperatureMin']) / 2;

if average_temperature > 77:
    msg_temperature_feeling = 'hot'
elif average_temperature > 68:
    msg_temperature_feeling = 'warm'
elif average_temperature > 58:
    msg_temperature_feeling = 'moderate'
else:
    msg_temperature_feeling = 'cold'


msg_rain_warning = " Bring your umbrella!" if data['daily']['data'][0]['precipProbability'] > 0.5 else ""


# In[63]:

msg = "Right now it is " + msg_temperature + " degrees out and " + msg_summary + ". Today will be " + msg_temperature_feeling + " with a high of " + msg_temperature_max + " degrees and a low of " + msg_temperature_min + " degrees." + msg_rain_warning

now = datetime.datetime.now()
subject = "8AM Weather forecast: " + str(now.strftime("%B")) + " " + str(now.day) + ", " + str(now.year)


# In[64]:

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox13c522fcf6954ddfa857679788497b18.mailgun.org/messages",
        auth=("api", "key-982f7a4b982e06e6d3949a0734062ef2"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox13c522fcf6954ddfa857679788497b18.mailgun.org>",
              "to": "Mathieu Rudaz <mathieu.rudaz@gmail.com>",
              "subject": subject,
              "text": msg})


# In[65]:

send_simple_message()


# In[ ]:




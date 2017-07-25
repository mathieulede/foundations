
# coding: utf-8

# In[160]:

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from twilio.rest import Client
import os.path


# In[173]:

# Twilio authentification
account_sid = "ACd7bb82d00d436cbba9397c72572aafbd"
auth_token = "38431437902b550b99d88a5244b35151"
client = Client(account_sid, auth_token)


# In[174]:

# Get the NYT page
response = requests.get("http://www.nytimes.com")
doc = BeautifulSoup(response.text, 'html.parser')


# In[178]:

# Get the top headline
center_column = doc.find('div', {'class': 'b-column'})
top_article = center_column.find("article", { 'class': ['story', 'theme-feature'] })

headline_data = {
    'headline': top_article.find("h1", {'class': 'story-heading'}).get_text(),
    'img_src': top_article.find("img")['src'],
    'summary': top_article.find("p", {'class': 'summary'}).get_text(),
    'date': time.strftime("%Y-%m-%d-%H-%M")
}


# In[ ]:

# Construct and send the sms
def send_sms():
    sms_msg = "New headline: " + headline_data['headline']

    client.messages.create(
        to="+13473342046",
        from_="+12014821773",
        body=sms_msg,
        media_url=headline_data['img_src'])


# In[ ]:

# Check if the current top headline is different from the last saved one
if os.path.isfile('headlines_history.csv'):
    headlines_history = pd.read_csv('headlines_history.csv')
    
    if headlines_history['headline'].tail(1).item() != headline_data['headline']:
        headlines_history = headlines_history.append([headline_data])
        headlines_history.to_csv('headlines_history.csv', index=False)
        send_sms()
else:
    df_headline_data = pd.DataFrame([headline_data])
    df_headline_data.to_csv('headlines_history.csv', index=False)
    send_sms()


# In[ ]:




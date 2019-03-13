#!/usr/bin/python
import requests
# Enter the Server IP address, username and password

things=['Firewalls','Switches','Routers']
for device in things:
        url = 'https://<hostname>/data/report/Best+Practice+Checks+-+'+device+'+-+High+and+Medium'
        username = '<username>'
        password = '<password>'
        try:
         response = requests.get(url, auth=(username,password),verify=False)
         #print response.text
         p=open(device+".xml","w")
         p.write(response.text)
         p.close()
        except requests.exceptions.ConnectionError as e:
         print "Connection to ("+url+"):\n"
         print e

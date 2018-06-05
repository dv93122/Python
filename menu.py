#!/usr/bin/python2
import time
import os
import webbrowser
import facebook   	#to get access of facebook 
import requests		#to send organic,grass-fed HTTP/1.1	 
import urllib		#for url library
from bs4 import BeautifulSoup  #to wrap the url 

x = ''' 
press 1 : To check time
press 2 : To reboot your system 
Press 3 : To create a new user in Redhat
press 4 : To check the Ram and c.p.u info
press 5 : To search data on google and print url of first page of Google
press 6 : To search something on Google 
press 7 : To login your facebook account and update the status 
press 8 : To scan all the IP address in your Network and MAC address 
'''
print x
choice = int(raw_input("Choose your choice:"))

if choice == 1:
	print time.ctime().split()[3]
elif choice == 2:
	os.system('reboot')
elif choice == 3:
         uname = raw_input("Enter your username:")
  	 os.system(' useradd ' +uname)
	 print "Enter your Password"
	 os.system(' passwd '  +uname)
elif choice == 4:
	os.system('free -m')
        os.system('top')
elif choice == 5:
   	text = raw_input("enter your search")
	text = urllib.quote_plus(text)

	url = 'https://google.com/search?q=' + text
	
	#to get response from the url
	response = requests.get(url)

	#to wrap the url
	soup = BeautifulSoup(response.text, 'lxml')
	for g in soup.find_all(class_='g'):
		#to print url
    		print(g.text)
    		print('-----')
elif choice == 6:
        x=raw_input("enter search the item")
	webbrowser.open_new_tab('https://www.google.com/search?q=' +x)
elif choice == 7:
	#to get access of user_access_token for facebook and google Api
	graph = facebook.GraphAPI('EAACEdEose0cBAGu6oFZBRbjBurzehPuUKJfc7eGRsNlNKlj0R6iEr7iPJ8nv3J6D9431qGtZA0brZBXnKZB2FtVcypmjnJUmX7gjAEMiKb41ZCLSHId7C3nFTfgNZBY2fJnYiMNaZCYEoTQish5czCuyhQqZAw9XxpNEpdXaLMbjgNxMRULqYp8BU124uuZAM1DJydb7NEthVeQZDZD', version="2.6")						
	#to get access of user_access_token for facebook and google Api
	status=raw_input("enter your status")
	#to post the status on user facebook
	graph.put_object(parent_object='me', connection_name='feed', message=status)	#to post the status on user facebook
	
elif choice == 8:
        os.system('ifconfig')	
else:
	print "No chance"

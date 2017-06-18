from flask import Flask
import requests


app = Flask(__name__)




def xml_pretty(xml_string):
	import xml.dom.minidom
	xml =xml.dom.minidom.parseString(xml_string)
	pretty_xml_ =xml.toprettyxml()
	print (pretty_xml_)

@app.route('/SendSMS/<string:name>')
def SendSMS(name):
    username ='ACa920c25520795abaf477e153e59f94ef' #account_SID
    password ='1257682f22fd7aca372dab1d73f5800f'   #auth_token
    number_to_text =name 
    twilio_number ='+14159420675'
    message_body ='Hi , this is Tarek, from python program!'
    base_url ='https://api.twilio.com/2010-04-01/Accounts'
    message_url = base_url + '/'+ username +'/Messages'

    auth =(username,password)

    post_data ={"From":twilio_number,"To":number_to_text,"Body":message_body}

    r = requests.post(message_url,data=post_data,auth=auth)

    xml_pretty(r.text)

if __name__ == '__main__':
  app.run(port=5000,debug=True)
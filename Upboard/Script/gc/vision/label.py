import argparse
import base64
import httplib2
import os
from time import sleep

from apiclient.discovery import build
from oauth2client.client import GoogleCredentials
from time import sleep
from google.cloud import translate

def main():

 os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/norman/Documents/Vision2-befbab1fbecb.json"
 
 API_DISCOVERY_FILE = 'https://vision.googleapis.com/$discovery/rest?version=v1'
 http = httplib2.Http()

 credentials = GoogleCredentials.get_application_default().create_scoped(
     ['https://www.googleapis.com/auth/cloud-platform'])
 credentials.authorize(http)

 service = build('vision', 'v1', http, discoveryServiceUrl=API_DISCOVERY_FILE)
  
 translate_client = translate.Client()
 target = 'es'

 os.system('espeak -v es-la -a 200 "Ahora tomare la foto"')  
 sleep(2)
 os.system('fswebcam -r 640x480 --jpeg 85 -D 1 reconoce.jpg')  
 sleep(5)

 with open("reconoce.jpg", 'rb') as image:
   image_content = base64.b64encode(image.read())
   service_request = service.images().annotate(
     body={
       'requests': [{
         'image': {
           'content': image_content.decode("utf-8")
          },
         'features': [{
           'type': 'LABEL_DETECTION',
           'maxResults': 5,
          }]
        }]
     })
   response = service_request.execute()
   opcion = ""
   for results in response['responses']:
     if 'labelAnnotations' in results:          
       for annotations in results['labelAnnotations']:
         print('Found label %s, score = %s' % (annotations['description'],annotations['score']))
         opcion = annotations['description']
         print(opcion)
         break
   translation = translate_client.translate(opcion,target_language=target)
   print(translation['translatedText'])    
   string = "Creo que es " + str(translation['translatedText']) 
   os.system('feh -F reconoce.jpg &')   
   os.system('espeak -v es-la -a 200 "{}"'.format(string))
   os.system('killall -9 feh')
   return 0 

if __name__ == '__main__':
 main()


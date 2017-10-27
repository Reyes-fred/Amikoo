import sys
import os,random

tipo = sys.argv[1]
message = sys.argv[2];
message = message.split("/")
path = "/home/alfredo/archivos/"


if(message[1] == 'Random'):
  randomfile = random.choice(os.listdir(path+message[0]+"/"+tipo+"/"))
  file = randomfile
  nombre=file
elif(message[1] == "Stop"):
  os.system('killall -9 aplay')
  os.system('killall -9 vlc')
  os.system('killall -9 feh')
  sys.exit()
else:
  nombre=message[1]

if(tipo == 'Sound'):
  path2 = path+message[0]+"/Sound/"+nombre
  os.system('mpg123 '+path2)

elif(tipo == "Image"):
  path2 = path+message[0]+"/Image/"+nombre
  os.system('feh -F '+path2)

elif(tipo == "Video"):
   path2 = path+message[0]+"/Video/"+nombre
   os.system("vlc -ldummy --fullscreen "+nombre)

else:
 print("error")

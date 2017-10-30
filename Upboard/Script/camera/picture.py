import os
import datetime
import shutil

def main():
  now = datetime.datetime.now()
  name = str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"-"+str(now.hour)+"-"+str(now.minute)+"-"+str(now.second)
  name = str(name)+".jpg"
  os.system("fswebcam -r 4096x2304 --jpeg 100 --no-banner " + name)
  shutil.move(name,"/home/alfredo/tdb/"+name)
  os.system("feh -F /home/alfredo/tdb/"+name)
  return 0

if __name__ == '__main__':
 main()

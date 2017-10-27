import os
import datetime
import shutil

def main():
  now = datetime.datetime.now()
  name = str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"-"+str(now.hour)+"-"+str(now.minute)+"-"+str(now.second)
  name = str(name)+".jpg"
  os.system("fswebcam -r 640*480 --jpeg 85 -D 1 " + name)
  shutil.move(name,"/home/alfredo/tdb/"+name)
  return 0

if __name__ == '__main__':
 main()

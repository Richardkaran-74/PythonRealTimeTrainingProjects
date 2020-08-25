import os
from os import path
import datetime
from datetime import date,time,timedelta
import time
def main():
    print(os.name)

    #print('item exits:' + str(path.exits('File text1.txt')))
    #print('item is a file:' + str(path.isfile('Rolling Dice.py')))
    #print('item is a directory:' + str(path.isdir('File text.txt')))
    print('item path:' + str(path.realpath('File text.py')))
    print('item path & name:' + str(path.split(path.realpath('File text.py'))))

    t = time.ctime(path.getmtime('File text1.txt'))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime('File text1.txt')))

    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime('File text1.txt'))
    print('It has been '+ str(td)+' since the file has modified')
    print('or '+str(td.total_seconds())+' seconds')

if __name__ == '__main__':
    main()

def printPicnic(itemsdict, leftwidth,rightwidth):
    print("PICNIC ITEMS".center(leftwidth+rightwidth,'-'))
    for k,v in itemsdict.items():
        
        print(k.ljust(leftwidth,'.')+str(v).rjust(rightwidth))

printitems={'sandwiches':4,'apples':12,'cups':4,'cookies':8000}

printPicnic(printitems,12,5)

import pyperclip
pyperclip.copy('hellow word')


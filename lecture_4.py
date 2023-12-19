# def div(x):
#     try:
#         return 42/x
#     except ZeroDivisionError:
#         print('error, ivalid input')


# print(div(3))
# print(div(0))
import time, sys
x=1
increase=True
try:
    while True:

        
        print(' '*x,end='')
        print('**********')
        time.sleep(0.1)

        if x<20 and increase==True :
            x=x+1

        elif x==20 and increase==True:
            increase=not increase

        elif x>0 and x<=20 and increase==False:
            x=x-1
        elif x==0 and increase==False:
            increase= not increase
except KeyboardInterrupt:
    sys.exit()

    


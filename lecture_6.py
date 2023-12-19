# x={'nino': 'Now 27',"jemal":"March 23"
#    ,"mariam":"March 23",'giorgi':'Oct 12'}

# while True:
#     inp=input()
#     if inp=='':
#         break
#     elif inp in x:
#         print( x[inp])
#     else:
#         print(f"i don't know {inp}")
#         print("will you tell me when is her birthday")
#         ye=input()
#         if ye=="yes":
#             print('so when is birthday')
#             add=input()
#             x[inp]=add
#         else:
#             continue


# #----------------------asoebis datvla----------------

# import pprint
# x='chito gvrito chito margalito daaa, me ra mamgerebs udziro zedca zambaxis'
# count={}
# for i in x:
#     count.setdefault(i,0)
#     count[i]=count[i]+1 

# pprint.pprint (count)



# X_O_X_O_X_O_X_O_X_O_X_O_X_O_X_O_X_O_X_O_X_O_X_O_X_O_X_O_X_O_X_O_X_O_X_O





dic={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
var="X"
for i in range(9):
        
    print(dic[1]+'|'+dic[2]+'|'+dic[3])
    print('-+-+-')
    print(dic[4]+'|'+dic[5]+'|'+dic[6])
    print('-+-+-')
    print(dic[7]+'|'+dic[8]+'|'+dic[9])
    
    print(f'{var}-ის ჯერია')

    x=int(input())
    if var =="X":
        dic[x]=var
        var='O'
    else:
        dic[x]=var
        var='X'
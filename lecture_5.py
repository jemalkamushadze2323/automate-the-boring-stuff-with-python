# # z=['x','p','misha','davoto']
# # def com(x):
# #     y=[]
# #     for i in list(x):
# #         y=y+list(i)
# #     print(y)

# # com(z)

# #-----------------------------commma code----------------------------------

# z = ['x', 'p', 'misha', 'davoto','red','yellow']



# def com(list):
#     if len(list)==0:
#         print('')
#     elif len(list)==1:
#         print(list)
#     else:
        

#         y = ''
#         cop_x=list.copy()
#         while len(cop_x)>=2:
#             y=y+cop_x.pop(0)+', '
#         y=y+' and '+ cop_x.pop(0)
#         print(y)

# com(z)



# #-------------------------coin flip streak



# import random
# y=0
# for i in range(10000):
            
#     x= ''.join([ 'T' if random.randint(0,1,)==0  else 'H' for i in range(100)])
#     f_ch_T='TTTTTT'
#     f_ch_H='HHHHHH'
    
#     if (f_ch_H or f_ch_T) in x:
#         y+=1
# print(y/10000*100)



grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for x in range(len(grid[0])):
    for y in range(len(grid)):

        print(grid[y][x],end='')
    print('')
    

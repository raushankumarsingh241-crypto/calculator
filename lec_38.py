list=[[1,1,1],[1,1,1],[1,1,1]]
print(list[0])
print(list[1])
print(list[2])
str=input('enter you position where you marks "X"')
l=str.split(" ")
row=int(l[0])
col=int(l[1])
list[row-1][col-1]='X'
print(list[0])
print(list[1])
print(list[2])
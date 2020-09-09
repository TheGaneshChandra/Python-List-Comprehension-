
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
#lst = [x,y,z]
lsit = []
i = j = k = 0
#print("[",end = "")
while i<x+1:
    j = 0
    while j<y+1:
        k = 0
        while k<z+1:
            if i+j+k != n:
                lst = [i,j,k]
                lsit.append(lst)
                #print(lst, end = ", ")
            k = k+1
        j = j+1
    i = i+1
print(lsit)

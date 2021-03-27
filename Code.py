import random

def display():
    for i in range(n):
        for j in range(n):
            print(chess[i][j],end=" ")
        print()

def displayt():
    for i in range(n):
        for j in range(n):
            print(tchess[i][j],end=" ")
        print()

n=8
fail=0
countfinal=0
n2=0

for n1 in range(0,8):
    for n2 in range(0,8):
        for n3 in range(0,8):
            for n4 in range(0,8):
                for n5 in range(0,8):
                    for n6 in range(0,8):
                        for n7 in range(0,8):
                            for n8 in range(0,8):
                                chess=[[0,0,0,0,0,0,0,0],
                                       [0,0,0,0,0,0,0,0],
                                       [0,0,0,0,0,0,0,0],
                                       [0,0,0,0,0,0,0,0],
                                       [0,0,0,0,0,0,0,0],
                                       [0,0,0,0,0,0,0,0],
                                       [0,0,0,0,0,0,0,0],
                                       [0,0,0,0,0,0,0,0]]

                                tchess=[[0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0],
                                        [0,0,0,0,0,0,0,0]]

                                row=0
                                chess[row][n1]=1
                                num=n1
                                diag=row+num
                                p=row
                                q=num
                                for i in range(n):
                                    tchess[row][i]="N"
                                    tchess[i][num]="N"
                                for i in range(n):
                                    for j in range(n):
                                        if(i+j==diag):
                                            tchess[i][j]="N"
                                while(1):
                                    try:
                                        tchess[p][q]="N"
                                        p=p+1
                                        q=q+1
                                    except:
                                        break
                                row=row+1
                                if(tchess[row][n2]==0):
                                    chess[row][n2]=1
                                    num=n2
                                else:
                                    continue
                                diag=row+num
                                p=row
                                q=num
                                for i in range(n):
                                    tchess[row][i]="N"
                                    tchess[i][num]="N"
                                for i in range(n):
                                    for j in range(n):
                                        if(i+j==diag):
                                            tchess[i][j]="N"
                                while(1):
                                    try:
                                        tchess[p][q]="N"
                                        p=p+1
                                        q=q+1
                                    except:
                                        break
                                row=row+1
                                if(tchess[row][n3]==0):
                                    chess[row][n3]=1
                                    num=n3
                                else:
                                    continue
                                diag=row+num
                                p=row
                                q=num
                                for i in range(n):
                                    tchess[row][i]="N"
                                    tchess[i][num]="N"
                                for i in range(n):
                                    for j in range(n):
                                        if(i+j==diag):
                                            tchess[i][j]="N"
                                while(1):
                                    try:
                                        tchess[p][q]="N"
                                        p=p+1
                                        q=q+1
                                    except:
                                        break
                                row=row+1
                                if(tchess[row][n4]==0):
                                    chess[row][n4]=1
                                    num=n4
                                else:
                                    continue
                                diag=row+num
                                p=row
                                q=num
                                for i in range(n):
                                    tchess[row][i]="N"
                                    tchess[i][num]="N"
                                for i in range(n):
                                    for j in range(n):
                                        if(i+j==diag):
                                            tchess[i][j]="N"
                                while(1):
                                    try:
                                        tchess[p][q]="N"
                                        p=p+1
                                        q=q+1
                                    except:
                                        break
                                row=row+1
                                if(tchess[row][n5]==0):
                                    chess[row][n5]=1
                                    num=n5
                                else:
                                    continue
                                diag=row+num
                                p=row
                                q=num
                                for i in range(n):
                                    tchess[row][i]="N"
                                    tchess[i][num]="N"
                                for i in range(n):
                                    for j in range(n):
                                        if(i+j==diag):
                                            tchess[i][j]="N"
                                while(1):
                                    try:
                                        tchess[p][q]="N"
                                        p=p+1
                                        q=q+1
                                    except:
                                        break
                                row=row+1
                                if(tchess[row][n6]==0):
                                    chess[row][n6]=1
                                    num=n6
                                else:
                                    continue
                                diag=row+num
                                p=row
                                q=num
                                for i in range(n):
                                    tchess[row][i]="N"
                                    tchess[i][num]="N"
                                for i in range(n):
                                    for j in range(n):
                                        if(i+j==diag):
                                            tchess[i][j]="N"
                                while(1):
                                    try:
                                        tchess[p][q]="N"
                                        p=p+1
                                        q=q+1
                                    except:
                                        break
                                row=row+1
                                if(tchess[row][n7]==0):
                                    chess[row][n7]=1
                                    num=n7
                                else:
                                    continue
                                diag=row+num
                                p=row
                                q=num
                                for i in range(n):
                                    tchess[row][i]="N"
                                    tchess[i][num]="N"
                                for i in range(n):
                                    for j in range(n):
                                        if(i+j==diag):
                                            tchess[i][j]="N"
                                while(1):
                                    try:
                                        tchess[p][q]="N"
                                        p=p+1
                                        q=q+1
                                    except:
                                        break
                                row=row+1
                                if(tchess[row][n8]==0):
                                    chess[row][n8]=1
                                    num=n8
                                else:
                                    continue
                                diag=row+num
                                p=row
                                q=num
                                for i in range(n):
                                    tchess[row][i]="N"
                                    tchess[i][num]="N"
                                for i in range(n):
                                    for j in range(n):
                                        if(i+j==diag):
                                            tchess[i][j]="N"
                                while(1):
                                    try:
                                        tchess[p][q]="N"
                                        p=p+1
                                        q=q+1
                                    except:
                                        break
                                if(fail==0):
                                    display()
                                    print()
                                    countfinal=countfinal+1
                                    break
print("TOTAL NUMBER OF POSSIBILITY OF CHESS 8X8 =",countfinal)


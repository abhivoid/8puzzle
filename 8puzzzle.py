import copy
p=[]
c=[]
def solve(a,b):
    p.append(a)

    while(p!=[]):
        x=p.pop(0)
        k=0
        for i in c:
             if(i==x):
                  k=1
                  break
        if(k==0):
             print(*x)
             l=0
             pq(x)
             c.append(x)
             for i in range(3):
              for j in range(3):
                if(x[i][j]==b[i][j]):
                    l=l+1
             if(l==9):
                break
             
             
    print("Done");

def pq(x):
    k=0
    for i in range(3):
        for j in range(3):
            if(x[i][j]==0):
                if(j<2):
                    w=copy.deepcopy(x)
                    c=copy.deepcopy(w[i][j]);
                    w[i][j]=copy.deepcopy(w[i][j+1]);
                    w[i][j+1]=copy.deepcopy(c);
                    p.append(w);

                if(j>0):
                    
                    w2=copy.deepcopy(x)
                    c=copy.deepcopy(w2[i][j]);
                    w2[i][j]=copy.deepcopy(w2[i][j-1]);
                    w2[i][j-1]=copy.deepcopy(c);
                    p.append(w2);


                if(i<2):
                        w4=copy.deepcopy(x)
                        c=copy.deepcopy(w4[i][j]);
                        w4[i][j]=copy.deepcopy(w4[i+1][j]);
                        w4[i+1][j]=copy.deepcopy(c);
                        p.append(w4);

                if(i>0):
                        w5=copy.deepcopy(x)
                        c=copy.deepcopy(w5[i][j]);
                        w5[i][j]=copy.deepcopy(w5[i-1][j]);
                        w5[i-1][j]=copy.deepcopy(c);
                        p.append(w5);


                k=1
                break

        if(k==1):
            break




intial=[]
print("Enter Intial state")
for i in range(3):
    a=[]
    for j in range(3):
        a.append(int(input()))
    intial.append(a)
final=[]
print("Enter Final state")
for i in range(3):
    a=[]
    for j in range(3):
        a.append(int(input()))
    final.append(a)


solve(intial,final)
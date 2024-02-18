import random
comp=random.randint(0,2)
user=int(input(" 0 for snake 1 for water and 2 for gun"))
def check(comp,user):
    if(comp==user):
        return 0
    if(comp==0 and user==1):
        return -1
    if(comp==1 and user ==2):
        return -1
    if(comp==2 and user==0):
        return-1
score=check(comp,user)
print("user:",user)
print("computer",comp)
if(score==0):
    print("its a draw") 
elif(score==-1):
    print("user lose")
else:
    print("user a won")   
    
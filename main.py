class fibonacci:
    def __init__(self):
        self.x=int(input("Enter fabonacci ssequence end value:"))
        i,a,b=1,0,1
        while (i+a) <= self.x:
            result=a+b
            print(f"{result}")
            a=b
            b=result
            i=result

i=1
while i==1:
    print("Hello from fibonacci sequence generator")
    y=fibonacci()
    ans=input("Do you want to generate more sequences? (yes/no)")
    if ans=="yes" or ans=="YES" or ans=="Yes":
        i=1
    elif ans=="no" or ans=="NO" or ans=="No":
        i=0
    else:
        print("Oops! You made wrong choice:(\n  No problem here we go again:)")
        i=1
    

print("Hope you enjoyed:)\nHAVE A GOOD DAY!!!")




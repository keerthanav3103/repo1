import random
import json
import mysql.connector
mydb=mysql.connector.connect(host='mydb',user='root',password='Gryffindor@2000',database='myeappdata')
myc=mydb.cursor()
def cancellingappliance(getref):
    f=open("electronicsdatabase.json","r")
    mydatabase1=json.load(f)
    f.close()
    for i in range(1,len(mydatabase1)+1):
        ans=mydatabase1[str(i)]['productid']
        if ans==getref:
            print("Your cancellation has been initiated...")
            a=random.randint(1000,10000)
            print(a)
            print('enter otp :')
            otp=int(input())
            if a==otp:
                print('cancelling done and refund initiated')
            else:
                print("Please enter the correct OTP.")
            del mydatabase1[str(i)]
            i=i-1
            query1="delete from customerdata where productid='%s'" %(getref)
            myc.execute(query1)
            mydb.commit()
            f=open("electronicsdatabase.json","w")
            json.dump(mydatabase1,f)
            f.close()
            break
        else:
            print("The reference id",getref,"does not exist...")
            print("Please check your reference id")
            break

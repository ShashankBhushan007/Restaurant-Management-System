print('''******************************************************************************************
*                                  Welcome to 'PAN ASIA'!!!                              *
*                            Pan Asia, Frazer Road , Patna-800001                        *
******************************************************************************************''')
A=[[1,'Chicken Butter Masala                           ',380],
   [2,'Rogan Josh                                       ',440],
   [3,'Sikandari Raan                                   ',650],
   [4,'Kastoori Kabab                                   ',600],
   [5,'Dal Bukhara                                      ',450],
   [6,'Tom Yum Goong                                    ',560],
   [7,'Massaman Curry                                   ',680],
   [8,'Mookata Thai BBQ                                 ',800],
   [9,'Lamb Grapow                                      ',470],
   [10,'Sukhumvit Soi 5 Fried Chicken                   ',740],
   [11,'Kimchi Jjigae                                   ',300],
   [12,'Bibimbap                                        ',480],
   [13,'Tteokbokki                                      ',450],
   [14,'Korean BBQ                                      ',800],
   [15,'Japchae                                         ',630],
   [16,'Sushi & Sashimi                                 ',300],
   [17,'Onigiri                                         ',420],
   [18,'Yakitori                                        ',560],
   [19,'Shabu Shabu                                     ',780],
   [20,'Miso Soup                                       ',500],
   [21,'Hot Pot                                         ',640],
   [22,'Kung Pao Chicken                                ',560],
   [23,'Soup Dumplings                                  ',450],
   [24,'Chinese Drunken Chicken                         ',660],
   [25,'Char Siu BBQ                                    ',800],
   [26,'Chai                                            ',100],
   [27,'Mekhong                                         ',250],
   [28,'Soju                                            ',150],
   [29,'Sake                                            ',200],
   [30,'Maotai                                          ',250]]
name=input("Dear Customer , May I know your name.")
ph_no=int(input("Enter your ph.no."))
address= input("Enter you address")
Date=input('Enter the Date')
print('''Dear Customer, Please let us know your order.''')
k=0
B=[]
while(k==0):
    
    print('''Enter 1) for INDIAN ACCENT
      2) for THAI CHOICE
      3) for KOREA COURT
      4) for JAPAN JEWELS
      5) for CHINA STATION
      6) for GULP IT DOWN ASIA''')
    n=int(input())
    if n==1:
        print('                 INDIAN ACCENT')
        print("Enter the no. beside the dish you choose.")
        for i in range(0,5):
            print(A[i][0],')',A[i][1],'Rs',A[i][2])
        ch=int(input())
        print('Enter the Quantity')
        q=int(input())
        for i in range(0,5):
            if(ch==i):
                B.append(q)
                B.append(A[i-1][1])
                B.append(A[i-1][2])
        
        n=0

        
    if n==2:
        print('                  THAI CHOICE')
        print("Enter the no. beside the dish you choose.")
        for i in range(5,10):
            print(A[i][0],')',A[i][1],'Rs',A[i][2])
        ch=int(input())
        print('Enter the Quantity')
        q=int(input())
        for i in range(5,11):
            if(ch==i):
                B.append(q)
                B.append(A[i-1][1])
                B.append(A[i-1][2])
        
        n=0
    if n==3:
        print('                  KOREA COURT')
        print("Enter the no. beside the dish you choose.")
        for i in range(10,15):
            print(A[i][0],')',A[i][1],'Rs',A[i][2])
        ch=int(input())
        print('Enter the Quantity')
        q=int(input())
        for i in range(10,16):
            if(ch==i):
                B.append(q)
                B.append(A[i-1][1])
                B.append(A[i-1][2])
        
        n=0


    if n==4:
        print('                 JAPAN JEWELS')
        print("Enter the no. beside the dish you choose.")
        for i in range(15,20):
            print(A[i][0],')',A[i][1],'Rs',A[i][2])
        ch=int(input())
        print('Enter the Quantity')
        q=int(input())
        for i in range(15,20):
            if(ch==i):
                B.append(q)
                B.append(A[i-1][1])
                B.append(A[i-1][2])
        
        n=0
    if n==5:
        print('                 CHINA STATION')
        print("Enter the no. beside the dish you choose.")
        for i in range(20,25):
            print(A[i][0],')',A[i][1],'Rs',A[i][2])
        ch=int(input())
        print('Enter the Quantity')
        q=int(input())
        for i in range(20,26):
            if(ch==i):
                B.append(q)
                B.append(A[i-1][1])
                B.append(A[i-1][2])
        
        n=0

    if n==6:
        print('              GULP IT DOWN ASIA')
        print("Enter the no. beside the dish you choose.")
        for i in range(25,30):
            print(A[i][0],')',A[i][1],'Rs',A[i][2])
        ch=int(input())
        print('Enter the Quantity')
        q=int(input())
        for i in range(25,31):
            if(ch==i):
                B.append(q)
                B.append(A[i-1][1])
                B.append(A[i-1][2])
        
        n=0
    print('''Sir, If your order is complete then enter 1.
If you want to add anything more then enter 0''')
    k=int(input())
print('''*******************************************************************************************************
*                                               'PAN ASIA'                                            *
*                                  Pan Asia, Frazer Road , Patna-800001                               *
*******************************************************************************************************''')
print()
print('Name-',name,'                 Phone No.-',ph_no)
print('Address-',address,'           Date-',Date)
print('_______________________________________________________________________________________________________')
print('''S.No.           Item Name                                        Rate            Qty.          Amount
_______________________________________________________________________________________________________
                                                                        ''')
for i in range(0,(int(len(B)/3))):
    print(i+1,')      |     ',B[(i*3)+1],B[(i*3)+2],'     |      ',B[i*3],'    |      ',B[i*3]*B[(i*3)+2])
    n=n+B[i*3]*B[(i*3)+2]
print('''_______________________________________________________________________________________________________
                                                                        ''')
print(''' GST No.- 09AAACE4923H1ZQ                                                 |      Gross Amount =''',n,'''
 Email ID- panasia@gmail.com                                              |              SGST = 9%
 Phone No.- 1234567890                                                    |              CGST = 9%
                                                                          |               GST =''',int(n*.18),'''
_______________________________________________________________________________________________________                                                                                       
                                                                                   Net Amount =''',int(n*1.18))
print('''_______________________________________________________________________________________________________

                                              Thanks for your Order
                                                Come Back Again!!!''')


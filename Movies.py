import random
otp=random.randint(1000,2000)
file=open(r'C:\Users\deepu\Desktop\Projects\Python-mini\Python-project\Otp-generator.txt','w')
file.write(otp)
file.close()
class movie:
    def __init__(self,Mov_Name,category,language,time):
        self.Mov_Name=Mov_Name
        self.category=category
        self.language=language
        self.time=time
        
    def display_mov(self):
        print(f'Mov_Name:{self.Mov_Name},Category:{self.category},time:{self.time}')
class Theater:
    def __init__(self,Tname,location,Available_seats,Amount):
        self.Tname=Tname
        self.location=location
        self.Available_seats=Available_seats
        self.Amount=Amount
        
    def display_seats(self):
        print(f'Available seats in {self.Tname}')
        print(f' Available seats is {self.Available_seats}')
        number=int(input("Total numbers of ticket needed:"))
        if 1<number<100:
            Cname=input("Enter Customer name:")
            
            print('-'*50)
            print(f'Seat reserved by {Cname} and Cost is {self.Amount * number}')
            print('Select 1 for Online ')
            print('select 2 for cash')
            print('-'*50)
            Payment=(int(input("Enter method : ")))
            
            
            if Payment==1:
                UPI=input('UPI ID:')
                

                pin=int(input('enter pin : '))
                # if pin
                print('payment done')
                print('-'*50)
            elif Payment==2:
                Cash=int(input('enter recieved cash :$'))
                total=self.Amount * number
                
                if Cash >= total:
                    remaining_amount= Cash-total
                    
                    print(f'Cash received. Change returned: $ {remaining_amount}')
                    print('-'*50)
                else:
                    print('Insufficient cash. Transaction cancelled.')
                    return
            else:
                print('Invalid payment method.')
                return

            print(f"{number} seats successfully booked. Remaining seats: {self.Available_seats-number}")
        else:    
            print('Invalid number of tickets or not enough seats available.')
            
print("----- Kannada Movie Booking System -----")   
print(" 1 Horror ")
print(" 2 Action ")
print(" 3 Drama ")
print(" 4 Thriller ")
print(" 5 Mystery ")
print(" 6 lovestory ")
print(" 7 Adventure ")
print(" 8 Rom-com ")
print(" 9 Comedy ")

print('-'*50)
Enter_Movie_Category_number=int(input(" Enter your choice (1-9):"))
if Enter_Movie_Category_number==1:
    Horror= movie("Karva", "Horror", "Kannada", "2h 28m")
    Horror.display_mov()
    t1 = Theater("PVR", "Bangalore", 100, 200)#Tname,location,Available_seats,Amount
    t1.display_seats()
    print('-'*50)
    
elif Enter_Movie_Category_number==2:
    Action=movie("Kantara","Action","Kannada","2h 30m")
    Action.display_mov()
    t2 = Theater("INOX", "Mysore", 200, 180)
    t2.display_seats()
    print('-'*50)
    
elif Enter_Movie_Category_number==3:
    Drama=movie("777 Charlie", "Drama", "Kannada", "2h 44m")
    Drama.display_mov()
    t3 = Theater("Cinepolis", "Mangalore", 150, 220)
    t3.display_seats()
    print('-'*50)
    
elif Enter_Movie_Category_number==4:
    Thriller=movie("Lucia", "Thriller", "Kannada", "2h 15m")
    Thriller.display_mov()
    t4 = Theater("Carnival", "Hubli", 120, 160)
    t4.display_seats()
    
elif Enter_Movie_Category_number==5:
    Mystery=movie("U Turn", "Mystery", "Kannada", "2h 10m")
    Mystery.display_mov()
    t5 = Theater("Rockline", "Belgaum", 180, 190)
    t5.display_seats()
elif Enter_Movie_Category_number==6:
    Mystery=movie("arya", "lovestory", "Kannada", "2h 10m")
    Mystery.display_mov()
    t6 = Theater("ganesha", "tiptur", 150, 290)
    t6.display_seats()
elif Enter_Movie_Category_number==7:
    Thriller=movie("Journey 2", "Adventure", "Kannada", "2h 15m")
    Thriller.display_mov()
    t7 = Theater("Carnival", "Hubli", 200, 150)
    t7.display_seats()
    
elif Enter_Movie_Category_number==8:
    Thriller=movie("college days", "Rom-com", "Kannada", "2h 15m")
    Thriller.display_mov()
    t8 = Theater("Carnival", "Hubli", 220, 250)
    t8.display_seats()
    
elif Enter_Movie_Category_number==9:
    Thriller=movie("Kirik party", "comedy", "Kannada", "2h 15m")
    Thriller.display_mov()
    t9 = Theater("lakshmi", "Tiptur", 100, 200)
    t9.display_seats()
    print('-'*50)

else:
    print("Your chossen movie category not available for now in any theater")
        

             
            
            
        
        
    
    
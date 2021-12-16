class google_pay: 
    def __init__(self):

        print("Welcome to gpay")
        
        self.__username = str(input("Enter name : "))
        if type(self.__username) == str:
           print("Name verified sucessfully \n")
        else:
            raise TypeError("Invalid name or check your name once again and try again")
        
    def check_mobilenumber(self):
        self.__usernumber = input("Enter Mobile Number : ")
        if type(self.__usernumber)==str:
            if len(self.__usernumber)==10:
                print(self.__usernumber,)
                print("Mobile number verified sucessfully \n")
            else:
                raise TypeError("Check your mobile number : ")
        else:
            raise ValueError("Invalid Type check your Mobile name and Try Again")
    
    def check_upi(self):
        self.__upi = input("Enter your upi id :")
        if type(self.__upi) == str:
            if len(self.__upi) < 16:
                print("your Upi id verified sucessfully \n")
                
            else:
                raise TypeError("check your Upi")
        else:
            raise ValueError("Invalid upi")

class bank(google_pay):
    def __init__(self):
        
        print("welcome!")
        
    def check_userbank(self):
        
        self.__userbank = int(input("Enter your bank name"))
        if self.userbank==str:
            print("this is a valid bank")
        else:
            print("this is a invalid bank)
            
            
        self.__useraccno = int(input("Enter Account number"))
        if len (self.__useraccno) <=12:
            print("Succesfully Verified !!")
                  
        else:
            raise TypeError("Please Check your bank account number")
        
    def pin_creation(self):
        self.__pin = int(input("Set up a 4 digit upi pin "))
        if len(self.__pin) == 6:
            self.__repin = input("re enter pin")
            if self.__pin==self.__repin:
                print("Your Pin Setup Sucessful")
            else:
                raise TypeError("Incorrect pin ,Please Try again")
        else:
            print("Try again!")

class userdata(bank):
    def __init__(self):
            self.__alldata=[self.__username,self.__usernumber,self.__upi,self.__userbank,self.__useraccnos,self.__pin]
            print(self.__alldata)
            
class payment(bank):
    def __init__(self):
        print("LETS START YOUR TRANSACTION")
    def r_data(self,ifsc):
        self.__rname = input("Enter Reciver's Name : ")
        if type(self.__rname) == str:
                self.__bankname= input("Enter Receiver's Bank :")
                
                self.__ifsccode = "str"
                print ("your ifsc code")
                if len(self.__ifsccode) == 13:

                    print("IFSC CODE verified")
                else:
                    raise ValueError("Inalid IFSC code \n check the code again")
        else:
            raise TypeError("Invalid Type Name")

    def transcaction(self):
            self.__raccno =int( input("Enter Reciver's Account number : "))
            if len (self.__raccno) <=17:
                    self.__reaccno1=int(input(" Re-Enter Reciver's Account number : "))
                    if self.__reaccno1 == self.__raccno:
                           print("Account Number verified")
                    else:
                         raise ValueError("Account Number mismatched Try again")
            else:
                raise ValueError("maximum number of limit crossed check and try agani")
    def mn_to_transfer(self):
            self.__amount = input("Enter amount to be transfered : ")
            self.__pin = input("Enter your 4 digit pin to make transcaction : ")
            if self.__pin == "0075":
                print("your Transcaction is sucessfull \n")
                

            else:
                print("Incorect pin!please try again")
obj = gpay()
obj.check_mobilenumber()
obj.check_upi()
obj1=bank()
obj1.check_bank()
obj1.pin_creation()
obj2 = userdata()
obj3 = payment()
obj3.reciver_data("CIUB0000893")
obj3.transcaction()
obj3.mn_to_transfer()


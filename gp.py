class Google_pay:                                                                                   
    
    def __init__(self,Phone_number,Name):                                                                  
        
        self.mobile=Phone_number
        self.name=Name
        
    def open_gpay(self):
        print("Google Pay")
        
    def mobile_verification(self):
        if (len(self.mobile)==10):
            if type(self.mobile) == str:                                                                            
                print("phone number verified")
            else:
                raise TypeError("the phone numbers should only be in integer format ")
        else:
            raise ValueError("the phone number should not be grater than or lesser than 10")
        
    def name_verification(self):
        if type(self.name) == str:
            if len(self.name) <= 20:                                                                                 
                print("name verified")
            else:
                raise ValueError("The name should contain lesser than or equal to 20 letters")
        else:
            raise TypeError("The name should contain string characters only")

    def otp_verification(self,code,otp):
        if(otp==code):
            print("otp verified")
        else:
            raise ValueError("The otp you are entered is not correct")


    def PanCard_Verification(self):
        self.pan_number="HUTREI2345"
        if (len(self.pan_number) == 10):
            print("pan card verified")
        else:
            raise ValueError("The entered number is a Inavlid Pan_number")

    def Bank_verification(self):
        self.Account=[]
        self.Account_number=9874269845
        self.Account.append(self.Account_number)                                                                     
        print(self.Account)
        print("Bank account Verified")

    

    def set_Pin(self,number):
        self.pin=number
        
        if (len(self.pin)==4 or len(self.pin) ==6):
            print("your pin is successfully created")
        else:
            raise ValueError("the entered Pin number is not valid")

    def Enter_your_Pin(self,match,pin):
        self.match=match
        self.pin=pin
        if self.match==self.pin:
            print("Finished")
        else:
            raise ValueError("The number entered did not match pin number")

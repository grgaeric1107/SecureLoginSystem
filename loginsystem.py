import hashlib

def clear_terminal():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

class login_system:
    def __init__(self):
     self.user_info={}
     

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register(self,username,password):
        clear_terminal()
        if username in self.user_info:
            print("Username already existed")
        else:
            self.user_info.update({username : self.hash_password(password)})
            print("Registered")
            
    def login(self,username,password):
        clear_terminal()
        hashed_password=self.hash_password(password)
        if username in self.user_info :
            if hashed_password==self.user_info[username]:
             print("Login successful")
            else:
                print("Incorrect password")
        else:
            print("login unsuccessful")
            print("Your Username  isn't registered")
    
    def change_password(self,username,password,newpassword):
        clear_terminal()
        if username in self.user_info:
            h1=self.hash_password(password)
            if h1 == self.user_info[username]:
                self.user_info.update({username : self.hash_password(newpassword)})
                print("password changed")
                print("\n")
            else:
                print("your old password is incorrect")
                print("\n")
                
                
                
l1=login_system()
l1.register("Arik Gurung","Arik12345678")
l1.login("Arik Gurung","Arik12345678")
l1.change_password("Arik Gurung","Arik12345678","Arik123")
l1.login("Arik Gurung","Arik123")




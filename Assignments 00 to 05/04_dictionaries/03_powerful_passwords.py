from hashlib import sha256

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def login(email, stored_logins, password_to_check):
    return stored_logins.get(email) == hash_password(password_to_check)

def main():
    stored_logins = {
        "example@gmail.com": hash_password("password"),
        "code_in_placer@cip.org": hash_password("karel"),
        "student@stanford.edu": hash_password("password")
    }

    print(login("example@gmail.com", stored_logins, "password"))
    print(login("code_in_placer@cip.org", stored_logins, "Karel"))
    print(login("code_in_placer@cip.org", stored_logins, "karel"))   
    print(login("student@stanford.edu", stored_logins, "password"))  
    print(login("student@stanford.edu", stored_logins, "wrong123"))  

if __name__ == '__main__':
    main()

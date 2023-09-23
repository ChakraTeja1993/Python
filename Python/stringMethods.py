import bcrypt
import mysql.connector
password ="chakra@321"
# Function to generate a salt and hash the password
def hash_password(password):
    # Generate a salt
    salt = bcrypt.gensalt()
    
    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    print(salt)
    print(hashed_password)
    
    return salt, hashed_password

hash_password(password)


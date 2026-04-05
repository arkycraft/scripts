import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_hash, password):
    return stored_hash == hash_password(password)

# Example usage
if __name__ == "__main__":
    password = "my_secure_password"
    hashed = hash_password(password)
    print(f"Hashed password: {hashed}")
    # Verify the password
    is_valid = verify_password(hashed, "my_secure_password")
    print(f"Password valid: {is_valid}")
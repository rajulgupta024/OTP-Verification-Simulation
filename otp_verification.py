import random

def generate_otp():
    """Generate a 6-digit OTP randomly."""
    return str(random.randint(100000, 999999))

def send_otp(email, otp):
    """Simulate sending the OTP to the user's email address."""
    print(f"Simulating sending OTP to {email}: {otp}")

def prompt_for_otp():
    """Prompt the user to enter the OTP received in their email."""
    return input("Enter the OTP received: ")

def verify_otp(otp, entered_otp):
    """Verify if the entered OTP matches the generated OTP."""
    return otp == entered_otp

def main():
    email = input("Enter your email address: ")
    
    otp = generate_otp()
    send_otp(email, otp)
    
    attempts = 3
    while attempts > 0:
        entered_otp = prompt_for_otp()
        if verify_otp(otp, entered_otp):
            print("OTP verification successful. Access granted!")
            break
        else:
            print("Invalid OTP. Please try again.")
            attempts -= 1
    else:
        print("You've exceeded the maximum number of attempts. Access denied.")

if __name__ == "__main__":
    main()

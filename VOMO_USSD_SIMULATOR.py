# ================================
# VoMo USSD Simulator
# A Python simulation of a mobile
# money USSD menu system
# Built by: [Nana Annor-Koffie Mensah]
# Date: April 2026
# ================================

import time

# A dictionary was created to store the keypad numbers
ussd_code = {
    "A": "1 2 3",
    "B": "4 5 6",
    "C": "7 8 9",
    "D": "* 0 #"
}

def dial_number():
    # This is the heart of the project.
    # A function was created to make sure the code works
    while True:
        # The while loop makes sure every time a user enters the shortcode or not
        # it gives the user feedback
        type_number = input("Dial the short code to proceed (*188# or type p): ")

        if type_number == "p" or type_number == "*188#":
            print("USSD code running...")
            time.sleep(1)
            print("Unlock more deals on our new VoMo App")
            time.sleep(1)

            # Menu options displayed to the user
            option_1 = [
                "1) Transfer money",
                "2) Momo pay & Pay Bill",
                "3) Airtime & Bundles",
                "4) Allow Cash Out",
                "5) Financial",
                "6) Next",
                "0) Go back"
            ]

            for item in option_1:
                print(item)

            # try/except prevents the program from crashing if user types a letter
            try:
                select_option = int(input("Input your choice: "))
            except ValueError:
                print("Please enter a number, not a letter.")
                continue

            if select_option == 1:
                print("USSD Code running...")
                time.sleep(1)
                print("Transfer money selected...")
                time.sleep(1)
                break

            elif select_option == 2:
                print("USSD Code running...")
                time.sleep(1)
                print("Momo Pay & Pay Bill selected...")
                time.sleep(1)
                break

            elif select_option == 3:
                print("USSD Code running...")
                time.sleep(1)
                print("Airtime & Bundles selected...")
                time.sleep(1)
                break

            elif select_option == 4:
                print("USSD Code running...")
                time.sleep(1)
                print("Allow Cash Out selected...")
                time.sleep(1)
                break

            elif select_option == 5:
                print("USSD Code running...")
                time.sleep(1)
                print("Financial selected...")
                time.sleep(1)
                break

            elif select_option == 6:
                print("USSD Code running...")
                time.sleep(1)
                print("Service is currently unavailable.")
                time.sleep(1)
                break

            elif select_option == 0:
                # Takes the user back to the top of the while loop
                print("Going back...")
                time.sleep(1)
                continue

            else:
                # Handles any number outside the valid range
                print("Invalid option. Please choose 1-6 or 0 to go back.")
                time.sleep(1)
                continue

        else:
            # Handles anything that isn't the shortcode
            print("Invalid code. Please dial *188# or type p to proceed.")
            time.sleep(1)

# ================================
# Program starts here
# ================================
print("Hello, welcome to VoMo! 👋")
time.sleep(1)
print("Please follow the guidelines to access our services.")
time.sleep(1)

# Show the keypad so the user knows what to dial
print("\nVoMo Keypad:")
print("-" * 15)
for num in ussd_code.values():
    print(num)
print("-" * 15)
time.sleep(1)

dial_number()
time.sleep(1)
print("Thank you for using VoMo. Goodbye! 👋")
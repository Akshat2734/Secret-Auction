import os 
print("Welcome to the secret auction")
input_dict = {}
while True:
    yes_or_no = input("Do you want to continue in putting your bidding: ").lower()
    if yes_or_no == 'yes':
        ask_user_for_key = input("What's is your name?\n")
        ask_user_for_value = int(input("What's is your bidding price: "))
        input_dict[f"{ask_user_for_key}"]= ask_user_for_value
        os.system('cls')
    else:
        break 
output = dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=True))
x = list(input_dict.keys())[0]
y = list(input_dict.values())[0]
print(f"Thus the winner is {x} with the bidding price {y}")

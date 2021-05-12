import random

chinese_food = ["Panda Garden", "Main Moon", "China Buffet", "Katana's"]
italian_food = ["Spaghetti", "Lasagna", "Pizza", "rigatoni"]
mexican_food = ["Burrito's", "Taco's", "Los Gallos", "Jaliscos"]
fast_food = ["Wendy's", "Chipoltle", "Popeyes", "Taco Bell"]

cuisine_choice_responses = ["MMMMM...Sounds Good", "Ooooh...Nice", "Ah yes, only the most fattening"]

random_response = random.choice(cuisine_choice_responses)

def welcome():
    print("Hello there, looks like you are having trouble deciding what to eat. I'll help.")
    cuisine_choice = input("Please select what type of cuisine you prefer: \n1 = Chinese\n2 = Mexican\n4 = Fast Food\n7 = Italian\n8 = I Don't Know!\nPlease enter a number: ")
    if cuisine_choice == "1":
        print(random_response+"You should eat at: "+random.choice(chinese_food))
    elif cuisine_choice == "2":
        print(random_response+"You should eat at: "+random.choice(italian_food))
    elif cuisine_choice == "3":
        print(random_response+"You should eat at: "+random.choice(mexican_food))
    elif cuisine_choice == "4":
        print(random_response+"You should eat at: "+random.choice(fast_food))
    elif cuisine_choice == "5":
        random_choice = random.randint(1,5)
    else:
        print("You did not choose one of the options. Please try again. ")
        welcome()


welcome()
        
        
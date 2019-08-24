import math
import sys
from sys import exit

def byebye():
    choice = int(input("\nChoose your fitness calculator:\n 1 - Body Mass Index:\n 2 - Body Adiposity Index:\n 3 - Waist to Height Ratio:\n 4 - VO² MAX:\n 5 - VO² MAX Version 2:\n 6 - One Repetition Maximum\n 7 - Daily Calorie Intake \n 8 - Exit \n\n "))
    if choice == 1:
        main1()
    elif choice == 2:
        main2()
    elif choice == 3:
        main3()
    elif choice == 4:
        main4()
    elif choice == 5:
        main5()
    elif choice == 6:
        main6()
    elif choice == 7:
        main7()
    elif choice == 8:
        sys.exit(0)
   






def main1_intro():
    print('''
    _____  __  __ _____    _____      _            _       _             
    |  _ \|  \/  |_   _|  / ____|    | |          | |     | |            
    | |_) | \  / | | |   | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
    |  _ <| |\/| | | |   | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
    | |_) | |  | |_| |_  | |___| (_| | | (__| |_| | | (_| | || (_) | |   
    |____/|_|  |_|_____|  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                                     
''')


def main1():
    main1_intro()
    get_height = 0.0
    get_weight = 0.0
    body_mass_index = 0.0
    get_height = float(input("Enter your height in meters: "))
    get_weight = float(input("Enter your weight in kilograms: "))
    body_mass_index = round(get_weight/ (get_height * get_height), 1)

    if body_mass_index < 18.5:
        print("A person with a BMI of " + str(body_mass_index) + " is underweight")
        byebye()
    elif body_mass_index > 18.5 and body_mass_index <25:
        print("A person with a BMI of " + str(body_mass_index) + " is normal")
        byebye()
    elif body_mass_index > 25 and body_mass_index <30:
        print("A person with a BMI of " + str(body_mass_index) + " is overweight")
        byebye()
    elif body_mass_index > 30:
        print("A person with a BMI of " + str(body_mass_index) + " is obese")
        byebye()
    else:
        print("Incorrect Inputs")
        byebye()

def main2_intro():
    print('''
  ____          _____    _____      _            _       _             
 |  _ \   /\   |_   _|  / ____|    | |          | |     | |            
 | |_) | /  \    | |   | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 |  _ < / /\ \   | |   | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |_) / ____ \ _| |_  | |___| (_| | | (__| |_| | | (_| | || (_) | |   
 |____/_/    \_\_____|  \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                                                                                                                                                                               
''')



def main2():
    main2_intro()
    get_hip = 0.0
    get_height = 0.0
    body_adiposity_index = 0.0
    get_hip = float(input("Enter your hip circumferance in meters: "))
    get_height = float(input("Enter your height in meters: "))
    body_adiposity_index = (100 * get_hip) / (get_height * math.sqrt(get_height)) - 18
    body_adiposity_index_round = round(body_adiposity_index,1)
    print(str(body_adiposity_index_round)+ str("% body fat"))
    byebye()



def main3_intro():
    print('''
 __          __   _     _     _    _      _       _     _     _____       _   _       
 \ \        / /  (_)   | |   | |  | |    (_)     | |   | |   |  __ \     | | (_)      
  \ \  /\  / /_ _ _ ___| |_  | |__| | ___ _  __ _| |__ | |_  | |__) |__ _| |_ _  ___  
   \ \/  \/ / _` | / __| __| |  __  |/ _ \ |/ _` | '_ \| __| |  _  // _` | __| |/ _ \ 
    \  /\  / (_| | \__ \ |_  | |  | |  __/ | (_| | | | | |_  | | \ \ (_| | |_| | (_) |
     \/  \/ \__,_|_|___/\__| |_|  |_|\___|_|\__, |_| |_|\__| |_|  \_\__,_|\__|_|\___/ 
                                             __/ |                                    
                                            |___/                                                                                                  
''')



def main3():
    main3_intro()
    get_waist = 0.0
    get_height = 0.0
    waist_height_ratio = 0.0
    get_gender = []
    get_waist = float(input("Enter your waist circumferance in inches: "))
    get_height = float(input("Enter your height in inches: "))
    get_gender = str(input("Enter your gender: ").lower())
    waist_height_ratio = get_waist / get_height
    waist_height_ratio_round = round(waist_height_ratio,2)

    if get_gender == "male" and waist_height_ratio < 0.34:
        print("You are a male and underweight")
    elif get_gender == "male" and waist_height_ratio > 0.34 and waist_height_ratio < 0.52:
        print("You are a male and healthy")
    elif get_gender == "male" and waist_height_ratio > 0.53 and waist_height_ratio < 0.57:
        print("You are a male and overweight")
    elif get_gender == "male" and waist_height_ratio > 0.58 and waist_height_ratio < 0.62:
        print("You are a male and very overweight")
    elif get_gender == "male" and waist_height_ratio > 0.63:
        print("You are a male and obese")

    elif get_gender == "female" and waist_height_ratio < 0.34:
        print("You are a female and underweight")
    elif get_gender == "female" and waist_height_ratio > 0.34 and waist_height_ratio < 0.48:
        print("You are a female and healthy")
    elif get_gender == "female" and waist_height_ratio > 0.49 and waist_height_ratio < 0.53:
        print("You are a female and overweight")
    elif get_gender == "female" and waist_height_ratio > 0.54 and waist_height_ratio < 0.57:
        print("You are a female and very overweight")
    elif get_gender == "female" and waist_height_ratio > 0.58:
        print("You are a female and obese")

    print(str(waist_height_ratio_round)+ str(" waist-height ratio"))
    byebye()








def main4_intro():
        print('''
 __      ______    ___                        
 \ \    / / __ \  |_  )                       
  \ \  / / |  | |  / /   _ __ ___   __ ___  __
   \ \/ /| |  | | /___| | '_ ` _ \ / _` \ \/ /
    \  / | |__| |       | | | | | | (_| |>  < 
     \/   \____/        |_| |_| |_|\__,_/_/\_\                                                           
''')




def main4():
    main4_intro()
    get_hrmax = 0.0
    get_hrrest = 0.0
    vo2max_ratio = 0.0
    get_age = 0.0
    get_gender = []
    get_hrmax = float(input("Enter your maximum heart rate: "))
    get_hrrest = float(input("Enter your resting heart rate: "))
    get_age = float(input("Enter your age: "))
    get_gender = str(input("Enter your gender: ").lower())
    vo2max_ratio = 15.3 * (get_hrmax / get_hrrest)
    vo2max_ratio_round = round(vo2max_ratio,2)

    if get_gender == "male" and vo2max_ratio_round < 41 and get_age >= 20 and get_age <= 29:
        print("You are a male with poor health")
    elif get_gender == "male" and vo2max_ratio_round > 42 and vo2max_ratio_round < 45 and get_age >= 20 and get_age >= 29:
        print("You are a male with fair health")
    elif get_gender == "male" and vo2max_ratio_round > 46 and vo2max_ratio_round < 50 and get_age >= 20 and get_age >= 29:
        print("You are a male with good health")
    elif get_gender == "male" and vo2max_ratio_round > 51 and vo2max_ratio_round < 55 and get_age >= 20 and get_age >= 29:
        print("You are a male with excellent health")
    elif get_gender == "male" and vo2max_ratio_round > 56 and get_age >= 20 and get_age >= 29:
        print("You are a male with superior health")

    elif get_gender == "male" and vo2max_ratio_round < 40 and get_age >= 30 and get_age <= 39:
        print("You are a male with poor health")
    elif get_gender == "male" and vo2max_ratio_round > 41 and vo2max_ratio_round < 43 and get_age >= 30 and get_age <= 39:
        print("You are a male with fair health")
    elif get_gender == "male" and vo2max_ratio_round > 44 and vo2max_ratio_round < 47 and get_age >= 30 and get_age <= 39:
        print("You are a male with good health")
    elif get_gender == "male" and vo2max_ratio_round > 48 and vo2max_ratio_round < 53 and get_age >= 30 and get_age <= 39:
        print("You are a male with excellent health")
    elif get_gender == "male" and vo2max_ratio_round > 54 and get_age >= 30 and get_age <= 39:
        print("You are a male with superior health")
    
    elif get_gender == "male" and vo2max_ratio_round < 37 and get_age >= 40 and get_age <= 49:
        print("You are a male with poor health")
    elif get_gender == "male" and vo2max_ratio_round > 38 and vo2max_ratio_round < 41 and get_age >= 40 and get_age <= 49:
        print("You are a male with fair health")
    elif get_gender == "male" and vo2max_ratio_round > 42 and vo2max_ratio_round < 45 and get_age >= 40 and get_age <= 49:
        print("You are a male with good health")
    elif get_gender == "male" and vo2max_ratio_round > 46 and vo2max_ratio_round < 52 and get_age >= 40 and get_age <= 49:
        print("You are a male with excellent health")
    elif get_gender == "male" and vo2max_ratio_round > 53 and get_age >= 40 and get_age <= 49:
        print("You are a male with superior health")

    elif get_gender == "male" and vo2max_ratio_round < 34 and get_age >= 50 and get_age <= 59:
        print("You are a male with poor health")
    elif get_gender == "male" and vo2max_ratio_round > 35 and vo2max_ratio_round < 37 and get_age >= 50 and get_age <= 59:
        print("You are a male with fair health")
    elif get_gender == "male" and vo2max_ratio_round > 38 and vo2max_ratio_round < 42 and get_age >= 50 and get_age <= 59:
        print("You are a male with good health")
    elif get_gender == "male" and vo2max_ratio_round > 43 and vo2max_ratio_round < 49 and get_age >= 50 and get_age <= 59:
        print("You are a male with excellent health")
    elif get_gender == "male" and vo2max_ratio_round > 50 and get_age >= 50 and get_age <= 59:
        print("You are a male with superior health")

    elif get_gender == "male" and vo2max_ratio_round < 30 and get_age >= 60 and get_age <= 69:
        print("You are a male with poor health")
    elif get_gender == "male" and vo2max_ratio_round > 31 and vo2max_ratio_round < 34 and get_age >= 60 and get_age <= 69:
        print("You are a male with fair health")
    elif get_gender == "male" and vo2max_ratio_round > 35 and vo2max_ratio_round < 38 and get_age >= 60 and get_age <= 69:
        print("You are a male with good health")
    elif get_gender == "male" and vo2max_ratio_round > 39 and vo2max_ratio_round < 45 and get_age >= 60 and get_age <= 69:
        print("You are a male with excellent health")
    elif get_gender == "male" and vo2max_ratio_round > 46 and get_age >= 60 and get_age <= 69:
        print("You are a male with superior health")

    elif get_gender == "male" and vo2max_ratio_round < 27 and get_age >= 70 and get_age <= 79:
        print("You are a male with poor health")
    elif get_gender == "male" and vo2max_ratio_round > 28 and vo2max_ratio_round < 30 and get_age >= 70 and get_age <= 79:
        print("You are a male with fair health")
    elif get_gender == "male" and vo2max_ratio_round > 31 and vo2max_ratio_round < 35 and get_age >= 70 and get_age <= 79:
        print("You are a male with good health")
    elif get_gender == "male" and vo2max_ratio_round > 36 and vo2max_ratio_round < 41 and get_age >= 70 and get_age <= 79:
        print("You are a male with excellent health")
    elif get_gender == "male" and vo2max_ratio_round > 42 and get_age >= 70 and get_age <= 79:
        print("You are a male with superior health")
    elif get_gender == "male" and get_age >= 80:
        print("You are too old!")
    elif get_age < 19:
        print("You are too young!")

#Female
    elif get_gender == "female" and vo2max_ratio_round < 35 and get_age >= 20 and get_age <= 29:
        print("You are a female with poor health")
    elif get_gender == "female" and vo2max_ratio_round > 36 and vo2max_ratio_round < 39 and get_age >= 20 and get_age >= 29:
        print("You are a female with fair health")
    elif get_gender == "female" and vo2max_ratio_round > 40 and vo2max_ratio_round < 43 and get_age >= 20 and get_age >= 29:
        print("You are a female with good health")
    elif get_gender == "female" and vo2max_ratio_round > 44 and vo2max_ratio_round < 49 and get_age >= 20 and get_age >= 29:
        print("You are a female with excellent health")
    elif get_gender == "female" and vo2max_ratio_round > 50 and get_age >= 20 and get_age >= 29:
        print("You are a female with superior health")

    elif get_gender == "female" and vo2max_ratio_round < 33 and get_age >= 30 and get_age <= 39:
        print("You are a female with poor health")
    elif get_gender == "female" and vo2max_ratio_round > 34 and vo2max_ratio_round < 36 and get_age >= 30 and get_age <= 39:
        print("You are a female with fair health")
    elif get_gender == "female" and vo2max_ratio_round > 37 and vo2max_ratio_round < 40 and get_age >= 30 and get_age <= 39:
        print("You are a female with good health")
    elif get_gender == "female" and vo2max_ratio_round > 41 and vo2max_ratio_round < 45 and get_age >= 30 and get_age <= 39:
        print("You are a female with excellent health")
    elif get_gender == "female" and vo2max_ratio_round > 46 and get_age >= 30 and get_age <= 39:
        print("You are a female with superior health")
    
    elif get_gender == "female" and vo2max_ratio_round < 31 and get_age >= 40 and get_age <= 49:
        print("You are a female with poor health")
    elif get_gender == "female" and vo2max_ratio_round > 32 and vo2max_ratio_round < 34 and get_age >= 40 and get_age <= 49:
        print("You are a female with fair health")
    elif get_gender == "female" and vo2max_ratio_round > 35 and vo2max_ratio_round < 38 and get_age >= 40 and get_age <= 49:
        print("You are a female with good health")
    elif get_gender == "female" and vo2max_ratio_round > 39 and vo2max_ratio_round < 44 and get_age >= 40 and get_age <= 49:
        print("You are a female with excellent health")
    elif get_gender == "female" and vo2max_ratio_round > 45 and get_age >= 40 and get_age <= 49:
        print("You are a female with superior health")

    elif get_gender == "female" and vo2max_ratio_round < 24 and get_age >= 50 and get_age <= 59:
        print("You are a female with poor health")
    elif get_gender == "female" and vo2max_ratio_round > 25 and vo2max_ratio_round < 28 and get_age >= 50 and get_age <= 59:
        print("You are a female with fair health")
    elif get_gender == "female" and vo2max_ratio_round > 29 and vo2max_ratio_round < 30 and get_age >= 50 and get_age <= 59:
        print("You are a female with good health")
    elif get_gender == "female" and vo2max_ratio_round > 31 and vo2max_ratio_round < 34 and get_age >= 50 and get_age <= 59:
        print("You are a female with excellent health")
    elif get_gender == "female" and vo2max_ratio_round > 35 and get_age >= 50 and get_age <= 59:
        print("You are a female with superior health")

    elif get_gender == "female" and vo2max_ratio_round < 25 and get_age >= 60 and get_age <= 69:
        print("You are a female with poor health")
    elif get_gender == "female" and vo2max_ratio_round > 26 and vo2max_ratio_round < 28 and get_age >= 60 and get_age <= 69:
        print("You are a female with fair health")
    elif get_gender == "female" and vo2max_ratio_round > 29 and vo2max_ratio_round < 31 and get_age >= 60 and get_age <= 69:
        print("You are a female with good health")
    elif get_gender == "female" and vo2max_ratio_round > 32 and vo2max_ratio_round < 35 and get_age >= 60 and get_age <= 69:
        print("You are a female with excellent health")
    elif get_gender == "female" and vo2max_ratio_round > 36 and get_age >= 60 and get_age <= 69:
        print("You are a female with superior health")

    elif get_gender == "female" and vo2max_ratio_round < 23 and get_age >= 70 and get_age <= 79:
        print("You are a female with poor health")
    elif get_gender == "female" and vo2max_ratio_round > 24 and vo2max_ratio_round < 26 and get_age >= 70 and get_age <= 79:
        print("You are a female with fair health")
    elif get_gender == "female" and vo2max_ratio_round > 27 and vo2max_ratio_round < 29 and get_age >= 70 and get_age <= 79:
        print("You are a female with good health")
    elif get_gender == "female" and vo2max_ratio_round > 30 and vo2max_ratio_round < 35 and get_age >= 70 and get_age <= 79:
        print("You are a female with excellent health")
    elif get_gender == "female" and vo2max_ratio_round > 36 and get_age >= 70 and get_age <= 79:
        print("You are a female with superior health")
    elif get_gender == "female" and get_age >= 80:
        print("You are too old!")


    print(str(vo2max_ratio_round)+ str(" ml/kg/min"))
    byebye()










def main5_intro():
    print('''
 __      ______  ___   __  __             __      __           _               ___  
 \ \    / / __ \|_  ) |  \/  |            \ \    / /          (_)             |__ \ 
  \ \  / / |  | |/ /  | \  / | __ ___  __  \ \  / /__ _ __ ___ _  ___  _ __      ) |
   \ \/ /| |  | /___| | |\/| |/ _` \ \/ /   \ \/ / _ \ '__/ __| |/ _ \| '_ \    / / 
    \  / | |__| |     | |  | | (_| |>  <     \  /  __/ |  \__ \ | (_) | | | |  / /_ 
     \/   \____/      |_|  |_|\__,_/_/\_\     \/ \___|_|  |___/_|\___/|_| |_| |____|                                                          
''')



def main5():
    main5_intro()
    get_hrrest = 0.0
    vo2max_ratio = 0.0
    get_weight = 0.0
    get_age = 0.0

    get_age = float(input("Enter your age: "))
    get_weight = float(input("Enter your weight in kilograms: "))
    get_hrrest = float(input("Enter your resting heart rate: "))
    vo2max_ratio = 3.542 + (-0.014 * get_age) + (0.015 * get_weight) + (-0.011 * get_hrrest)
    vo2max_ratio_round = round(vo2max_ratio,2)

    print(str(vo2max_ratio_round)+ str(" VO² Max"))
    byebye()






def main6_intro():
    print('''
   ____               _____                 _   _ _   _               __  __            _                            
  / __ \             |  __ \               | | (_) | (_)             |  \/  |          (_)                           
 | |  | |_ __   ___  | |__) |___ _ __   ___| |_ _| |_ _  ___  _ __   | \  / | __ ___  ___ _ __ ___  _   _ _ __ ___   
 | |  | | '_ \ / _ \ |  _  // _ \ '_ \ / _ \ __| | __| |/ _ \| '_ \  | |\/| |/ _` \ \/ / | '_ ` _ \| | | | '_ ` _ \  
 | |__| | | | |  __/ | | \ \  __/ |_) |  __/ |_| | |_| | (_) | | | | | |  | | (_| |>  <| | | | | | | |_| | | | | | | 
  \____/|_| |_|\___| |_|  \_\___| .__/ \___|\__|_|\__|_|\___/|_| |_| |_|  |_|\__,_/_/\_\_|_| |_| |_|\__,_|_| |_| |_| 
                                | |                                                                                  
                                |_|                                                                                  

    ''')


def main6():
    main6_intro()
    get_weight = 0.0
    get_reps = 0.0
    max_weight = 0.0

    get_weight = float(input("Enter the weight lifted: "))
    get_reps = float(input("Enter the number or repetitions: "))
    max_weight = get_weight * (36 / (37 - get_reps))
    max_weight_round = round(max_weight,2)
    print(max_weight_round)
    byebye()








def main7_intro():
    print (r"""
  _____        _ _          _____      _            _        _____       _        _        
 |  __ \      (_) |        / ____|    | |          (_)      |_   _|     | |      | |       
 | |  | | __ _ _| |_   _  | |     __ _| | ___  _ __ _  ___    | |  _ __ | |_ __ _| | _____ 
 | |  | |/ _` | | | | | | | |    / _` | |/ _ \| '__| |/ _ \   | | | '_ \| __/ _` | |/ / _ \
 | |__| | (_| | | | |_| | | |___| (_| | | (_) | |  | |  __/  _| |_| | | | || (_| |   <  __/
 |_____/ \__,_|_|_|\__, |  \_____\__,_|_|\___/|_|  |_|\___| |_____|_| |_|\__\__,_|_|\_\___|
                    __/ |                                                                  
                   |___/                                                                  
    """)





def main7():
    main7_intro()
    get_gender = []
    get_weight = 0.0
    get_height = 0.0
    get_age = 0.0
    get_activity = []
    calorie1 = 0.0

    get_weight = float(input("Enter your weight in kilograms: "))
    get_height = float(input("Enter your height in centimeters: "))
    get_age = float(input("Enter your age: "))
    get_activity = float(input("Enter the number corresponding to your activity\n 1 - Little to no exercise: \n 2 - Light exercise (1-3 days per week): \n 3 - Moderate exercise (3-5 days per week): \n 4 - Heavy exercise (6-7 days per week): \n 5 - Very Heavy exercise (Twice per day, extra heavy workouts):  \n"))

    calorie1_rev = 88.362 + (13.397 * get_weight) + (4.799 * get_height) - (5.677 * get_age)
    calorie1_rev_no_exercise = (calorie1_rev) * 1.2
    calorie1_rev_little_exercise = (calorie1_rev) * 1.375
    calorie1_rev_moderate_exercise = (calorie1_rev) * 1.55
    calorie1_rev_heavy_exercise = (calorie1_rev) * 1.725
    calorie1_rev_vheavy_exercise = (calorie1_rev) * 1.9

    calorie1_rev_no_exercise_round = round(calorie1_rev_no_exercise,1)
    calorie1_rev_little_exercise_round = round(calorie1_rev_little_exercise,1)
    calorie1_rev_moderate_exercise_round = round(calorie1_rev_moderate_exercise,1)
    calorie1_rev_heavy_exercise_round = round(calorie1_rev_heavy_exercise,1)
    calorie1_rev_vheavy_exercise_round = round(calorie1_rev_vheavy_exercise,1)


    if get_activity == (1):
        print(str("You need ")+ str(calorie1_rev_no_exercise_round) + str(" Daily Calories"))
        byebye()
    elif get_activity == (2):
        print(str("You need ")+ str(calorie1_rev_little_exercise_round) + str(" Daily Calories"))
        byebye()
    elif get_activity == (3):
        print(str("You need ")+ str(calorie1_rev_moderate_exercise_round) + str(" Daily Calories"))
        byebye()
    elif get_activity == (4):
        print(str("You need ")+ str(calorie1_rev_heavy_exercise_round) + str(" Daily Calories"))
        byebye()
    elif get_activity == (5):
        print(str("You need ")+ str(calorie1_rev_vheavy_exercise_round) + str(" Daily Calories"))
        byebye()







try:
#Enter 1 for BMI, 2 for BAI, 3 for WHR, 4 for VO²Max, 5 for VO²Max Version 2, 6 for 1RM, 7 for Daily Calorie Intake.
  choice = int(input("\nChoose your fitness calculator:\n 1 - Body Mass Index:\n 2 - Body Adiposity Index:\n 3 - Waist to Height Ratio:\n 4 - VO² MAX:\n 5 - VO² MAX Version 2:\n 6 - One Repetition Maximum\n 7 - Daily Calorie Intake \n \n "))
  if choice == 1:
      main1()
  elif choice == 2:
      main2()
  elif choice == 3:
      main3()
  elif choice == 4:
      main4()
  elif choice == 5:
      main5()
  elif choice == 6:
      main6()
  elif choice == 7:
      main7()

  else:
    print("Invalid input.")
    sys.exit()
except ValueError:
  print("Invalid input.")
  sys.exit()
#global variables and imports


#getting users imputs as height and weight 
def get_users_inpute():
    weight = float(input("enter your weight (kg): "))
    height = float(input("enter your height (m): "))
    return weight,height

#calculate BMI
def calculate_bmi(weight,height):
    return weight / (height**2)
    
#get the BMI result
def get_bmi_resulte(bmi):
    print(f"bmi: {bmi}\nresult:")
    if bmi < 18.5:
        print ("Under Weight!")
    elif 18.5<= bmi <25:
        print ("Normal")
    elif 25<= bmi <30:
        print ("Over Weight!")
    elif 30<= bmi <35:
        print ("Obese!")
    else:
        print("Extermely Obese")

#create main function to run
def main():
    weight,height = get_users_inpute()
    bmi = calculate_bmi(weight,height)
    get_bmi_resulte(bmi)

if __name__ == "__main__":
    main()
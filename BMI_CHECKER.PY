# CREATING A BMI CALCULATOR :-

Weight=float(input("Enter you Weight: "))  #taking the weight from user 

Height=float(input("Enter your Height in meters: "))  # taking the height from user

def calculate_bmi(Weight:float,Height:float)->float:
    ''' return bmi given weight(kg) and height(meter)'''

    return Weight/(Height**2)

def classify_bmi(bmi:float)->int:
    #Checking or classifying the cateogary of user in bmi
    '''return BMI cateogary based on value'''
    if bmi<18.5:
        return "Underweight"   # return Underweight
    elif bmi<25:
        return "Normal"  # return normal
    elif bmi<30:
        return "Overweight"  # return Overweight
    else:
        return "Obese"  # return Obese
    
BMI=calculate_bmi(Weight, Height)  # calculate bmi
cateogary=classify_bmi(BMI)
# cateogary of user in bmi

print(f"Your BMI is {BMI:.2f} and in {cateogary} cateogary")
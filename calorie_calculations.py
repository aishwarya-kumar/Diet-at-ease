

# Functions to 



def bmi_calc(height,weight, gender):
    bmi = round(float(weight /(height*height))*10000.00, 1)
    
    if bmi <= 18.4:
        bmi_interpretation = "Underweight"
        goal = "weight_gain"
    elif bmi >= 18.5 and bmi <= 24.9:
        bmi_interpretation = "Normal"
        goal = "maintain_weight"
    elif bmi >= 25.0 and bmi<= 29.9:
        bmi_interpretation = "Overweight"
        goal = "weight_loss"
    elif bmi>= 30.0:
        bmi_interpretation = "Obesity"
        goal = "strict_weight_loss"
    else:
        print("Error: bmi out of bounds")
        
    return bmi, bmi_interpretation, goal

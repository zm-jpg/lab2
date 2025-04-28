def calculate_bmi(height, weight):
    print("height:"+str(height))
    print("weight:"+str(weight))
    bmi = weight/(height**2)
    return bmi

def classify_bmi(bmi_value):
    if(bmi_value<18.5):
        print("underweight")
    elif(bmi_value>=18.5 and bmi_value<=25.0):
        print("normal weight")
    else:
        print("overweight")

def main():
 bmi_output=calculate_bmi(1.8,80)
 print("bmi:"+str(bmi_output))
 classify_bmi(bmi_output)

if __name__ == "__main__":
 main()

def display_main_menu():
    print("Enter some numbers separated by commas")
    return

def get_user_input():
    print("enter temperature:")
    temp= input('Enter temperature values:')
    inputs=temp.split(",")
    print('temp='+str(inputs))
    thislist = [float(i) for i in inputs]
    return thislist


def calc_average(numberlist):
    average=sum(numberlist)/len(numberlist)
    print("average is:"+ str(average))
    return

def calc_max(numlist):
    largest=max(numlist)
    print("maximum number is:"+str(largest))

def calc_min(list):
    lowest=min(list)
    print("minimum number is:"+str(lowest))
    


def main():
    display_main_menu()
    x= get_user_input()
    calc_average(x)
    calc_max(x)
    calc_min(x)

if __name__ == "__main__":
    main()
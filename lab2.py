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
    lowest=min(numlist)
    print("minimum number is:"+str(lowest))
    return

def calc_median(listorder):
    ascending=listorder.sort()
    n=len(listorder)
    if n%2==0:
        median= ((listorder[(n//2-1)]+listorder[n//2])/2)
    else:
        median=(n+1)/2
    print("The median is:"+str(median))
    return

def main():
    display_main_menu()
    list= get_user_input()
    calc_average(list)
    calc_max(list)
    calc_median(list)

    
if __name__ == "__main__":
    main()
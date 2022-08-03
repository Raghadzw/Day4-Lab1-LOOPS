for num in range(45,210):
    if num==100:
        continue
    if num==205:
        break
    print(num)




while True:
    x = input("What is the product of 7*24 ?")
    if int(x) == 168:
        print("You answered this Question correctly")
        break
    else:
        print("Your Answer is wrong try again..")
        continue


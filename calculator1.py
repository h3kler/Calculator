#made by sushant kumar, 9th A



#-*-coding:utf8;-*-
#qpy:console


#modules
import time


#variable settings
l_mai = "-----------------------------------------------------------"
l_sec = "----------------------------"
l_thi = "."
l_sess = "----------------------------------------------------------------------------------------------------------------------"
a = True
per = 100

#Welcome & Name

print("Hello!!")
time.sleep(0.5)
print("Please tell us your name")
name =  input('=>')
print(f"welcome {name} to this calculator! \n")
time.sleep(2)
print("**note:- only 2 numbers can be operated at once** \n")
time.sleep(1)
print("**note:- only normal integers are allowed.. no decimal numbers or fractions are allowed..**")
print(f'{l_mai}\n')

while a==True:
    print('choose operator:-')
    print('add, subtract, multiply, percentage')
    o = input("=>")
    if o=="add":
        print(l_mai)
        print("YOU ARE GOING TO ADD")
        print(l_mai)
        print("Enter first number:")
        num1 = int(input("=>"))
        print("Enter second number:")
        num2 = int(input("=>"))
        print(f"Your first number is {num1} and second number is {num2} which is now going to be operated")
        print(l_thi)
        time.sleep(1)
        print(l_thi)
        time.sleep(1)
        print(l_thi)
        print('\n')
        print(l_sec)
        print(f'YOUR ANSWER IS {num1+num2}')
        print(l_sec)
        print('------Session ends--------- \n')
        print('Do you want to exit? yes/no')
        exit = input("=>")
        if exit=="yes":
            break
        if exit=="no":
            print(f'{l_sess} \n')
            continue
        else :
            print('Wrong input!')
            print('exiting')
            print('.')
            time.sleep(1)
            print('.')
            break
    if o=="subtract":
        print(l_mai)
        print("YOU ARE GOING TO SUBTRACT")
        print(l_mai)
        print("Enter first number:")
        num1 = int(input("=>"))
        print("Enter second number:")
        num2 = int(input("=>"))
        print(f"Your first number is {num1} and second number is {num2} which is now going to be operated")
        print(l_thi)
        time.sleep(1)
        print(l_thi)
        time.sleep(1)
        print(l_thi)
        print('\n')
        print(l_sec)
        print(f'YOUR ANSWER IS {num1-num2}')
        print(l_sec)
        print('------Session ends--------- \n')
        print('Do you want to exit? yes/no')
        exit = input("=>")
        if exit=="yes":
            break
        if exit=="no":
            print(f'{l_sess} \n')
            continue
        else :
            print('Wrong input!')
            print('exiting')
            print('.')
            time.sleep(1)
            print('.')
            break
    if o=="multiply":
        print(l_mai)
        print("YOU ARE GOING TO MULTIPLY")
        print(l_mai)
        print("Enter first number:")
        num1 = int(input("=>"))
        print("Enter second number:")
        num2 = int(input("=>"))
        print(f"Your first number is {num1} and second number is {num2} which is now going to be operated")
        print(l_thi)
        time.sleep(1)
        print(l_thi)
        time.sleep(1)
        print(l_thi)
        print('\n')
        print(l_sec)
        print(f'YOUR ANSWER IS {num1*num2}')
        print(l_sec)
        print('------Session ends--------- \n')
        print('Do you want to exit? yes/no')
        exit = input("=>")
        if exit=="yes":
            break
        if exit=="no":
            print(f'{l_sess}\n')
            continue
        else :
            print('Wrong input!')
            print('exiting')
            print('.')
            time.sleep(1)
            print('.')
            break
    if o=="divide":
        print(l_mai)
        print("YOU ARE GOING TO DIVIDE")
        print(l_mai)
        print("Enter first number:")
        num1 = int(input("=>"))
        print("Enter second number:")
        num2 = int(input("=>"))
        print(f"Your first number is {num1} and second number is {num2} which is now going to be operated")
        print(l_thi)
        time.sleep(1)
        print(l_thi)
        time.sleep(1)
        print(l_thi)
        print('\n')
        print(l_sec)
        print(f'YOUR ANSWER IS {num1/num2}')
        print(l_sec)
        print('------Session ends--------- \n')
        print('Do you want to exit? yes/no')
        exit = input("=>")
        if exit=="yes":
            break
        if exit=="no":
            print(f'{l_sess}\n')
            continue
        else :
            print('Wrong input!')
            print('exiting')
            print('.')
            time.sleep(1)
            print('.')
            break
    if o=="percentage":
        print(l_mai)
        print("YOU ARE GOING TO GET PERCENTAGE")
        print(l_mai)
        print("Enter numerator:")
        num1 = int(input("=>"))
        print("Enter denominator:")
        num2 = int(input("=>"))
        print(f"The numerator is {num1} and denominator is {num2} which is now going to be operated")
        print(l_thi)
        time.sleep(1)
        print(l_thi)
        time.sleep(1)
        print(l_thi)
        print('\n')
        print(l_sec)
        print(f'YOUR ANSWER IS {num1/num2*100}%')
        print(l_sec)
        print('------Session ends--------- \n')
        print('Do you want to exit? yes/no')
        exit = input("=>")
        if exit=="yes":
            break
        if exit=="no":
            print(f'{l_sess} \n')
            continue
        else :
            print('Wrong input!')
            print('exiting')
            print('.')
            time.sleep(1)
            print('.')
            break
    else:
        print('wrong input')
        print('exiting')
        print(l_thi)
        time.sleep(1)
        print(l_thi)
        time.sleep(1)
        print(l_thi)
        break
        
#END....
        
        
        
    
    


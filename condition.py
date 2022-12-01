# 1.  if statements

num=5
if num<10:
    print("num is smaller than 10")
a= 7
b=0

if a>b:
     print("a is greater than b")

if "python" in ["java","python","react"]:
    print("true")

if "ball" in ["spoon","plate","ball","knife"]:
    print("true")

# example
# you have written an exam with total score of 100 and if your score is above or equal to 60 then you will be considered as PASS in the exam
my_score=80
passing_score=60
if my_score >= passing_score:
    print("congratulations you PASSED")

# print("congratulations anyways")


# 2. if-else statements

num=5
if num > 10:
    print("number is greater than 10")
else:
    print("number is less than 10")

#3. elif statements

# it is similar to the if- else statement but it executes multiple statements
num=10
if num==0:
    print("number is zero")
elif num > 5:
    print("number is greater than 5")
else:
    print("number is smaller than 5")

#4. nested if else statements

#  this means that an if statement or an if else  statement is present inside another if or if else block. this is just to help us us check multiple conditions too
# example 1
num= 5
if num>0:
    print("number is bigger than 0")
if num< 10 :
    print("number is less than 10")

# example 2
num=7
if num != 0:
            if num > 0:
                        print("number is greater than 0")

# example 3
x=10
if x==10:
    if x<20:
        print(x,"is smaller than 20")
    if x < 20:
        print(x,"is smaller than 21")

# example 4
num=7
if num != 0:
            if num > 0:
                        print("number is greater")
            else:
                        print("number is lesser")            
else:
            print("number is zero")

# 5. elif ladder

print("hello web class")
Name = input ("Enter a name: ")
weight = int(input("Enter your weight: "))
if weight <=18:
    print (Name,"is a child")
elif weight<=20:
    print (Name,"is a teenager")
elif weight<=24:
    print (Name,"is an adult")
elif weight>=25:
    print (Name, "is an elderly person")
else:
    print (Name, "is an obesity")


#conditinal if statement on a single line

# we could also write an if statement with the expression and one  statement or multiple statement on the same line without worrying bout indentations but they should be seperated by semicolons
# example 1
num=7
if num>0: print("number is greater than zero")

# example 2
# x=5
# if x==5: print("yes x is equal to 5");  print("i hope you understand it now")
# elif x!=5: print("no x is not equal to 5"); print("hello everyone") 
# else: print("sorry this is wrong")

#  example 3
a =10
if (a): print("the given value of a is:"); print(a)

# example 4
if "a" in "fruits": print("apple"); print("orange")
else: print("mango"); print("grapes")

# example 5
num1=10
num2=20
num3=30
if (num1==10 and num2== 20 and  num3==30):
    print("all the conditions are true")

# additionally we have the pass in if statements 
# if statements cant be empty,but if for any reason we dont have a statement we can use pass so as to avoid getting an error 
a=33
b=200
if b>a:
    pass
else:
    print("sorry") 

  

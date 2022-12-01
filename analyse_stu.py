import json
#  if you have to import the json function for it to read as json instead of text,because text reads character by character
# the "student.json" is seen as a text file until you specify 

studentdata=open("student.json","r")
student=json.load(studentdata)
print(student)
stu_export=[]
# to read through an array,you iriterate using the loop function
# this picks out the value of the variable "name in the json file"
for stu in student:
    point=0
    # print(stu["name"])
    # print(stu["phonenumber"])
    if stu["attendance"]["week1"]["module1"]== True:
        point+=1 
    if stu["attendance"]["week1"]["module2"]== True:
        point+=1
    if stu["attendance"]["week2"]["module1"]== True:
        point+=1
    if stu["attendance"]["week2"]["module2"]== True:
        point+=1
    if stu["attendance"]["week3"]["module1"]== True:
        point+=1
    if stu["attendance"]["week3"]["module2"]== True:
        point+=1
    if stu["attendance"]["week4"]["module1"]== True:
        point+=1
    if stu["attendance"]["week4"]["module2"]== True:
        point+=1       
    print(stu["name"],"with phone number",stu["phone"],"has",point,"in attendance")
   
# this puts the export into a variable called export, and the export into a list called stu_Export
    export=stu["name"], "with phone number " , stu["phone"], "has ", point, "points"
    stu_export.append(export)

print(stu_export)

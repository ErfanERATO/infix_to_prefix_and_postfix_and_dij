# ele => برای مقایسه لیست هاست
# append() => این متد برای اضافه کردن یک آیتم به یک لیست موجود میباشد
# pop() => یک تابع داخلی هست که یا اخرین آیتم لیست رو حذف میکنه یا آیتمی با ایندکسی که به اون دادیم
# len() => برای ما طول استرینگ رو برمیگردونه
# end => برای اضافه کردن هر رشته تو انتهای خروجی دستور چاپ در پایتون استفاده می شود end  پارامتر
# elif =>استفاده میکنیم elif چندین شرط بیان کنیم از else و if یا بین if اگر ما بخوایم بعد از


import operator

output = []
operator = []

# اولویت بندی ها
priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

# وارد کردن عبارت infix
# و ریختن اون تو یک متغییر
print("___________________________________")
experetion = input("Enter infix expration: ")
print("___________________________________")

# expration داخل  X  به ازای هر
for x in experetion:

    #ابتدا باید پرانتز گذاری بشه از چپ به راست
    #(append) پرانتز های باز وارد پشته میشن 
    if(x == '('):
        operator.append(x)
    #میشن و در خروجی نوشته میشن pop با رسیدن به پرانتز بسته محتوای پشته تا رسیدن به اولین پرانتز 
    elif(x == ')'):
        while(operator[-1] != '('):
            ele = operator.pop()
            output.append(ele)
        operator.pop()
    elif(x == '^' or x == '*' or x == '/' or x == '+' or x == '-'):
        if(len(operator) > 0):
            while(priority[operator[-1]] >= priority[x]):
                ele = operator.pop()
                output.append(ele)
                if(len(operator) == 0):
                    break
        operator.append(x)
    else:
        output.append(x)
while(len(operator) != 0):
    ele = operator.pop()
    output.append(ele)

# پرینت گرفتن خروجی ها
print("the infix expration is = ", experetion)
print("the Postfix expration is =", end=' ')
for ele in output:
    print(ele, end='')

# __________________________________________________________________________________________


output = []
operator = []

# اولویت بندی ها
priority2 = {')': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

# وارد کردن عبارت infix
# و ریختن اون تو یک متغییر
print("\n___________________________________")
experation = input("Enter infix expration: ")
print("___________________________________")

# expration داخل  i  به ازای هر
#منفی به این معنی هست که از آخر شروع بشه  index
#-1یعنی از اخرین آیتم شروع بشه
#-2 یعنی از آیتم یکی مونده به آخر شروع بشه
#[::-1]یعنی از آخر یکی یکی کم کن
#ابتدا باید پرانتز گذاری بشه از راست به چپ
#(append) پرانتز های باز وارد پشته میشن 
for i in experation[::-1]:
    if(i == ')'):
        operator.append(i)
    #میشن و در خروجی نوشته میشن pop با رسیدن به پرانتز بسته محتوای پشته تا رسیدن به اولین پرانتز 
    elif(i == '('):
        while(operator[-1] != ')'):
            ele = operator.pop()
            output.append(ele)
        operator.pop()
    elif(i == '^' or i == '*' or i == '/' or i == '+' or i == '-'):
        if(len(operator) > 0):
            while(priority2[operator[-1]] > priority2[i]):
                ele = operator.pop()
                output.append(ele)
                if(len(operator) == 0):
                    break
        operator.append(i)
    else:
        output.append(i)
if(len(operator) > 0):
    while(len(operator) != 0):
        ele = operator.pop()
        output.append(ele)

print("the infix expration is = ", experation)
print("the Pretfix expration is =", end=' ')
for ele in output[::-1]:
    print(ele, end='')

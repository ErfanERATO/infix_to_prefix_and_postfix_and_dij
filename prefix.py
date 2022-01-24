# def => یک کیوورد برای تعریف فانکشن
# items() =>key_value برای برگردوندن یک لیست با تمام
# size() => تعداد المان های موجود را در امتداد یک مسیر مشخص نمایش میدهد
# reverse() => جای آبجکت های یم لیست رو برعکس میکنه
# __init__() => هربار که یک شئ از یک کلاس ایجاد میشود این متد فراخوانی میشود این متد
# به کلاس اجازه میدهد تا ویژگی های شئ رو مقدار دهی اولیه کنه و فقط در کلاس ها استفاده میشه
# len() => برای ما طول استرینگ رو برمیگردونه
# pop() => یک تابع داخلی هست که یا اخرین آیتم لیست رو حذف میکنه یا آیتمی با ایندکسی که به اون دادیم
# push() => یک تابع هست که در پشته یک المان رو به آخر پشته یا ایندکسی که میدیم اضافه میکنه
# isalpha() => برمیگردونه اگر تمام کاراکتر های وارد شده جزو حروف الفبا باشه true برای ما
# append() => این متد برای اضافه کردن یک آیتم به یک لیست موجود میباشد


class infix_to_prefix:

    # اولویت بندی ها
    priority = {'^': 5, '*': 4, '/': 4, '+': 3, '-': 3, '(': 2, ')': 1}

    def __init__(self):
        self.items = []
        self.size = -1

    def push(self, value):
        self.items.append(value)
        self.size += 1

    def pop(self):
        if self.isempty():
            return 0
        else:
            self.size -= 1
            return self.items.pop()

    def isempty(self):
        if(self.size == -1):
            return True
        else:
            return False

    def seek(self):
        if self.isempty():
            return False
        else:
            return self.items[self.size]

    def is0perand(self, i):
        if i.isalpha() or i in '1234567890':
            return True
        else:
            return False

    def reverse(self, expration):
        revers = ""
        for i in expration:
            if i is '(':
                i = ')'
            elif i is ')':
                i = '('
            revers = i+revers
        return revers

    def infixtoprefix(self, expration):
        prefix = ""
        # print('prefix expression after every iteration is:')
        for i in expration:
            if(len(expration) % 2 == 0):
                print("*Incorrect infix expration*")
                return False
            elif(self.is0perand(i)):
                prefix += i
            elif(i in '+-*/^'):
                while(len(self.items) and self.priority[i] < self.priority[self.seek()]):
                    prefix += self.pop()
                self.push(i)
            elif i is '(':
                self.push(i)
            elif i is ')':
                o = self.pop()
                while o != '(':
                    prefix += o
                    o = self.pop()
            # print(prefix)

        while len(self.items):
            if(self.seek() == '('):
                self.pop()
            else:
                prefix += self.pop()
                # print(prefix)
        return prefix


x = infix_to_prefix()
print("___________________________________")
expration = input('enter the expression =>')
print("___________________________________")
revers = ""
revers = x.reverse(expration)
# print(revers)
result = x.infixtoprefix(revers)
if (result != False):

    prefix = x.reverse(result)
    # print("the prefix expr of :", expration, "is", prefix)
    print("the infix expration is :", expration)
    print("the prefix expration is :", prefix)
    print("___________________________________")
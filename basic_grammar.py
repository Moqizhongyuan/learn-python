# =========================================
# 1. 数据类型
# =========================================

# 整数
age = 18
# 浮点数
height = 185.6
# 字符串
name = "Tom"
# 布尔值
is_student = True
# None
empty_value = None

print(age)
print(height)
print(name)
print(is_student)
print(empty_value)
print('\n')

# =========================================
# 2. 运算符
# =========================================

a = 7
b = 4

# 算数运算
print(a + b) # 加
print(a - b) # 减
print(a * b) # 乘
print(a / b) # 除
print(a % b) # 取余
print(a // b) # 整除
print(a ** b) # 幂运算
print('\n')

# 比较运算
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print('\n')

# 逻辑运算符
print(True and False)
print(True or False)
print(not True)
print('\n')

# =========================================
# 3. 分支和循环
# =========================================

score = 85

# if/elif/else
if score >= 90:
  print("great")
elif score >= 80:
  print("not bad")
else: 
  print("bad")
print('\n')

# for 循环
for i in range(5):
  print(f"for: {i}")
print('\n')

# while 循环
count = 0

while count < 5:
  print(f"while: {count}")
  count += 1
print('\n')

# =========================================
# 4. 数组（Python 中叫 list）
# =========================================

numbers = [1, 2, 3, 4, 5]

# 增
numbers.append(99.1)

# 删
numbers.remove(3)

# 改
numbers[1] = 0

# 查
print(numbers[1])

#遍历
for i in numbers:
  print(f"num: {i}")

print(numbers)

print('\n')

# =========================================
# 5. 函数
# =========================================

# 无返回值函数
def say_hello():
  print("hello")

say_hello()

print('\n')

# 有参数函数
def add(a, b):
  return a + b

print(add(10, 20))

print('\n')

def greet(name = "Tom"):
  print(f"hello, {name}")

greet()
greet(name='Alice')
greet("Frank")

print('\n')


# =========================================
# 6. 结构体或类
# =========================================

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def introduce(self):
    print(f"Hello, my name is {self.name}, age is {self.age}")

p = Person("Tom", 18)

p.introduce()
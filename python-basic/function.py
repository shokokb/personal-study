# coding: UTF-8
def f(x):
	return 2 * x

def swap (x, y):
	return y, x

print f(3)

print swap(3, 4)

print len("Hello")
print str(100)
print int("5")
print float(100)

try :
	print int("Prince")
except ValueError:
	print "Exception occurred"
# else:
# 	print "OK"
finally:
	print "Done!"

print "====="
# 標準入力
# age_str = input("Enter your age:")
# age = int(age_str)
# if age < 20:
# 	print "You are young"
# else:
# 	print "You are old"
print "====="

def odd(x):
	return x % 2 != 0

def odd_str(x):
	if odd(x):
		return "奇数"
	else:
		return "偶数"

print(odd_str(2))
print(odd_str(3))

def getName(first_name, family_name = ""):
	return family_name + " " + first_name

print("Shoko", "KOBAYASHI")
print("Shoko")
print("Shoko" "KOBAYASHI")

print "======"
x = 10 # global variables

# def func():
# 	print(x)
# func()

def func():
	global x
	x += 1
	print(x)
func()

print(x)
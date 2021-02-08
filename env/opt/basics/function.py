# coding: UTF-8
from typing import List

def f(x) -> int:
	return 2 * x

# 複数の戻り値を返せる
def swap (x, y):
	return y, x

def say_something(*args):
	print(args)

def odd(x):
	return x % 2 != 0

def odd_str(x):
	if odd(x):
		return "奇数"
	else:
		return "偶数"

x = 10 # global variables
def func():
	global x
	x += 1
	print(x)
func()

def append_array(a:int, arr:List = None) -> List[int]:
	if not arr:
		arr = []
	arr.append(a)
	return arr

# リストのデフォルト引数に空文字列を与えない
def getName(first_name, family_name = ""):
	return family_name + " " + first_name

def menu(**kwargs):
	print(kwargs)
	for k, v in  kwargs.items():
		print(k, v)

if __name__ == "__main__":
	print(f(3))
	print(swap(3, 4))
	print("=====")
	# 標準入力java
	# age_str = input("Enter your age:")
	# age = int(age_str)
	# if age < 20:
	# 	print("You are young"
	# else:
	# 	print("You are old"
	print("=====")



	print(odd_str(2))
	print(odd_str(3))

	print("Shoko", "KOBAYASHI")
	print("Shoko")
	print("Shoko" "KOBAYASHI")

	print("======")
	
	# def func():
	# 	print(x)
	# func()

	print(x)

	say_something("Mike", "John", "Yoko")

	append_array(100)

	menu(top="bible",second="dictionary")
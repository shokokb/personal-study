# coding: UTF-8

class UppercaseError(Exception):
	pass

if __name__ == "__main__":
	try :
		print(10 / 0)
	except ZeroDivisionError:
		print("NG")
	except UppercaseError as e:
		print(e)
	else :
		print("OK")
	finally : 
		print("clean up!")



# coding : UTF-8

def main():
  numbers = [1, 2, 3, 4]
  # [2, 4] -> [2^2, 4^2] -> [4, 16]
  squared = [n**2 for n in numbers if n % 2 == 0]
  print(squared)  # [4, 16]

if __name__ == "__main__":
  main()

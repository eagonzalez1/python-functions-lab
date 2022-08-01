

# 1: Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

n = int(input("Enter a number: "))

def sum_to(n):
  total_sum = 0
  total_Ns = n
  while total_Ns > 0:
    total_sum = total_sum + total_Ns
    total_Ns -= 1
  return total_sum
print(sum_to(n))



# 2: Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

num_list = [1, 2, 7, 9, 2, 5, 2, 6, 4, 1]

def largest(list):
  list.sort()
  return list[-1]

print(largest(num_list))




# 3: Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

first_string = "fleep floop"
second_string = "p"

def occurrences(string_one, string_two):
  return string_one.count(string_two)

print(occurrences(first_string, second_string))



# 4: Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.


def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product

print(product(5, 3, 7, 2, 4, 9))

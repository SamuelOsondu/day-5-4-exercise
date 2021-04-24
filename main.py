#Write your code below this row 👇

for numbers in range (1, 100):
  if numbers % 3 == 0:
    print ("fizz")
  if numbers % 5 == 0:
    print ("buzz")
  elif numbers % (3 and 5) == 0:
    print ("fizzbuzz")
  print (numbers)






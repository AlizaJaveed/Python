def my_function(fname, lname):
  print(fname + " \t" + lname)

my_function("Aliza" , "Javed")

def my_function(*kids):
  print("The youngest child is " + kids[1])

my_function("Aliza", "Kinza", "Maria")

def my_function(kid1, kid2, kid3):
  print("The youngest child is " + kid1)

my_function(kid1 = "Aliza", kid2 = "Kinza", kid3 = "Maria")
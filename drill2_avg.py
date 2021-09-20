def findAvg(name,dateOfBirth,grade,math,english,physics):
  print('Name - ',name)
  print('Date of birth - ',dateOfBirth)
  print('grade - ',grade)
  print('All grades - ', 'math - ',math, ',english - ',english, ',physics - ',physics)
  avg = (math + english + physics)/3
  print('avg - ',avg)

name = input('name: ')
dateOfBirth = input('Enter your date of birth:')
grade = input('Enter your grade:')
math =  int(input("Enter your Math score: "))
english =  int(input("Enter your Math score: "))
physics =  int(input("Enter your Math score: "))

findAvg(name,dateOfBirth,grade,math,english,physics)

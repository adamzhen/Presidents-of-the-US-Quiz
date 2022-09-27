from random import randint
def repeat(v, lst):
  b=False
  for i in range(len(lst)):
    if lst[i]==v:
      return True
  return b
def grovCleveland(val, p):
  if (val==22 and p==24) or (val==22 and p==24):
    return True
  else:
    return False 
def rand(n, start, stop, p=-1):
  lst = []
  for i in range(n):
    val = randint(start, stop)
    while repeat(val,lst) or val==p or grovCleveland(val, p):
      val = randint(start, stop)        
    lst.append(val)
  return lst
def getordn(p):
  orddict = {1 : "st", 2: "nd", 3:"rd"}
  if p>=1 and p<=3:
    return orddict.get(p)
  else:
    return "th"
def printInfo(p, name):
  presdates = open("presDates.txt","r")
  dates = presdates.readlines()[p-1]
  dates = dates.split()
  print(name+" served as president from", dates[0],"-",dates[1])
print("PRESIDENTS OF THE UNITED STATES \n")
score = 0
numq=int(input("How many rounds do you want? MAX 45: "))
print("Choose either 'a', 'b', 'c', or 'd':\n")
lst = rand(numq, 1, 45)
pres = ['George Washington', 'John Adams', 'Thomas Jefferson', 'James Madison', 'James Monroe', 'John Quincy Adams', 'Andrew Jackson', 'Martin Van Buren', 'William Henry Harrison', 'John Tyler', 'James K. Polk', 'Zachary Taylor', 'Millard Fillmore', 'Franklin Pierce', 'James Buchanan', 'Abraham Lincoln', 'Andrew Johnson', 'Ulysses S. Grant', 'Rutherford B. Hayes', 'James Garfield', 'Chester A. Arthur', 'Grover Cleveland', 'Benjamin Harrison', 'Grover Cleveland', 'William McKinley', 'Theodore Roosevelt', 'Howard Taft', 'Woodrow Wilson', 'Warren G. Harding', 'Calvin Coolidge', 'Herbert Hoover', 'Franklin D. Roosevelt', 'Harry S. Truman', 'Dwight D. Eisenhower', 'John F. Kennedy', 'Lyndon B. Johnson', 'Richard Nixon', 'Gerald Ford', 'Jimmy Carter', 'Ronald Reagan', 'George H.W. Bush', 'Bill Clinton', 'George W. Bush', 'Barack Obama', 'Donald Trump']
for i in range(numq):
  p = lst[i]
  ordn = getordn(p)
  print("Question "+str(i+1)+": Who was the "+str(p)+ordn+" president of the US?")
  correct = rand(1, 0, 3)
  choices = rand(4, 1, 45, p)
  lett = {0:"a)", 1:"b)", 2:"c)", 3:"d)"}
  for j in range(4):
    if j==correct[0]:
      print(lett.get(j), pres[p-1])
    else:
      print(lett.get(j), pres[choices[j]-1])
  ans = input("-> ").strip().lower()
  if ans+")"==lett.get(correct[0]):
    print("CORRECT!")
    score+=1
  else:
    print("INCORRECT")
    print("The correct president was: "+lett.get(correct[0]), pres[p-1])
  printInfo(p, pres[p-1])
  print()
print("Wow! You got", str(score)+"/"+str(numq),"questions right!")

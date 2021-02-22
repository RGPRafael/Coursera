''' 
learning python again
reminder that have to finish
hacker rank, 
the course is using python 3 i think...
'''

'''
example 0 : 
x = 2
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finis')

example 1 :
n = 5
while n > 0:
    print(n)
    n = n-1
print('Blastoff!')

example 3 :

name = input('Enter file: ')
handle =  open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word, count
....


constants:
string constants use single quotes  ' '

numeric expressions:
x = 4 ** 3
print(x) >> 64

read user:
input()

example 5:
inp = input('Europe floor?')
usf = int(inp) + 1
print('US floor,usf)

'''
##TRY E EXCEPT

'''
a = 'Hello bob'
try:
    i = int(a)
except :
    i = -1
print( 'First', i)
'''


### ASSIGMENT

'''
hrs = input("Enter Hours:")
h = float(hrs)
taxa = input("Ente Pay rate:")
t = float(taxa)

    
if h <= 40:
   p = h * t 

elif h > 40:
   extra = h - 40
   p = 40 * t + (extra * 1.5 * t)
    
print ( p )


'''

### ASSIGMENT

'''
def computepay(h,t):
   if h <= 40:
      p = h * t 

   elif h > 40:
      extra = h - 40
      p = 40 * t + (extra * 1.5 * t)
    
   return p

hrs = input("Enter Hours:")
h = float(hrs)
taxa = input("Ente Pay rate:")
t = float(taxa)
print("Pay",computepay(h,t))

'''

'''

largest = 0
smallest = None
while True:
    num = input("Enter a number: ")    
    if num == 'done' : ### em pyhton 3 isso eh permitido
        break
    try:
        n = int(num)
    except NameError:
        print('Invalid input')
    
    if   largest < n :
         largest = n
    
    if   smallest == None or smallest > n:
         smallest = n
            
print("Maximum is", largest )
print("Minimum is", smallest )
'''

#fim da parte 1 do curso
# começando a parte 2

### STRINGS

'''
fruit = 'banana'
index = 0
while index < len(fruit):
    l = fruit[index]
    print(index, l)
    index = index + 1


for l in fruit :
    print(l)

s = 'monty python'
print(s[0:4]) # vai de 0 ate 4 nao inclusivo
print(s[:2])
print(s[8:])

'''

#using in as a logical operator

'''

fruit = 'banana'
if( 'n' in fruit):
     print('find')
print('done')
if 'banana' == fruit :
    print('equal')

#dir(fruit)          all the methods 

'''


#searching a string

'''

fruit = 'banana'
pos = fruit.find('na') ## retorna -1 se nao encontrar
print(pos)
n = fruit.replace('n','J')
print(n)

greeet = '         Helllo bob     '
x = greeet.lstrip()
print(x)
x = greeet.rstrip()
print(x)
x = greeet.strip()
print(x)

###strings em python3 sao unicode ?

text = "X-DSPAM-Confidence:    0.8475"
t = text.find('0')
s = text[t:]
print(float(s))

'''

#using open()
# open files
'''
try:
       h = open(input('name_of_file.txt: '))
except:
       print('?')
       quit()
for caract in h :  #new line : \n
    print(caract)  #print adiciona \n !!
i = h.read()       #nao divide em linhas

'''


'''
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
cout = 0
values = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        cout   = cout + 1
        s      = line[line.find(':')+1:]
        f      = float(s.lstrip())
        values = values + f
m = values/cout
print('Average spam confidence:', m)


'''
##list

'''

f = ['J','G','S']
for i in f:
    print( i ,end = " ")
print(len(f))
#list is mutable
stuff =  list() #lista vazia
stuff.append('b')
stuff.append(99)
print(stuff)
# min , max ..
abc = 'adorei o seu cabelo'
string = abc.split() #use caract para separacao
print(string)

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    # print(line)
    list_words = line.split()
    # print(list_words)
    for i in list_words:
        if ( i not in lst) :
            lst.append(i)
lst.sort()
print(lst)



fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    #print(line)
    if line.startswith('From') and 'From:' not in line:
        count = count + 1
        words = line.split()
        print(words[1])

print("There were", count, "lines in the file with From as the first word")
'''

##Dictionaries
## bagas no order 

'''
p = dict()
p['m'] = 12
# m é a chave ou index e 12 é o valor
p['c'] = 3
print(p['c'])
#mutable
p['c'] = p['c'] + 2
print(p['c'])

#we can use in operator to 
#see if  a key is in the dictionary
if 'c' in p:
    print('IT IS')
if 'cc' not in p:
    print("SAD")

# x recebe o se a chave nao existir
x = p.get('chave', 0)  
print(x)

for key in p:
    print(key,p[key])

#give a list of keys
print(p.keys())

#give a list of values
print(p.values())

#give a list of tuple of keys and values
print(p.items())


for a,b in p.items():
    print(a,b)
'''


'''
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dicio  = dict()
for word in handle:
    if 'From ' in word:
        list_of_words = word.split()
        dicio[list_of_words[1]] = dicio.get(list_of_words[1], 0)  + 1

person = None
freq   = None 
for key,value in dicio.items():
    if ( freq is  None  or value > freq):
        freq   = value
        person = key
print(person , freq)


'''

### TUPLAS
## no mutable
'''

(x , y ) = ( 4, 'fred')
if ( 0,1,2) < ( 8, 9,10):
   print(True)

#sorting
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dicio  = dict()
print(sorted(dicio.items()))
for k,v in sorted(dicio.items()):
    print(k)


lst = list()
for k,v in dicio.items():
    newt = ( v, k)
    lst.append(newt)
lst = sorted(lst, reverse=True)
for v, k in lst[:10]:
    print(k,v)

'''

#LIST COMPREHENCION

'''
####10.2
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dicio  = dict()
for word in handle:
    if 'From ' in word:
        list_of_words = word.split()
        time = list_of_words[5].split(':')
        dicio[time[0]] = dicio.get(time[0], 0)  + 1
t = sorted(dicio.items())
for k,v in t:
    print(k,v)

'''


print('Installing and Running python')


























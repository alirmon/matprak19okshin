
# coding: utf-8

# Rock paper scissors 3 pepper

# In[10]:


t="yes";
while t=="yes":
    a= input("Player A, Rock Paper Scissors?") 
 
    b=input("Player B, Rock Paper Scissors?") 
    if a=='rock' or a=='Rock':
        am= 1 
    elif a=='paper' or a=='Paper': 
        am= 2
    elif a=='scissorc' or a=='Scissors':
        am=0 
    else: 
        am=-1 
    if b=='rock' or b=='Rock':
        bm = 1 
            
    elif b=='paper' or b=='Paper': 
        bm= 2
    elif b=='scissorc' or b=='Scissors':
        bm=0
    else: 
        bm=-1 
    if am<0 or bm<0: 
        print ("Wrong input, try again") 
        break
    if am==bm: 
        print("Draw!") 
    elif am==(bm+1)%3:
        print ("Player A win!")
    elif am==(bm-1)%3: 
        print ("Player B win!") 
    t= input ("Do you want to play again?")


# In[ ]:


Guess number 3 pepper


# In[2]:


import random
t= 'yes'
while t=='yes':
    number = random.randint(1,9)

    count = 0
    guess= 0
    while guess != number:
        guess= input("Write your number ")
        count+=1
        if  int(guess)<number :
            print("Too low! Try again")
        elif int(guess) > number:
            print("Too high! Try again")
        else:
            print("Correct!And it only took you",count,"tries!")
            break
    t= input("Want to try again? ")


# Check for prime 3 pepper

# In[16]:


a=int(input("Give me a number "))
print (a)
if a == 1:
    t = False
elif a == 2:
    t = True
else:
    for i in range(2, (a//2)+1):
        if  a%i ==0 :
            t=False
            break
if t:
    print("It is prime")
else:
    print("It is not prime")


# In[ ]:


Age 100 2 peppers


# In[17]:


n = input("What is your name: ")
a = int(input("How old are you: "))
y = (2019 - a)+100
if a<100:
    print(n + " will be 100 years old in the year ",y)
else:
    print(n + " was 100 years old in the year ",y)


# Print smaller then 5 1 pepper

# In[20]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
for i in a :
    if i<=5:
        b.append(i)
print(b)
        


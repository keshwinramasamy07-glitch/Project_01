print('hi i am keshwin')
print(input('who are you?'))
print('this is a page that tells some information about me!!!!')
def introduction():
    print('''name:keshwin
fname:ramasamy
mname:dhanalashmi
dob:7th feb 2009
          ''')
    return
def achievement_1():
    print('its non other then my 10th mark')
    print('but it is a complete disaster')
    print('sorry sorry')
    print('its the biggest setbsck for the biggest comeback ')
    print('''
            __/\\__/\\__
           [           ]
           [  []    [] ]
          [[   /____\\  ]]
           [  /\\____/\\ ]
           [___________]''')
    b=input('do u want to know my mark(yes/no):')
    if b=='yes':
        mark={'english':70,'tamil':74,'science':75,'social':81,'maths':81}
        for i,j in mark.items():
            print(i,':',j)
def achievement_2():
    print('it is the comeback era')
    print('my 12th exam mark!!!')
    print('every silence is warmup of for a new beginning')
    c=input('do u want to know my mark(yes/no):')
    if c=='yes':
        mark={'english':93,'physics':83,'maths':94,'chemistry':91,'computer':96}
        for i,j in mark.items():
            print(i,':',j)
def mistrybox():
    print('''i am belongs to a board student but i has a dream of write jee mains every one laugh at me......
          and the day comes i have completed my exam ...
          the result day came result have published everyonee nocked my door.. and i showed mystry box... 
          all laughs turned into tears''')
    d=input('do you want to see the box(yes/s):')
    if d=='yes' or d=='s':
        print('the magic:',92.7,'percentile')
        mark={'maths':98,'physics':82.7,'chemistry':85.58}
        for i,j in mark.items():
            print(i,':',j)
print('''
personal     : 1
10th mark    : 2
12th mark    : 3
unexpected   : 4
stop         : 5''')
while True:
    a=int(input('what do uwant to see(1,2,3,4,5):'))
    if a==1:
        introduction()
    elif a==2:
        achievement_1()
    elif a==3:
        achievement_2()
    elif a==4:
        mistrybox()
    elif a==5:
        break
    else:
        print("vilated only 1-5")
        
              
        
        
    
        


             
    
    
            



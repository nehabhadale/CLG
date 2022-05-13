print('Welcome to Expert system')

score=0
questions=['Your age : ','Gender  : ','BMI : ','How often do you eat vegetables, fruit or berries?']
yesnoqs=['Is there Family history of diabetes',
        'History of hypertension ? ','Have you ever been found to have high blood glucose?',
        'Do you usually do at least 30 minutes of daily physical activity at work and/or during leisure time?',
        ]
for i in range(4):
    print(questions[i])
    print()
    if i == 0 :
        age=int(input())
        if age <40:
            score+=0
        elif (age>=40 and age<=49) :
            score+=1
        elif(age>=50 and age<=59) :
            score+=2
        elif age>=60:
            score+=3
    if i == 1 :
        gender =input().lower()
        if(gender=='male'):
            score+=1
        else:
            score+=0
    if i==2 :
        height=float(input("\nHeight in cms "))
        weight= float(input("\nWeight in kg "))
        ht=height/100
        bmi = (weight)/(ht*ht)
        if (bmi>=40):
            score+=3
        elif (bmi>=30 and bmi<40) :
            score+=2
        elif(bmi>=25 and bmi<30) :
            score+=1
        else :
            score+=0

    if i == 3:
        ans = input("Everday or not everday : ").lower()
        if ans =='everyday':
            score +=0 
        else :
            score+=1




for i in range(4):     # for yes/no kind of questions
    print(yesnoqs[i])
    print()
    ans=input("Yes/No : ").lower()
    if i!=3:

        if(ans=='yes'):
            score+=1
        elif( ans=='no'):        
            score+=0
    else :
        if(ans=='yes'):
            score-=1
        elif( ans=='no'):        
            score+=0



if (score<3):
    print("Answer : You are least likely to suffer from diabetes.")
elif (score>=4):
    print("Answer : You are more likely to suffer from diabetes. Please visit a doctor  and also do blood checkup ")

'''
OUTPUT:
Welcome to Expert system

Your age :
25

Gender : 
female

BMI : 

Height in cms 150
Weight in kg 54

How often do you eat vegetables, fruit or berries?
Everday or not everday : everyday

Is there Family history of diabetes
Yes/No : no

History of hypertension ? 
Yes/No : no

Have you ever been found to have high blood glucose?
Yes/No : no

Do you usually do at least 30 minutes of daily physical activity at work and/or during leisure time?
Yes/No : yes

Answer : You are least likely to suffer from diabetes
'''
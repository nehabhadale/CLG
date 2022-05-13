print('Welcome to COVID-19 Expert system')
covidSuspisionCounter=0


severity=0
asym=0
oxylevel=0
temp=0
questions=["What is patient's body temparature",'What is the oxygen level','How many vaccines has the patient taken',"What is patient's age"]
yesnoqs=['Does the patient have cough and cold','Is the patient able to recognize smell and taste','Is the patient suffering from sore throat','Is the patient suffering from headache','Is the patient suffering from BP/ diabetes','Has the patient come in a contact of a Covid suspicious person']
for i in range(6):     # for yes/no kind of questions
    print(yesnoqs[i])
    print()
    ans=input()
    if(i!=1 and ans=='yes'):
        covidSuspisionCounter+=1
    elif(i==1 and ans=='no'):        # for smell and taste question
        covidSuspisionCounter+=1
for i in range(4):
    print(questions[i])
    print()
    if(i==0):
        ans=float(input())
        if(ans>=101.0):
            severity+=2             # more temperature --> more severity
            covidSuspisionCounter+=1
            temp=1
        elif(ans<101.0 and ans>=99.6):
            severity+=1
        else:
            severity+=0
    if(i==1):                          #oxygen level
        ans=int(input())
        if(ans>=94):
            severity+=0
        elif(ans<94 and ans>87):
            severity+=1
        else:
            severity+=2              # less oxygen level --> more severe
            covidSuspisionCounter+=1 # increments covid suspision counter
            oxylevel=1
    if(i==2):
        ans=int(input())
        if(ans==0):                     # vaccination
            severity+=2                  # no vaccines taken --> more severe
        elif(ans==1):
            severity+=1
        else:
            severity+=0
    if(i==3):                           #age
        ans=int(input())
        if(ans>12 and ans<31):
            severity+=0
        elif(ans>31 and ans<51):
            severity+=1
        else:                          # above 50 --> more severe
            severity+=2
if(covidSuspisionCounter>3):
    print('The patient is probably covid positive')
    print()
    if(severity<3):         # based on the value of the variable severity
        print('It looks like the symptoms are mild\nhome quarantine')
    elif(severity>=3 and severity<6):
        print('The patient can get an admission in the general ward')
    else:
        print('The patient looks critical')
else:        # if suspision counter is less than 3
    print('It looks like patient is not Covid positive')
print()
if(oxylevel==1):
    print("Keep monitoring patient's oxygen level")
if(temp==1):
    print("Keep monitoring patient's body temperature")
import random

def error_message():
    print ("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.\n")

  
def order_latte():
    milk = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n[d] Almond milk \n[e] Oatmilk \n[f] Hemp milk\n>").lower()
    if milk == 'a':
        return 'latte'
    elif milk == 'b':
        return 'non-fat latte'
    elif milk == 'c':
        return 'soy latte'
    elif milk == 'd':
        return 'almond latte'
    elif milk == 'e':
        return 'oat latte'
    elif milk == 'f':
        return 'hemp latte'
    else:
        error_message()
        return order_latte()

def extra_options():
    res = input('Would you like a plastic cup or did you bring your own reusable cup? \n[a] I\'ll need a cup. \n[b] Brought my own! \n> ')
    
    if res == 'a':
        print('Okay, no problem! We\'ll get you a plastic cup.')
    elif res == 'b':
        print('Great! We\'ll fill up your reusable cup.')
    else:
        error_message()
        return extra_options()


def get_drink_type():
    res = input("What type of drink would you like? \n[a] Coffee \n[b] Milk Tea \n[c] Latte \n>").lower()
    if res == 'a':
        return 'coffee'
    elif res == 'b':
        return 'milk tea'
    elif res == 'c':
        return order_latte()
    else:
        error_message()
        return get_drink_type()
  
def get_size():
    res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \yn[c] Large \n> ').lower()
    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:
        error_message()
        return get_size()
def NumberDrink():
    res=int(input("How many drinks do you need ?\n"))
    return res 

def coffee_ordering():
    print("Welcome to the cafe!")
    
    drink_type = get_drink_type()
    size = get_size()
    noDrink= NumberDrink()
    print("Alright, that's {} {} {}.".format(noDrink,size, drink_type))
   
    extra_options()
    
    usname = input("Can I get your name please?\n")
    print("Thanks, {}! Your drink will be ready shortly".format(usname))

name="BOT04"
bot_template = "BOT : {0}"
time = "10 AM to 9 PM"
bye = "Have a nice day!"
resp = { 
    "name": ["They call me {0}".format(name), "I usually go by {0}".format(name),
	"My name is the {0}".format(name),],

    "cancel":  ["Your order is cancelled "],
    
    "order":  ["What would you like to order ?"],

    "what are the timings of the shop?": [
	"The shop is opened from {0}! see you there! :)".format(time), ],

    "how are you?": [
	"I am fine! Hope you too!:)",
	"I am doing good!" ],
    "Good-bye": [
	"Have a nice day!",
	"See you again!"
	],

    "":
    ["Hey! Are you there?"],
    
    }

def related(xtext): 
    if "name" in xtext: 
        ytext = "name"
    elif "cancel" in xtext: 
        ytext = "cancel"

    elif "order" in xtext:
        ytext="order"

    elif "time" in xtext:
        ytext = "what are the timings of the shop?"
    elif "how are" in xtext:
        ytext = "how are you?"
    elif "bye" in xtext:
         ytext = "Good-bye"
    else: 
        ytext = ""
    return ytext

def response(message):
    if message in resp: 
    
        bot_message = random.choice(resp[message])
       
        
    else: 
        bot_message = "I'm sorry, I did not understand your query.\n"
    return bot_message

def send_message(message): 
    
    resp1 = response(message)
    if "to order" in resp1:
        print(bot_template.format(resp1))
        coffee_ordering()
        
    else:
       print(bot_template.format(resp1))



def User_issue():
    print("Welcome")
    print("How can I help you?")
    
    while 1: 
        my_input = input("\nUser : ") 
        my_input = my_input.lower()
        if my_input == "exit" or my_input == "stop": 
            print("exit...")
            break
        related_text = related(my_input) 
        send_message(related_text)
       

User_issue()
'''
OUTPUT :


Welcome

How can I help you?

User : how are you
BOT : I am doing good!

User : whats your name 
BOT : My name is the BOT04

User : shop time
BOT : The shop is opened from 10 AM to 9 PM! see you there! :)

User : i want to order
BOT : What would you like to order ?

Welcome to the cafe!
What type of drink would you like? 
[a] Coffee
[b] Milk Tea
[c] Latte
>a
What size drink can I get for you? 
[a] Small
[b] Medium \yn[c] Large
> b
How many drinks do you need ?
2
Alright, that's 2 medium coffee.
Would you like a plastic cup or did you bring your own reusable cup?
[a] I'll need a cup.
[b] Brought my own!
> a
Okay, no problem! We'll get you a plastic cup.

Can I get your name please?
ZWE
Thanks, ZWE! Your drink will be ready shortly

User : cancel my order
BOT : Your order is cancelled 

User : bye
BOT : See you again

'''
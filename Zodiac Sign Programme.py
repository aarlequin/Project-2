#!/usr/bin/env python
# coding: utf-8

# In[1]:




#Begin by introducing the user to the program. Ask the user to input "START" to begin the program. 

start = str(input(
    "\033[1mWelcome to Zodiac Star 🌠. Enter START to begin and discover your star today:\033[0m  ")).lower()
#Create a while loop to prevent the program from crashing if a user enters the wrong information. 
while (start != "start"):
    start = input("\033[1mPlease type start\033[0m")

userlist=[]
for i in range (5):
# Ask users to enter their user ID number.
            print('\033[1mPlease enter your 2 digit user id\033[0m')
    
            user_id = (input("\033[1mEnter your user ID login:\033[0m    "))
#A conditional while loop is placed here to ensure that the user only enters a two digit ID number, otherwise the program will loop. 
#Asking them to re-enter their user ID number. 
            while len(user_id) != 2 or (user_id.isnumeric() == False):
                user_id = input("\033[1mPlease try again. This time make sure it's a 2 digit number\033[0m")
    
#Print the user's 2 digit ID number and ask them to save it for the next time they login in. 
            print(f"\033[1mSave your ID login: {user_id}\033[0m") 

#Ask the user to enter their name and store it as a variable. 
            name = str(input("\033[1mEnter your full name:\033[0m    ")).lower()

#Use the datetime library to support the importation and usage of the user's date of birth. This will help us to calulate their birthday, and then their zodiac sign.
            import datetime
#Ask the user to enter their date of birth in a specif format of DD/MM/YYY.
            bdate = input("\033[1mEnter your date-of-birth(ie.DD/MM/YYYYs):\033[0m ")

#Based on the date of birth that the user inputs, calculate their date of birth and their age using the datetime library.
            day, month, year = map(int, bdate.split('/'))
            birth_date = datetime.date(year, month, day)

            current_year = datetime.datetime.now().year

            age = current_year - birth_date.year

#Print the user's age.
            print(f"\033[1mYour age is:{age}\033[0m\n\n")


#Create conditional branching if and elif statements based on the user's date of birth to determine their zodiac sign. 
#All of the zodiac signs should be written out, including the OR and AND condiational characters. 
#Take the user's month and day of birth. If it falls within the dates of a specif zodiac sign print their sign immediatly.
#If Else, the program will continue to run through the codes until their zodiac sign is matched to them. 

def zsign(month,day):
    
            if ((int(month) == 12 and int(day) >= 22) or (int(month) == 1 and int(day) <= 19)):
                zodiac_sign = ("\n Capricorn ♑")
            elif ((int(month) == 1 and int(day) >= 20) or (int(month) == 2 and int(day) <= 17)):
                zodiac_sign = ("\n Aquarius ♒ ")
            elif ((int(month) == 2 and int(day) >= 18) or (int(month) == 3 and int(day) <= 19)):
                zodiac_sign = ("\n Pices ♓")
            elif ((int(month) == 3 and int(day) >= 20) or (int(month) == 4 and int(day) <= 19)):
                zodiac_sign = ("\n Aries ♈")
            elif ((int(month) == 4 and int(day) >= 20) or (int(month) == 5 and int(day) <= 20)):
                zodiac_sign = ("\n Taurus ♉")
            elif ((int(month) == 5 and int(day) >= 21) or (int(month) == 6 and int(day) <= 20)):
                zodiac_sign = ("\n Gemini ♊")
            elif ((int(month) == 6 and int(day) >= 21) or (int(month) == 7 and int(day) <= 22)):
                zodiac_sign = (" Cancer ♋")
            elif ((int(month) == 7 and int(day) >= 23) or (int(month) == 8 and int(day) <= 22)):
                zodiac_sign = ("\n Leo ♌")
            elif ((int(month) == 8 and int(day) >= 23) or (int(month) == 9 and int(day) <= 22)):
                zodiac_sign = ("\n Virgo ♍")
            elif ((int(month) == 9 and int(day) >= 23) or (int(month) == 10 and int(day) <= 22)):
                zodiac_sign = ("\n Libra ♎")
            elif ((int(month) == 10 and int(day) >= 23) or (int(month) == 11 and int(day) <= 21)):
                zodiac_sign = ("\n Scorpio ♏")
            elif ((int(month) == 11 and int(day) >= 22) or (int(month) == 12 and int(day) <= 21)):
                zodiac_sign = ("\n Sagittarius ♐")
                
            return zodiac_sign
        


#Create conditional branching if and elif statements based on the user's date of birth to determine their Chinese sign.    
            chineseYear = year % 12 
            if chineseYear == 0:
                chinese_sign=("Monkey") 
            elif chineseYear == 1:
                chinese_sign=("Rooster")
            elif chineseYear == 2:
                chinese_sign=("Dog")
            elif chineseYear == 3:
                chinese_sign=("Pig")
            elif chineseYear == 4: 
                chinese_sign=("Rat")
            elif chineseYear == 5: 
                chinese_sign=("Ox")
            elif chineseYear == 6:
                chinese_sign=("Tiger")
            elif chineseYear == 7:
                chinese_sign=("Rabbit")
            elif chineseYear == 8:
                chinese_sign=("Dragon")
            elif chineseYear == 9:
                chinese_sign=("Snake")
            elif chineseYear == 10:
                chinese_sign=("Horse")
            else: 
                chinese_sign=("Sheep") 
# A print function that prints the user's chinese sign. 
            print(f"Your Chinese sign is:{chinese_sign}")
#Create a list that contains the content of the table that will present the user's data.        
            userlist.append([user_id,name,bdate,age,zodiac_sign,chinese_sign])
#Install the tabualte table to present the user's data. 
get_ipython().system('pip install tabulate')
from tabulate import tabulate
#Print the table with the data of 5 users.
print(tabulate(userlist, headers=[     "UID","Name", "D.o.B", "Age","Western Zodiac", "Chinese Zodiac"]))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





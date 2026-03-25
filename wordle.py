import datetime
import requests
date=datetime.date.today()
url=f"https://www.nytimes.com/svc/wordle/v2/{date}.json"
response=requests.get(url)
if response.status_code==200:
    data=response.json()
    word=data["solution"]
else:
    print("Error")


counter=5
while(counter>0):
    user_input=input("Enter the word:")
    if len(user_input)!=5:
        print("wrong input")
    elif user_input==word:
        print(f"You have won {counter} points")
        break
    else:
        for i in range(0,len(user_input)):
            if user_input[i]==word[i]:
                print(f"{user_input[i]} is in correct position")
            elif user_input[i] in word:
                print(f"{user_input[i]} is in word but not in correct position")
            else:
                print("miss!")
        counter+=1
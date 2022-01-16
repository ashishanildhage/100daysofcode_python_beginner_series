ticker="ash"
stocklist={
    ticker:"CHOLAFIN",
    "price":250,
    "yestclose":240
}
stocklist["marketcap"]=3000000
print(stocklist)
stocklist={}
print(stocklist)
stocklist["yestclose"]=250
print(stocklist)
for columns in stocklist:
    print(columns,stocklist[columns])

#------------------
#Grading Program
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades={}
for scores in student_scores:
    if 91<=student_scores[scores]<=100:
        student_grades[scores]="Outstanding"
    elif 81<=student_scores[scores]<=90:
        student_grades[scores]="Exceeds Expectation"
    elif 71<=student_scores[scores]<=80:
        student_grades[scores]="Acceptable"
    elif student_scores[scores]<=70:
        student_grades[scores]="Fail"
print(student_grades)

#------------------
#Nesting dictionary in Dictionary
sectorlist={
    "IT":{"cmp":[2500,3000,2000,1500],"all_time_high":["TCS","INFY","BSOFT","NAUKRI"],"shares_holding":[5000,2000,2500,8000]},
    "Metals":{"cmp":[300,800],"all_time_high":["SAIL","TATASTEEL"],"shares_holding":[9000,12000]},
}#dictionary>Dictionary>Lists
#press { to dictionate and [ to list the "selected text"
print(sectorlist)

#------------------
# Nesting dictionary in List
# instead of making "IT" the index of the dictionary make it a key and enclose within a list
# to make index 0 instead of "IT"
sectorlist=[
    {
        "sector":"IT",
        "cmp":[2500,3000,2000,1500],
        "all_time_high":["TCS","INFY","BSOFT","NAUKRI"],
        "shares_holding":[5000,2000,2500,8000]
    },
    {
        "sector":"Metals",
        "cmp":[300,800],
        "all_time_high":["SAIL","TATASTEEL"],
        "shares_holding":[9000,12000]
    }
]
print(sectorlist)

#------------------
#Adding data to lists & dictionary
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(add_country,add_visits,add_cities):
    # travel_log.append({
    #     "country" : add_country,
    #     "visits": add_visits,
    #     "cities" : add_cities
    #     })
    new_country = {}
    new_country["country"] = add_country
    new_country["visits"] = add_visits
    new_country["cities"] = add_cities
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


#------------------
#Secret Auction
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
import os
print("Welcome to the Secret Auction Program")
nobidders=True
database={}
while nobidders:
    # database=[{
    #     "name":input("What is your name?: "),
    #     "bids":input("What's your bids?: ")
    #     }]
    name=input("What is your name?: ")
    bid=int(input("What's your bids?: "))
    database[name]=bid
    extras=input("Are their any other bidders? Type y/n.\n")
    if extras=="y":
        os.system("cls" if os.name in ('nt', 'dos') else 'clear')
    elif extras=="n":
        os.system("cls" if os.name in ('nt', 'dos') else 'clear')
        nobidders=False
        max=0
        for bids in database:
            if database[bids]>max:
                max=database[bids]
                winner=bids
        print(f"The winner is {winner} with the highest bid of {max}\nCongratulations...!!!")










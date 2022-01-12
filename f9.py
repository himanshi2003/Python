print("enter your birth date")
birth_year=int(input())
current_year=2021
age=current_year-birth_year
if(age<13):
    print("you are under age,you can not watch this movie")
else:
        print("you are old enough to watch this movie,enjoy")
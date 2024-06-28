age_days=int(input("Enter the number of days: "))
years=age_days//(30*12)
months=(age_days/(30*12)-years)*12
months=int(months)
days=30*((age_days/(30*12)-years)*12-months)
print(years,months,int(days))
"""""
another soln
years=days//360
days=days%360

months=days//30
days=days%30
"""""


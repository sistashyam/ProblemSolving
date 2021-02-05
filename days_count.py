def leap_year(n):
    leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
    non_leap_year = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    odd_days = 0
    years_left = year - 1
    years_left = years_left % 400
    odd_days = (years_left // 100) * 5
    years_left = years_left % 100
    odd_days = odd_days + ((years_left // 4) * 2) + (((years_left) - (years_left // 4)) * 1)
    odd_days = odd_days % 7
    
    if ((year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)):
        year_list = leap_year
    else:
        year_list = non_leap_year
    
    sunday = 0
    
    for i in range(0,len(year_list)):
        if i == 0:
            odd_days = odd_days + 1
        else:
            odd_days = odd_days - 1
            odd_days += year_list[i-1] + 1
        if odd_days % 7 == 0:
            sunday = sunday + 1
    return sunday

print(leap_year(1996))
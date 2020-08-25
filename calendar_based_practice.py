import calendar

print('Team meetings will be on:')
for m in range(1,13):
    cal = calendar.monthcalendar(2021,m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.WEDNESDAY]!=0:
        meetday = weekone[calendar.WEDNESDAY]
    else:
        meetday = weektwo[calendar.WEDNESDAY]
    print('%10s %2d'%(calendar.month_name[m], meetday))
def solution(a,b):
     day=['FRI','SAT','SUN','MON','TUE','WED','THU']
     mond=[31,29,31,30,31,30,31,31,30,31,30]
     return day[(sum(mond[:a-1])+b-1)%7]
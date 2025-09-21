class Solution:
    def dayOfYear(self, date: str) -> int:
        year  = int(date.split('-')[0])
        month = int(date.split('-')[1])
        day   = int(date.split('-')[2])
        month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
        ret = sum(month_days[0:month-1])
        ret += day
        # 閏年
        if month >= 3 and year % 4 == 0 and year % 100 != 0:
            ret += 1
        return ret
# 闰年判断
def is_leap_year(year):
    if(year%4==0and year%100!=0)or(year%400==0):
         return True
    else:
         return False

#成绩判断
def get_grade(score):
    if score >= 90:
        return "优秀"
    elif score >= 75:
        return "良好"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"

#测试
print(f"2024是闰年吗？{is_leap_year(2024)}")
print(f"2025是闰年吗？{is_leap_year(2025)}")
print(f"85分属于：{get_grade(85)}")
  

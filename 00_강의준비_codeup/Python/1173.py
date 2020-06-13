# 1번 풀이
# hour, minute = input().strip().split(" ")
# hour, minute = int(hour), int(minute)

# total_minutes = hour * 60 + minute
# total_minutes = total_minutes - 30

# if total_minutes < 0:
#     hour = 23
#     minute = 60 + total_minutes
# else:
#     hour = total_minutes // 60
#     minute = total_minutes % 60

# print(hour, minute)

# 2번 풀이
hour, minute = input().strip().split(" ")
hour, minute = int(hour), int(minute)

if minute >= 30:
    minute = minute - 30
else:
    minute = minute + 30
    hour = hour - 1
    if hour < 0:
        hour = 23

print(hour, minute)
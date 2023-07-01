the_input = int(input("Please Enter The Time In Seconds:"))
hour = int()
min = int()
sec = int()


def divid_to_60(a):
    min = a // 60
    sec = a % 60
    hour = min // 60
    min = min % 60
    print(f'the time is {hour}:{min}:{sec}')


divid_to_60(the_input)


# 3620

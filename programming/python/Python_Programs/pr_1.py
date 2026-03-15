def make_readable(seconds):
    m = 0
    minute = 0
    second = 0
    s = 0
    h = 0
    d = 0
    if(seconds >= 59):
        second = 59
    elif(seconds < 59):
        return h,minute,seconds
    for i in range(1,60):
        d = 60 * i
        if d > seconds:
            break
    m = int((60 * i) / 60)
    return m
    if(m == 59):
        return h,m,second
    elif(m > 59):
        minute = 59
        for i in range(1,60):
            s = 60 * i
            if s > m:
                break
        return m
        h = int((60 * i) / 60)
    elif(m < 59):
        return h,m,second
    if(h > 99):
        return "Error , hours can't be more than 99"
    return h,minute,second
print(make_readable(86399))
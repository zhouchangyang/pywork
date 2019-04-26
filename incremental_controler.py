import time
i=1
increment = 0.2
span = 10
while True:
    if i % 3 ==0:
        span=span+increment
    print(i,span)
    time.sleep(span)
    i+=1

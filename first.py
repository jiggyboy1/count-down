import time 

t = int(input('Enter a minute in second: '))

for i in range(1,t):
    minutes , seconds = divmod(t,60)
    timers = f'{minutes:02d}:{seconds:02d}'
    print(timers, end="\r")
    time.sleep(1.5)
    t = t - 1
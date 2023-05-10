

import os 
import threading

def cpu_waster():
    while True:
        pass


print("\n Process ID:", os.getpid())

print("Thread count", threading.active_count())


for thread in threading.enumerate():
    print(thread)

for i in range(12):
    threading.Thread(target=cpu_waster).start()


print("\n Process ID:", os.getpid())
print("Thread count", threading.active_count())
for thread in threading.enumerate():
    print(thread)

'''

output

 Process ID: 5044
Thread count 1
<_MainThread(MainThread, started 8585075520)>

 Process ID: 5044
Thread count 13
<_MainThread(MainThread, started 8585075520)>
<Thread(Thread-6 (cpu_waster), started 6249426944)>
<Thread(Thread-7 (cpu_waster), started 6266253312)>
<Thread(Thread-8 (cpu_waster), started 6283079680)>
<Thread(Thread-9 (cpu_waster), started 6299906048)>
<Thread(Thread-10 (cpu_waster), started 6333558784)>
<Thread(Thread-11 (cpu_waster), started 6316732416)>
<Thread(Thread-12 (cpu_waster), started 6350385152)>
<Thread(Thread-13 (cpu_waster), started 6367211520)>
<Thread(Thread-14 (cpu_waster), started 6384037888)>
<Thread(Thread-15 (cpu_waster), started 6400864256)>
<Thread(Thread-16 (cpu_waster), started 6417690624)>
<Thread(Thread-17 (cpu_waster), started 6434516992)>

'''
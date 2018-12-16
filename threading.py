#Threading

import threading
class Thread(threading.Thread):
    def run(self):
        i=1
        while i<=5:
            print(i)
            i=i+1

class Thread2(threading.Thread):
    def run(self):
        i=1
        while i<=5:
            print(i)
            i=i+1

t1=Thread()
t2=Thread2()
t1.start()
t2.start()
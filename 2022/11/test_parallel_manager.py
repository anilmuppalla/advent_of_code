from multiprocessing import Process, Manager
import pprint
import os

def f(d):
    d[1] += '1'
    d['2'] += 2
    pid = os.getpid()
    print("done: ", pid)

if __name__ == '__main__':
    manager = Manager()
    ps = []

    d = manager.dict()
    d[1] = '1'
    d['2'] = 2
    
    for i in range(0, 4):
        p = Process(target=f, args=(d,))
        p.start()
        ps.append(p)

    for p in ps:
        p.join()
    
    pprint.pprint(dict(d))
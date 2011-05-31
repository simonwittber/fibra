import timeit
import fibra
import random
import sys

scheduler = fibra.schedule()

class hackysacker:
    counter = 0
    def __init__(self,name,circle):
        self.name = name
        self.circle = circle
        circle.append(self)
        self.messageQueue = fibra.Tube()
        scheduler.install(self.messageLoop())

    def messageLoop(self):
        while 1:
            message = yield self.messageQueue.pop()
            if message == "exit":
                return
            kickTo = self.circle[random.randint(0,len(self.circle)-1)]
            hackysacker.counter += 1
            if hackysacker.counter >= turns:
                while self.circle:
                    hs = self.circle.pop()
                    if hs is not self:
                        yield hs.messageQueue.push('exit', wait=True)
            yield kickTo.messageQueue.push(self, wait=True)
                


def debugPrint(x):
    if debug:
        print x

debug=1
hackysackers=5
turns = 5

def runit(hs=10000,ts=1000,dbg=1):
    global hackysackers,turns,debug
    hackysackers = hs
    turns = ts
    debug = dbg
    
    hackysacker.counter= 0
    circle = []
    one = hackysacker('1',circle)

    for i in range(hackysackers):
        hackysacker(`i`,circle)

    def main():
        yield one.messageQueue.push(one)

    scheduler.install(main())
    scheduler.run()


if __name__ == "__main__":
    print timeit.Timer(setup="from __main__ import runit", stmt='runit(dbg=0)').timeit(20) / 20.0


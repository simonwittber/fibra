
import Axon
import time
import random
import sys

class hackymsg:
    def __init__(self,name):
        self.name = name

class counter:
   def __init__(self):
      self.count = 0
   def inc(self):
      self.count +=1

class hackysacker(Axon.Component.component):
    def __init__(self,name,circle,cntr,loops):
        Axon.Component.component.__init__(self)
        self.cntr = cntr
        self.name = name
        self.loops = loops # terminating condition
        self.circle = circle # a list of all the hackysackers
        circle.append(self)

    def main(self):
        yield 1
        while 1:
            while not self.anyReady():
                self.pause()
                yield 1
            while self.dataReady('inbox'):
                msg = self.recv('inbox')
                if msg == 'exit':
                    return
                if self.cntr.count > self.loops:
                    for z in self.circle:
                        z.inboxes['inbox'].append('exit')
                    return
                #print "%s got hackysack from %s" % (self.name, msg.name)
                kickto = self.circle[random.randint(0,len(self.circle)-1)]
                while kickto is self:
                    kickto = self.circle[random.randint(0,len(self.circle)-1)]
                #print "%s kicking hackysack to %s" %(self.name, kickto.name)
                msg = hackymsg(self.name)
                kickto.inboxes['inbox'].append(msg)
                self.cntr.inc()
                #print self.cntr.count
            yield 1

def runit(num_hackysackers=5,loops=100,dbg=0):
    cntr = counter()
    circle=[]
    first_hackysacker = hackysacker('1',circle,cntr,loops)
    first_hackysacker.activate()
    for i in range(num_hackysackers):
        foo = hackysacker(`i`,circle,cntr,loops)
        foo.activate()

    # throw in the first sack...
    msg = hackymsg('me')
    first_hackysacker.inboxes['inbox'].append(msg)

    Axon.Component.scheduler.run.runThreads()

if __name__ == "__main__":
    runit(num_hackysackers=1000,loops=1000)

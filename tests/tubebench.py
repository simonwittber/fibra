import timeit
import fibra
import sys


def cat():
    meow = fibra.Tube("meow")
    woof = fibra.Tube("woof")
    for i in xrange(1000):
        m = yield woof.pop()
        yield meow.push("meow")
    
def dog():
    meow = fibra.Tube("meow")
    woof = fibra.Tube("woof")

    while True:
        yield woof.push("woof")
        m = yield meow.pop(wait=True)
    


def test():
    schedule = fibra.schedule()
    schedule.install(cat())
    schedule.install(dog())
    schedule.run()

if __name__ == "__main__":
    print timeit.Timer(setup="from __main__ import test", stmt='test()').timeit(100)


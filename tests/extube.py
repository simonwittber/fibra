import fibra

def echo():
    input = fibra.Tube("log_service")
    yield 2
    while True:
        try:
            msg = yield input.pop(wait=True)
        except fibra.EmptyTube:
            print 'no message'
            yield 1
        else:
            print msg


def send():
    output = fibra.Tube("log_service")
    yield output.push("hello!", wait=False)
    print 'pushed'
        

schedule = fibra.schedule()
schedule.install(echo())
schedule.install(send())
schedule.install(send())
schedule.install(send())
schedule.install(send())
schedule.install(send())
schedule.run()

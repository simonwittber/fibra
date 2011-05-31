import fibra

def sub_task(x):
    if x < 5: 
        yield fibra.Return(x**x)
    else:
        raise ValueError("x must be < 5")

def main_task():
    #launch a sub task
    #wait for it to finish and collect the result.
    x = yield sub_task(4)
    print x
    #the sub task will raise an exception here...
    #yet the exception will bubble up to the parent task!
    try:
        x = yield sub_task(5)
    except ValueError:
        print "Oops, an exception occured."

schedule = fibra.schedule()
schedule.debug = True
schedule.install(main_task())
schedule.run()

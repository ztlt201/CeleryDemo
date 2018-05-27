from celery import Celery
from DebugTest import DebugTask
import os

app = Celery('engine', backend="redis://localhost", broker="redis://localhost")

@app.task(base=DebugTask)
def sayhello(name):
    print("%s say hello to you" % name)
    return "My litao"


@app.task(base=DebugTask)
def add(x, y):
    return x + y


@app.task(base=DebugTask)
def xsum(l):
    sum = 0
    for i in l:
        sum = sum + i
    return sum


@app.task(base=DebugTask)
def log_error(task_id):
    result = app.AsyncResult(task_id)
    #result.get(propagate=False)
    with open(os.path.join('/var/errors',task_id), 'a') as fh:
        #print('--\n\n{0} {1} {2}'.format(task_id, result.result, result.traceback), file=fh)
        print >> fh, '--\n\n{0} {1} {2}'.format(task_id, result.result, result.traceback)


@app.task(base=DebugTask)
def raise_error():
    raise Exception


if __name__ == '__main__':
    app.worker_main()
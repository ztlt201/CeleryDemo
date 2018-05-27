from engine import sayhello
from engine import xsum
from engine import *
from engine import add
from celery import group
from celery import chord
from celery import chain

#callback apply result of parent as first argument,so this cmd raise exception
sayhello.apply_async(("litao",), link=sayhello.s('test'))
#this is call a func not send to celery,not a task
sayhello.s("litao")()

s = sayhello.s()
async = s.apply_async(('litao',))
#
'''
names = [('litao',), ('tangjie',), ('haha',)]
res = group(sayhello.subtask(name) for name in names).apply_async()
res.get()

sayhello.apply_async(('litao',), link = sayhello.si("tebie"))

res = chain(sayhello.s("litao"), sayhello.s(), sayhello.s())()
print res.get()


res = group(add.s(i, i) for i in range(0,10))()
print res.get()

res = chord((add.s(i, i) for i in range(0,10)), xsum.s()).apply_async()
print res.get()

res = (add.s(4, 4) | group(add.si(i, i) for i in xrange(10)))()
print res.get()


s = raise_error.s()
s.apply_async(link_error=log_error.s())
'''
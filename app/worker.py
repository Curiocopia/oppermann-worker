#!/usr/bin/env python

import time
import rediswq
import sagemathapiclient
import os

host=os.getenv("REDIS_SERVICE")
queue = os.getenv("REDIS_QUEUE")

q = rediswq.RedisWQ(name=queue, host=host)
client = sagemathapiclient.SageMathAPIClient()
print("Worker with sessionID: " +  q.sessionID())
print("Initial queue state: empty=" + str(q.empty()))
while not q.empty():
  item = q.lease(lease_secs=10, block=True, timeout=2)
  if item is not None:
    itemstr = item.decode("utf-8")
    oppermann_pair = client.get_oppermann_counts(itemstr)
    if oppermann_pair[0] == oppermann_pair[1]:
      print(itemstr, " is MAGICAL with a pair of ", oppermann_pair[0], " prime numbers on either side of its square.")
    q.complete(item)
  else:
    print("Waiting for work")
print("Queue empty, exiting")

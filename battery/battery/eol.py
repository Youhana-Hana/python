import json
from itertools import groupby;

def key(item):
    return item['id'];

def calculate(buckets):
    if len(buckets) == 0:
        return None;
    data = json.loads(buckets);
    output = {}
    results = {}
    for k, g in groupby(data, key):
        results.setdefault(k, [])
        results[k].append(int(list(g)[0]['cycle']))

    for i in results.keys():
        average = sum(results[i]) / len(results[i])
        output[i] = average


    return output

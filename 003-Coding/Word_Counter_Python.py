#!/usr/bin/env python
f = open('Shakespeare.txt', 'r')
flat_list = [word for line in f for word in line.split()]
for x in flat_list:
    x = x.isalnum()


def word_count():
    counts = dict()
    for word in flat_list:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


print(word_count())

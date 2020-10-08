#!/usr/bin/python3
from collections import namedtuple, OrderedDict
import operator

class A(namedtuple('B', 'c')):
    def _asdict(self):
        return OrderedDict(zip(self._fields, self))

Person = namedtuple('Person', ['first', 'last', 'distance'])


PEOPLE = [Person('Donald', 'Trump', 7.85),
          Person('Vladimir', 'Putin', 3.626),
          Person('Jinping', 'Xi', 10.603)]


def format_sort_records(list_of_tuples):
    output = []
    
    template = '{last:10} {first:10} {distance:5.2f}'
    for person in sorted(list_of_tuples, key=operator.attrgetter('last', 'first')):
       output.append(template.format(**person._asdict()))
    return output

print(format_sort_records(PEOPLE))
import itertools
import operator
import pylab
import sys


# Datums in format: (what, min, max).
RAW_DATA = (
    ('coffee', 2, 3),
    ('tea', 7, 7),
    ('coffee', 1, 1),
    ('coffee', 3, 4),
    ('coffee', 5, 8),
    ('coffee', 3, 5),
    ('Battery', 1, 1),
    ('coffee', 2, 4),
    ('tea', 12, 14),
    ('sparkling water', 5, 6),
    ('coffee', 6, 6),
    ('coffee', 3, 4),
    ('coffee', 3, 3),
    ('coffee', 0, 1),
    ('coffee', 2, 2),
)


def avg(lst):
    return sum(lst) / float(len(lst))


def gen_drinks():
    groups = itertools.groupby(sorted(RAW_DATA), operator.itemgetter(0))
    group_names = []
    group_lens = []
    for name, group in groups:
        group_names.append(name)
        group_lens.append(len(list(group)))
    fig = pylab.figure(1, figsize=(6, 6))
    pylab.pie(group_lens, labels=group_names, autopct='%1.1f%%')
    pylab.title(u'Different drinks consumed daily (n={0})'.format(len(RAW_DATA)))
    fig.savefig('drinks.png')
    pylab.clf()


def gen_amounts():
    coffee_data = [d for d in RAW_DATA if d[0] == 'coffee']
    fig = pylab.figure(1, figsize=(6, 6))
    amounts = [avg([d[1], d[2]]) for d in coffee_data]
    pylab.pie(amounts, labels=[str(n) for n in amounts], autopct='%1.1f%%')
    avg_amount = '{0:.2}'.format(avg(amounts))
    pylab.title((u'Amount of cups drank in a day by coffee drinkers\n(n={0}, '
                 u'avg={1})').format(len(RAW_DATA), avg_amount))
    fig.savefig('amounts.png')
    pylab.clf()


def main():
    gen_drinks()
    gen_amounts()


if __name__ == '__main__':
    sys.exit(main() or 0)

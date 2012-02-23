import sys
import pylab


MARKET_SHARE = (
    ('Android', 50.9),
    ('iOS', 23.8),
    ('Symbian', 11.7),
    ('RIM', 8.8),
    ('Bada', 2.1),
    ('Microsoft', 1.9),
    ('Others', 0.8),
)


def main():
    fig = pylab.figure(1, figsize=(6, 6))
    pylab.pie([s[1] for s in MARKET_SHARE],
              labels=[s[0] for s in MARKET_SHARE],
              autopct='%1.1f%%')
    fig.savefig('images/market-share.png')
    pylab.clf()


if __name__ == '__main__':
    sys.exit(main() or 0)

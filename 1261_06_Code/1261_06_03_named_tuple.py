from collections import namedtuple
Stock = namedtuple("Stock", "symbol current high low")
stock = Stock("GOOG", 613.30, high=625.86, low=610.50)

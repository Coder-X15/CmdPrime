import sys
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

c_handler = logging.StreamHandler()
logger.addHandler(c_handler)

if len(sys.argv) < 2:
    print("Not enough parameters, range is missing")
    exit(1)

if len(sys.argv) > 2:
    print("Too many parameters.")
    exit(2)

input_range = sys.argv[1]
if not input_range.isnumeric():
    print("Range must be a number")
    exit(3)

input_range_integer = int(input_range)

series_a = [2, 5]
series_b = [3, 7]

for i in range(input_range_integer):
    series_a.append(series_a[1] + (i + 1) * 6)
    series_b.append(series_b[1] + (i + 1) * 6)

combined_series = list(set(series_a).union(set(series_b)))
combined_series.sort()

expr = lambda n, x :n**2 + 2*x*n
for n in combined_series:
        removed = {}
        for j in range(input_range_integer):
                if expr(n, j) in combined_series and expr(n,j) <= max(combined_series):
                        combined_series.remove(expr(n, j))

                       
        print("For n = {0} , removed : {1}".format(n , removed))
        logger.info(("For n = {0} , removed : {1}".format(n, removed)))

print(','.join([str(item) for item in combined_series]))

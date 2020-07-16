# Yeah, an edited version of the code. A joint project (or repo ?) by Mr Sinan Islekdemir and me !
import sys # so as to use the program as a command in the shell cmd.exe or bash
import logging # to log the o/p on screen

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

c_handler = logging.StreamHandler()
logger.addHandler(c_handler)

if len(sys.argv) < 2: # when the required number of args are missing.
    print("Not enough parameters, range is missing")
    exit(1)

if len(sys.argv) > 2: # when you go for excess (too bad !)
    print("Too many parameters.")
    exit(2)

input_range = sys.argv[1]
if not input_range.isnumeric(): # yeah , you got it right - we require numbers and not letters !
    print("Range must be a number")
    exit(3)
# my calculation is a bit cumbersome but still mathematically correct one to get rid of composites (though the time it takes to work is really disappointing)
input_range_integer = int(input_range)

series_a = [2, 5] 
series_b = [3, 7]

for i in range(input_range_integer):
    series_a.append(series_a[1] + (i + 1) * 6)
    series_b.append(series_b[1] + (i + 1) * 6)

combined_series = list(set(series_a).union(set(series_b)))
combined_series.sort() # a combined list to filter our prime numbers from

expr = lambda n, x :n**2 + 2*x*n # my quadratic sieve function !
for n in combined_series:
        removed = {}
        for j in range(input_range_integer):
                if expr(n, j) in combined_series and expr(n,j) <= max(combined_series):
                        combined_series.remove(expr(n, j))
                        removed.update({(j+1) : expr(n, j)})
                        # I hope you'll understand the rest of the process.
                       
        logger.info(("For n = {0} , removed : {1}".format(n, removed)))

print(','.join([str(item) for item in combined_series]))

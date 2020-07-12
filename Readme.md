Yeah, I'm back with a new prime sieve (although many discussion groups say this <u><b>isn't</b></u> significant - neither an improvement over the sieve of Eratosthenes nor a cut above the sieve of Atkin.
But this is an interesting programming exercise , according to one of those research helpers in Wikipedia - Jasper Deng; he's a really nice person and a good mentor ! Therefore, I decided to create this 
command-line tool for Windows (those willing to make distributions for Mac OS, Linux, etc. may fork this repo and get the code edited).
________
<u><h1>1. What Is This ?</h1></u>
A simple command-line tool to generate prime numbers and print it on your cmd.exe screen.

<u><h1>2. Why Did You Make This?</h1></u>
Seriously telling, my mind persuaded me to go innovative during this lockdown period. My innovative thinking made me get into this small idea.

<u><h1> 3. How Did You Make It ?</h1></u>
I have heard that prime numbers greater than 3 are of the form 6n - 1 or 6n + 1. Using this , the program generates the sample to be filtered, which is the filtered using the function 
<i><font face = "Lucida Calligraphy"> f(n, x) = n<sup>2</sup> + 2nx </font> </i> (= n (n + 2x) here, x is a counter), which produces some of the odd composites when n is odd. Thus
from a set consisting the sample, the filtration function I made (called quadratic sieving function) removes all possible occurences of odd composites (since the sample only contains
odd composites alongside primes).

<u><h1> 4. How Can Others Contribute </h1></u>
Others may fork this repo , make changes in the code to make it faster ( I made a slow version of this...)

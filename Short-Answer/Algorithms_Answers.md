#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

    a = 0
    while (a < n * n * n):
      a = a + n * n

a)  Being that a true or false decision is being mane of n and 'a' is not a constant if n cubed is greater than 'a' (by replacing 'a' with a + n squared if 'a' is smaller), the size of n might impact the complexity of the runtime. therefore O(n).


    sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1

b)  starting off i in range(n) makes the problem already dependant of the length of n. from there the value of both j and sum can change depending on the range of n. therefore O(n log(n)).


    def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

c) Recursive algorithm (calls on itself). if bunnies not 0, returns 2 + bunnies-1. one input and output at a time (with one step). therefore 0(n). 

## Exercise II


identify the first floor f = n[0] and start droping one egg for every single floor incrementing from the beggining (egg == 1). once an egg breaks (if the egg is returned as 0), stop droping eggs and return the number of the floor in which egg broke. runtime is 0(log(n)) depending on the size of the 'n' building due to the computation taking longer with buildings with many floors.
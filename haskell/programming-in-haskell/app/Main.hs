module Main (main) where

import Lib

main :: IO ()
main = someFunc


{--
1. Using a list comprehension, give an expression that calculates the sum 1^2 + 2^2 + ... 100^2
of the first one hundred integer squares.»

ghci> [x^2| x <- [1 .. 100]]
--}

{--
2. Suppose that a coordinate grid of size m × n is given by the list of all pairs (x, y)
of integers such that 0 <= x <= m and  0 <= y <= n. Using a list comprehension, 
define a function grid :: Int -> Int -> [(Int,Int)] that returns a coordinate
grid of a given size. 

For example:

ghci> grid 1 2
    [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2)]
--}

{--
3. Using a list comprehension and the function grid above, define a function 
square :: Int -> [(Int,Int)] that returns a coordinate square of size n,
excluding the diagonal from (0, 0) to (n, n). 

For example:

> square 2
[(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)]»

--}

{--
4. In a similar way to the function length, show how the library function 
replicate :: Int -> a -> [a] that produces a list of identical elements can
be defined using a list comprehension. For example:

> replicate 3 True
[True,True,True]

--}

{--
5. A triple (x, y, z) of positive integers is Pythagorean if it satisfies the
    equation x^2 + y^2 = z^2. Using a list comprehension with three generators,
    define a function pyths :: Int -> [(Int,Int,Int)] that returns the list of
    all such triples whose components are at most a given limit. For example:

> pyths 10
[(3,4,5),(4,3,5),(6,8,10),(8,6,10)]
--}

{--
6. A positive integer is perfect if it equals the sum of all of its factors,
    excluding the number itself. Using a list comprehension and the function factors, 
    define a function perfects :: Int -> [Int] that returns the list of all perfect
     numbers up to a given limit. For example:

> perfects 500
[6,28,496]
--}

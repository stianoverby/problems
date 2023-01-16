{-
Problem
    Filter a given array of integers and output only those values that are less 
    than a specified value X. The output integers should be in the same sequence
    as they were in the input. You need to write a function with the recommended
    method signature for the languages mentioned below.

Input Format

    The first line contains the delimiter X. The next B lines each contain an integer,
    which represents the elements of the list/array. You have to read the input
    to the End-Of-File.

Output Format

Print all the integers from the array that are less than the given upper limit 
in value on separate lines. The sequence should be the same as it was in the
original array.

Constraints
    1 <= B <= 100
    For any element, Y in the aray, -100 <= Y <= 100
    -100 <= X <= 100

Source: https://www.hackerrank.com/challenges/fp-filter-array/problem
-}

removeSmaller :: Int -> [Int] -> [Int]
removeSmaller n [] = []
removeSmaller n (x:xs) = if x < n 
                            then x:(f n xs) 
                            else (f n xs)

main = do 
    n <- readLn :: IO Int 
    inputdata <- getContents 
    let 
        numbers = map read (lines inputdata) :: [Int] 
    putStrLn . unlines $ (map show . removeSmaller n) numbers
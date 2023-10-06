module Lib
    ( grid
    , square
    , replicate'
    , pyths
    , factors
    , listToMaybe
    ) where


grid :: Int -> Int -> [(Int,Int)]
grid n m = [(x,y) | x <- [0 .. n], y <- [0 .. m]]

square :: Int -> [(Int,Int)]
square n = [(x,y) | (x,y) <- (grid n n), x /= y]

replicate' :: Int -> a -> [a]
replicate' n a = [a |  _ <- [1 .. n]]

pyths :: Int -> [(Int,Int,Int)]
pyths limit = [(x,y,z)| x <- range, y <- range, z <- range, (x^2 + y^2) == z^2 ]
    where range = [1 .. limit]

perfects :: Int -> [Int]
perfects limit = [x | x <- [1 .. limit], (sum $ factors x) == x] 


factors :: Int -> [Int]
factors 1 = []
factors n = maybe [n] (\a -> a : factors (n `div` a)) mval
  where
    mval = listToMaybe $ filter (\x -> (n `mod` x) == 0) [2 .. n - 1]

listToMaybe :: [a] -> Maybe a
listToMaybe [] = Nothing
listToMaybe (x:_) = Just x
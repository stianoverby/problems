{-
Problem
    For a given list with N integers, return a new list removing the elements at odd positions. The input and output portions will be handled automatically. You need to write a function with the recommended method signature.

Input Format
    N integers contained in the list, each on a separate line.

Output Format
    Output the list with the integers at odd positions removed i.e. the first element, the third element and so on. The relative positions of the remaining even-position elements should be the same as they were in the original array. Each integer will be on a separate line.

Source: https://www.hackerrank.com/challenges/fp-filter-positions-in-a-list/
-}

-- Functional composition solution
filterOddPos :: [Int] -> [Int]
filterOddPos = map snd . filter (even . fst) . zip [1..]

-- Pattern matching solution
{-
filterOddPos [] = []
filterOddPos (x:[]) = []
filterOddPos (x:y:xs) = y:(filterOddPos xs)
-}


-- This part deals with the Input and Output and can be used as it is. Do not modify it.
main = do
	inputdata <- getContents
	mapM_ (putStrLn. show). filterOddPos . map read. lines $ inputdata
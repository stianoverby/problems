groupByFour :: String -> [String]
groupByFour [] = []
groupByFour xs = take 4 xs : groupByFour (drop 1 xs)

groupByFourteen :: String -> [String]
groupByFourteen [] = []
groupByFourteen xs = take 14 xs : groupByFourteen (drop 1 xs)

allDifferent :: String -> Bool
allDifferent list = case list of
    []      -> True
    (x:xs)  -> x `notElem` xs && allDifferent xs

indexOfTrue :: [Bool] -> [Int]
indexOfTrue xs = [i | (i, x) <- zip [0..] xs, x]

addCost :: Int -> [Int] -> [Int]
addCost n xs = [i + n | i <- xs]

getCostOfValidS1 :: [Bool] -> [Int]
getCostOfValidS1 = (addCost 4) . indexOfTrue

getCostOfValidS2 :: [Bool] -> [Int]
getCostOfValidS2 = (addCost 14) . indexOfTrue

solver1 :: [String] -> [Int]
solver1 = map head . map getCostOfValidS1 . map (map allDifferent) . map groupByFour

solver2 :: [String] -> [Int]
solver2 = map head . map getCostOfValidS2 . map (map allDifferent) . map groupByFourteen

main =  do
        contents <- readFile "input"
        let readLines = lines contents
        let s1 = solver1 readLines
        let s2 = solver2 readLines
        print(s1)
        print(s2)


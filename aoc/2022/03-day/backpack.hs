import Data.Char (Char)
import qualified Data.Char as Char

firstHalf :: [a] -> [a] 
firstHalf x = take (length x `div` 2) x

lastHalf :: [a] -> [a]
lastHalf x = drop (length x `div` 2) x

divideString :: String -> [String]
divideString xs = [firstHalf xs, lastHalf xs]

groupByThree :: [String] -> [[String]]
groupByThree [] = []
groupByThree xs = take 3 xs : groupByThree (drop 3 xs)

commonChar :: [String] -> Char
commonChar [] = error "empty list"
commonChar [x] = head x
commonChar (x:xs) = head [c | c <- x, all (\s -> c `elem` s) xs]

charToVal :: Char -> Int
charToVal c = if Char.isUpper c
                then Char.ord c - 64 + 26
                else Char.ord c - 96

solver1 :: [String] -> Int
solver1 = sum . map charToVal . map commonChar . map divideString

solver2 :: [String] -> Int
solver2 = sum . map charToVal . map commonChar . groupByThree

main =  do
        contents <- readFile "input"
        let readLines = lines contents
        let s1 = solver1 readLines
        let s2 = solver2 readLines
        print(s1)
        print(s2)

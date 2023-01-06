splitOn :: (a->Bool) -> [[a]] -> [[[a]]]
splitOn pred xs = map (splitOn' pred) xs

splitOn' :: (a->Bool) -> [a] -> [[a]]
splitOn' _ [] = []
splitOn' pred lst@(x:xs)
        | pred x = splitOn' pred xs
        | otherwise = let (front,back) = break pred lst in front:(splitOn' pred back) 
        -- Groups the lst into a list of two tuples split on the element

overlap :: [[String]] -> [Bool]
overlap xs = map (\[a,b] -> overlap' a b) xs

overlap' :: String -> String -> Bool
overlap' a b =
        let (a1, a2) = parseRange a
            (b1, b2) = parseRange b
        in (a1 <= b2 && b1 <= a2)

completeOverlap :: [[String]] -> [Bool]
completeOverlap xs = map (\[a,b] -> completeOverlap' a b) xs

completeOverlap' :: String -> String -> Bool
completeOverlap' a b =
        let (a1, a2) = parseRange a
            (b1, b2) = parseRange b
        in (a1 <= b1 && b2 <= a2) || (b1 <= a1 && a2 <= b2)

parseRange :: String -> (Int, Int)
parseRange s =
        let (a, b) = span (/= '-') s
        in (read a, read $ drop 1 b)

splitOnComma = splitOn (\x -> x == ',')
calculateVal = sum . map (\x -> if x == False then 0 else 1) 

main =  do
        contents <- readFile "input"
        let intervals = splitOnComma $ lines contents
        let s1 = calculateVal $ completeOverlap intervals
        let s2 = calculateVal $ overlap intervals
        print(s1, s2)
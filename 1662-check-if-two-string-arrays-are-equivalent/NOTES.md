what i did was just iterated once over word 1 and once over word 2 if the resuting strings were equal (==) return true else return false 
time complexity O(n)+O(n)\n\n

#Method 2
i could have made it in another way resulting in a faster time complexty which is having i j a b all =0 i and a associated with word1 and j and b with word2 and while i<lenword1 and j <=len word2: and then proced to incriment a and b if the stirng isnt over yet and i and j while the string is finished . and ofcourse if a letter in 1 is diff than its the same place in 2 return false\n

when the while is finished i should check if i a is the last element of word 1 and j b is the last lettero of word2 if yes return true else return false.\n
this should reduce the time complexity to O(n) only

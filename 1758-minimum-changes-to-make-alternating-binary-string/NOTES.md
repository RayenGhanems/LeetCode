# Counting the number of times i need to change a letter:
  I simply just got a character called b that keeps track of what the character should be. each time i itereate through the stirng i change b accordingly. 
  
  # Return
  No for the return we rreturn the out ​if the return is les thatn len(s)/2 else we return len(s) - out since it would be better to change the ones we didnt consider changing in our first iterateion

  ## Example
  11010101
  so basically the first loop for loop will say oh so b =1 hence the out will be 7 so 10101010 but as we know if we only change the fist 1 it would be beter or basicaly the minimum which is len(s) - out since 7 was bigger than len(s) /2

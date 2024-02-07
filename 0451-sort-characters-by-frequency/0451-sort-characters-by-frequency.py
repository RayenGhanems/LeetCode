from collections import Counter
from operator import itemgetter

class Solution:
    def frequencySort(self, s):
        frequency = Counter(s)
        sorted_characters = sorted(frequency.items(), key=itemgetter(1), reverse=True)    
        result = ''.join(char * freq for char, freq in sorted_characters)
        
        return result
    
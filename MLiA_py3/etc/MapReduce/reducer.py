from operator import itemgetter
import sys

def reducer(after_mapper):

    current_word = None
    current_count = 0
    word = None 
    dic_result = {}    
    
    for line in after_mapper:
        word, count = line
        try:
            count = int(count)
        except valueError:
            continue

        if word in dic_result:
            dic_result[word] += 1
        else:
            dic_result[word] = 1

    return dic_result
        
"""
from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None 

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t',1)
    try:
        count = int(count)
    except valueError:
        continue
        
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print('%s\t%s' % (current_word, current_count))
            
        current_count = count
        current_word = word
        
    if current_word == word:
        print('%s\t%s') % (current_word, current_count)
        
echo "foo foo quux labs foo bar quux" | /home/hduser/mapper.py | sort -k1,1 | /home/hduser/reducer.py
"""
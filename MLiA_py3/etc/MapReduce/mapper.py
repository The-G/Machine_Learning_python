import sys

def mapper(text):
    print("text is:",text)
    after_map=[]
    for line in text.split():
        line = line.strip()
        words = line.split()
        for word in words:
            after_map.append((word,1))
            print('%s\t%s' % (word, 1))
            
    return after_map
        
"""
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print('%s\t%s' % (word, 1))
        
echo "foo foo quux labs foo bar quux" | /home/hduser/mapper.py
"""


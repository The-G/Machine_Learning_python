import sys

def mapper(text):
    print("text is:",text)
    for line in text:
        line = line.strip(" ")
        print("line : ", line)
        words = line.split()
        for word in words:
            print('%s\t%s' % (word, 1))
        
"""
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print('%s\t%s' % (word, 1))
"""


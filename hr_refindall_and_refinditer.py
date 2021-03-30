# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
m = re.findall("(?<=[^AEIOU])([AEIOU]{2,})(?=[^AEIOU])", raw_input(), re.IGNORECASE)

if not len(m):
        print(-1)
else:
    for i in m:
            print(i)
# working with regular expressions (double star search  and replace on '!')
import re
reStr = re.sub(r'\s\*\s', ' ! ', 'aaa ** bbb * eee * bcd **')
print(reStr)
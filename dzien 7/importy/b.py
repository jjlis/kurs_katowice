
import sys
print(sys.path)

import a
print(dir(a))
a.hello()


from a import hello

hello()
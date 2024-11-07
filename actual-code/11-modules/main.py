# import utils   # import in a namespaced way (utils.add(), etc)
# import utils as u   # alias utils as "u" (u.add(), etc)
from utils import add, name   # import individual pieces
from utils import add as other_add

def add(a,b):
    return a - b

# print(add(4,5))
# print(name)

print(other_add(4,5))
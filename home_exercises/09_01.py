import sys
import array

last_item = 100000
list_int = [i for i in range(last_item)]
tuple_int = tuple(list_int)
# sys.getsizeof() - memory reservation size (heap memory)
array_int = array.array('i', list_int)
dict_int_str = {int(i): int(i) for i in range(last_item)}

print(f"Memory used: {sys.getsizeof(list_int)} bytes")
print(f"Memory used: {sys.getsizeof(tuple_int)} bytes")
print(f"Memory used: {sys.getsizeof(array_int)} bytes")
print(f"Memory used: {sys.getsizeof(dict_int_str)} bytes")
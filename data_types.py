#!/usr/bin/env python3

print('Text Type')

var_str = 'string'
print(var_str)
print(type(var_str))

print('\nNumeric Types')

var_int = 55
print(var_int)
print(type(var_int))

var_float = 5.5
print(var_float)
print(type(var_float))

var_complex = 5j
print(var_complex)
print(type(var_complex))

print('\nSequence Types')

var_list = ['this','is','a','list']
print(var_list)
print(type(var_list))

var_tuple = ('this','is','a','tuple')
print(var_tuple)
print(type(var_tuple))

var_range = range(4)
print(var_range)
print(type(var_range))

print('\nMapping Type')

var_dict = {'zero':0,'one':1,'two':2,'three':3,'four':4}
print(var_dict)
print(type(var_dict))

print('\nSet Types')

var_set = {'vanilla','chocolate','mint','caramel'}
print(var_set)
print(type(var_set))

var_frozenset = frozenset({'birch','maple','oak','pine'})
print(var_frozenset)
print(type(var_frozenset))

print('\nBoolean Type')

var_bool = True
print(var_bool)
print(type(var_bool))

print('\nBinary Types')

var_bytes = bytes('immutable','UTF-8')
print(var_bytes)
print(type(var_bytes))

var_bytesarray = bytearray('mutable','UTF-8')
print(var_bytesarray)
print(type(var_bytesarray))

var_memoryview = memoryview(bytes('256','UTF-8'))
print(var_memoryview.obj)
print(type(var_memoryview))

print('\nNone Type')

var_nonetype = None
print(var_nonetype)
print(type(var_nonetype))


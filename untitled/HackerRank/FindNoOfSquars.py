#!/bin/python

import sys
import os

def  getMinimumUniqueSum(arr):
    rtrn_arr = []
    print(arr)
    for x in arr:
        print(x)
        a = x[0]
        b = x[1]
        count = 0
        for i in range (a,b+1):
            j = 1
            while j*j <= i:
                if j*j == i:
                     count = count+1
                j = j+1
            i = i+1
        rtrn_arr.append(count)
    return rtrn_arr



_arr_cnt = int ( input ( 'count : ') )
_arr_i = 0
_arr = [ ]
while _arr_i < _arr_cnt:
    _arr_item = input ('values : ' )
    _arr.append ( _arr_item )
    _arr_i += 1

res = getMinimumUniqueSum ( _arr )
for res_cur in res:
    print ( str ( res_cur ) + "\n" )

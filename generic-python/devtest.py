#!/usr/bin/env python 
################################################################
# Filename: devtest.py
# Location: /home/ssatish/temp/code-challenges/generic-python
# Project : 
# Date    : 2016-07-01
# Author  : ssatish
# Scope   : 
# Usage   : 
################################################################

import os
import sys
from datetime import datetime

###############################
# Constants
###############################
BASH_RCODE_FAILURE=1
BASH_RCODE_SUCCESS=0
FUNCTION_RCODE_FAILURE=0
FUNCTION_RCODE_SUCCESS=1

###############################
# Class: Solutions
###############################
class Solutions():

    def __init__(self):
        pass

    def greater_than_avg( self, _list):

        rlist = []
        
        if( not isinstance( _list, list)):
            return rlist
    
        avg = 0
        total = 0
        valid_count = 0
        for x in _list:
            if( isinstance( x, int)):
                total += x
                valid_count = valid_count+1

        avg = total / valid_count
        
        for x in _list:
            if( isinstance( x, int)):
                if x > avg:
                    rlist.append(x)
        
        return rlist

    def sort_fruit( self, _fruits):

        DICT_TAG_FRUIT_NAME = 'word'
        DICT_TAG_FRUIT_COUNT = 'count'

        rvalue = []
        
        if( not isinstance( _fruits, list)):
            return rvalue        

        name_temp = None
        count_temp = None
        
        fruit_dict = dict()
        for f in _fruits:
        
            name_temp = f.get(DICT_TAG_FRUIT_NAME)
            count_temp = f.get(DICT_TAG_FRUIT_COUNT)

            if( name_temp and count_temp):
                fruit_dict[count_temp] = name_temp

        k = None
        v = None
        for k, v in fruit_dict.items():
            temp = dict()
            temp[DICT_TAG_FRUIT_NAME] = str(v)
            temp[DICT_TAG_FRUIT_COUNT] = int(k)            
            rvalue.append(temp)

        return rvalue

    def transpose_dict( self, _in):
    
        rvalue = dict()
        
        if( not isinstance( _in, dict)):
            return rvalue
        
        for k, v in _in.items():
            rvalue[v] = k
        
        return rvalue
    
    def week_start_end( self, _in):
    
        rval_start = datetime()
        rval_end = datetime()
        
        if( not isinstance( _in, datetime())):
            return rvalue
        
        return (rval_start, rval_end)
    

###############################
# Function: devtest
###############################
def devtest():
    pass

###############################
# Function: main 
###############################
def main():
    return devtest()

if __name__ == "__main__":
    sys.exit( main())



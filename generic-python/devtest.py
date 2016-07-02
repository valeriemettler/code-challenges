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

    ###############################
    # Function: greater_than_avg
    ###############################
    def greater_than_avg( self, _list):

        rlist = []

        # Input must be a list
        if( not isinstance( _list, list)):
            return rlist
    
        avg = 0
        total = 0
        valid_count = 0
        for x in _list:

            # Element must be an Integer
            if( isinstance( x, int)):
                total += x
                valid_count = valid_count+1

        avg = total / valid_count
        
        for x in _list:

            # Element must be an Integer
            if( isinstance( x, int)):
                if x > avg:
                    rlist.append(x)
        
        return rlist

    ###############################
    # Function: sort_fruit
    ###############################
    def sort_fruit( self, _fruits):

        DICT_TAG_FRUIT_NAME = 'word'
        DICT_TAG_FRUIT_COUNT = 'count'

        rvalue = []

        # Input must be a list
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

    ###############################
    # Function: transpose_dict
    ###############################
    def transpose_dict( self, _in):
    
        rvalue = dict()

        # Input must be a dict
        if( not isinstance( _in, dict)):
            return rvalue
        
        for k, v in _in.items():
            rvalue[v] = k
        
        return rvalue

    ###############################
    # Function: week_start_end
    ###############################
    def week_start_end( self, _in):
    
        rval_start = None
        rval_end = None

        # Element must be an datetime
        if( not isinstance( _in, datetime())):
            return None
        
        return (rval_start, rval_end)

    ###############################
    # Function: test_month_last_day
    ###############################
    def month_last_day( self, _in):
        rvalue = 0

        # Element must be an datetime
        if( not isinstance( _in, datetime)):
            return rvalue

        LEAP_YEAR_CYCLE=4
        MONTH_OFFSET_SPLIT = 8


        month = _in.month
        if(month >= MONTH_OFFSET_SPLIT):
            if( month%2 == 0):
                rvalue=31
            else:
                rvalue=30
        elif( month != 2):
            if( month%2 == 0):
                rvalue=30
            else:
                rvalue=31
        else:
            if( (_in.year%LEAP_YEAR_CYCLE) == 0):
                rvalue = 29
            else:
                rvalue = 28

        return rvalue

    ###############################
    # Function: palindrome_test_function
    ###############################
    def palindrome_test_function( self):
        return is_palindrome

    ###############################
    # Function: string_parse
    ###############################
    def string_parse( self, _in):

        rvalue = []

        # Element must be an string
        if( not isinstance( _in, str)):
            return rvalue

        ROW_SEPARATOR_LINE="+------------------------------------+-----------------------------------+"
        COL_SEPARATOR_CHAR="|"
        COL_START_INDEX = 0
        COL_VALUE_START_OFFSET = 1

        t = _in.split( ROW_SEPARATOR_LINE)

        ROW_MIN_TOKENS = 2

        for x in t:
            temp = x.split(COL_SEPARATOR_CHAR)

            # Skip: Empty values
            if( ROW_MIN_TOKENS > len(temp)):
                continue

            # Trim out new line characters
            col_values = []
            for word in temp:
                if( word != '\n'):
                    col_values.append(word)

            # Column Headers: Skip: Start with lowercase letter
            col_start_char = col_values[COL_START_INDEX][COL_VALUE_START_OFFSET]
            if( (col_start_char.islower()) ):
                continue

            like_temp = str()
            current_col = str()
            dislike_temp = str()
            for index in xrange(0, len(col_values)):

                if( (index%2) ==0 ):
                    current_col = col_values[index].strip()
                    if(len(current_col)):
                        if(len(like_temp)):
                            like_temp = like_temp + " " + current_col
                        else:
                            like_temp = col_values[index].strip()
                else:
                    current_col = col_values[index].strip()
                    if(len(current_col)):
                        if(len(dislike_temp)):
                            dislike_temp = dislike_temp + " " + current_col
                        else:
                            dislike_temp = col_values[index].strip()

            rvalue.append( (  unicode(like_temp), unicode(dislike_temp)))

        return rvalue

###############################
# Function: is_palindrome
###############################
def is_palindrome(_in):

    if( not isinstance( _in, str)):
        return False

    # Normalize input
    temp = str()
    for x in _in:
        if( x.isalnum()):
            temp = temp + x.lower();

    count = len(temp)
    last_index = count-1
    for i in xrange(count/2):
        if( temp[i] != temp[last_index-i]):
            return False

    return True

###############################
# Function: devtest
###############################
def devtest():

    i="Test"
    is_palindrome(i)

###############################
# Function: main 
###############################
def main():
    return devtest()

if __name__ == "__main__":
    sys.exit( main())



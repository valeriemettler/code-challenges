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

"""
    ZeroCater Python challenge, devtest module
"""

import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta

###############################
# Constants
###############################
BASH_RCODE_FAILURE = 1
BASH_RCODE_SUCCESS = 0
FUNCTION_RCODE_FAILURE = 0
FUNCTION_RCODE_SUCCESS = 1

###############################
# Class: Solutions
###############################
class Solutions(object):

    """
        ZeroCater Python challenge, Solutions class
    """

    def __init__(self):
        pass

    ###############################
    # Function: greater_than_avg
    ###############################
    def greater_than_avg(self, _list):

        """
        :param _list: List of integers
        :return: sub list of all numbers that are greater than average of inputlist
        """

        rlist = []

        # Input must be a list
        if not isinstance(_list, list):
            return rlist

        avg = 0
        total = 0
        valid_count = 0
        for element in _list:

            # Element must be an Integer
            if isinstance(element, int):
                total += element
                valid_count = valid_count+1

        avg = total / valid_count

        for element in _list:

            # Element must be an Integer
            if isinstance(element, int):
                if element > avg:
                    rlist.append(element)

        return rlist

    ###############################
    # Function: sort_fruit
    ###############################
    def sort_fruit(self, _fruits):

        """
        :param _fruits: List of fruit dict with word and count
        :return: List of fruit ordered by count in ascending order
        """

        DICT_TAG_FRUIT_NAME = 'word'
        DICT_TAG_FRUIT_COUNT = 'count'

        rvalue = []

        # Input must be a list
        if not isinstance(_fruits, list):
            return rvalue

        name_temp = None
        count_temp = None

        fruit_dict = dict()
        for fruit in _fruits:

            # Elements must have { 'word', 'count'} attributes
            name_temp = fruit.get(DICT_TAG_FRUIT_NAME)
            count_temp = fruit.get(DICT_TAG_FRUIT_COUNT)
            if name_temp and count_temp:
                fruit_dict[count_temp] = name_temp

        key = None
        value = None
        for key, value in fruit_dict.items():
            temp = dict()
            temp[DICT_TAG_FRUIT_NAME] = str(value)
            temp[DICT_TAG_FRUIT_COUNT] = int(key)
            rvalue.append(temp)

        return rvalue

    ###############################
    # Function: transpose_dict
    ###############################
    def transpose_dict(self, _in):

        """
        :param _in: Dictionary
        :return:    Dictionary with key and values reversed
        """

        rvalue = dict()

        # Input must be a dict
        if not isinstance(_in, dict):
            return rvalue

        for key, value in _in.items():
            rvalue[value] = key

        return rvalue

    ###############################
    # Function: week_start_end
    ###############################
    def week_start_end(self, _in):

        """
        :param _in: Must be a instance of datetime
        :return: Tuple with two datetime elements ( week_start, week_end)
        """

        rval_start = None
        rval_end = None

        # Element must be an datetime
        if not isinstance(_in, datetime):
            return None

        # Week start
        WEEKDAY_MONDAY_VALUE = 0
        temp = _in
        temp = temp.replace(temp.year, temp.month, temp.day, 0, 0, 0, 0)
        while WEEKDAY_MONDAY_VALUE != temp.weekday():
            temp = temp - relativedelta(days=1)
        rval_start = temp

        # Week end
        WEEKDAY_SUNDAY_VALUE = 6
        temp = _in
        temp = temp.replace(temp.year, temp.month, temp.day, 23, 59, 59, 999999)
        while WEEKDAY_SUNDAY_VALUE != temp.weekday():
            temp = temp + relativedelta(days=1)
        rval_end = temp

        return (rval_start, rval_end)

    ###############################
    # Function: test_month_last_day
    ###############################
    def month_last_day(self, _in):

        """
        :param _in: Must be datetime
        :return:    int, last day of the month
        """

        rvalue = 0

        # Element must be an datetime
        if not isinstance(_in, datetime):
            return rvalue

        LEAP_YEAR_CYCLE = 4
        MONTH_OFFSET_SPLIT = 8

        month = _in.month
        if month >= MONTH_OFFSET_SPLIT:
            if month%2 == 0:
                rvalue = 31
            else:
                rvalue = 30
        elif month != 2:
            if month%2 == 0:
                rvalue = 30
            else:
                rvalue = 31
        else:
            if (_in.year%LEAP_YEAR_CYCLE) == 0:
                rvalue = 29
            else:
                rvalue = 28

        return rvalue

    ###############################
    # Function: palindrome_test_function
    ###############################
    def palindrome_test_function(self):

        """
        :return: returns a palindrome test function that take test string as input
        """

        return self.is_palindrome

    def is_palindrome(self, _in):

        """is_palindrome: If input is a string and if it's palindrome return True,
                          False otherwise"""

        if not isinstance(_in, str):
            return False

        # Normalize input
        temp = str()
        for char in _in:
            if char.isalpha():
                temp = temp + char.lower()

        count = len(temp)
        last_index = count-1
        for index in xrange(count/2):
            if temp[index] != temp[last_index-index]:
                return False

        return True

    ###############################
    # Function: string_parse
    ###############################
    def string_parse(self, _in):

        """
        :param _in: String, that has likes & dislikes
        :return:    List, of tuples with two unicode strings one each for like & dislike
        """

        rvalue = []

        # Element must be an string
        if not isinstance(_in, str):
            return rvalue

        ROW_SEPARATOR_LINE = "+------------------------------------+" \
                             "-----------------------------------+"
        COL_SEPARATOR_CHAR = "|"
        COL_START_INDEX = 0
        COL_VALUE_START_OFFSET = 1

        tokens = _in.split(ROW_SEPARATOR_LINE)

        ROW_MIN_TOKENS = 2

        for token in tokens:
            temp = token.split(COL_SEPARATOR_CHAR)

            # Skip: Empty values
            if ROW_MIN_TOKENS > len(temp):
                continue

            # Trim out new line characters
            col_values = []
            for word in temp:
                if word != '\n':
                    col_values.append(word)

            # Column Headers: Skip: Start with lowercase letter
            col_start_char = col_values[COL_START_INDEX][COL_VALUE_START_OFFSET]
            if col_start_char.islower():
                continue

            like_temp = str()
            dislike_temp = str()
            for index in xrange(0, len(col_values)):

                if (index%2) == 0:
                    current_col = col_values[index].strip()
                    if len(current_col):
                        if len(like_temp):
                            like_temp = like_temp + " " + current_col
                        else:
                            like_temp = col_values[index].strip()
                else:
                    current_col = col_values[index].strip()
                    if len(current_col):
                        if len(dislike_temp):
                            dislike_temp = dislike_temp + " " + current_col
                        else:
                            dislike_temp = col_values[index].strip()

            rvalue.append((unicode(like_temp), unicode(dislike_temp)))

        return rvalue

###############################
# Function: devtest
###############################
def devtest():
    """Test function"""
    pass

###############################
# Function: main
###############################
def main():
    """Main function"""
    return devtest()

if __name__ == "__main__":
    sys.exit(main())



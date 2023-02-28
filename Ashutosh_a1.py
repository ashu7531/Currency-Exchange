"""
Module for currency exchange
This module provides several string parsing functions to
implement a
simple currency exchange routine using an online currency
service.
The primary function in this module is exchange.
Author: ASHUTOSH KUMAR
Date: 30 NOV 2022
"""
def before_space(s):
    """
    Returns a copy of s up to, but not including, the first space
    Examples:
    >>> before_space("4.502 Euros")
    '4.502'
    >>> before_space("2 Rupees")
    '2'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space"""
    a=s.find(" ")
    return s[0:a]

def after_space(s):

    """Returns a copy of s up to, but not including, the first space
    Examples:
    >>> after_space("4.502 Euros")
    'Euros'
    >>> after_space("2 Rupees")
    'Rupees'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space"""
    a=s.find(" ")
    return s[a+1:]
def first_inside_quotes(s):
    """Returns the first substring of s between two (double) quotes
    A quote character is one that is inside a string, not one that
    string if we want to use a double quote character (") inside of 
    it.
    Examples:
    >>> first_inside_quotes('A "B C" D')
    'B C'
    >>> first_inside_quotes('A "B C" D "E F" G')
    'B C'

    Parameter s: a string to search
    Precondition: s is a string containing at least two double
    quotes"""
    a=s.find('"')
    b=s[a+1:]
    c=b.find('"')
    return b[0:c]
def get_lhs(json):
    """Returns the lhs value in the response to a currency query
    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the
    keyword
    "lhs".
    Examples:
    >>> get_lhs('{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }')
    '1 Bitcoin'
    >>> get_lhs('{ "lhs" : "1 USD", "rhs" : "81.63 INR", "err" : "" }')
    '1 USD'
    
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    a=json.find(':')
    b=json[a+3:]
    c=b.find('"')
    return b[0:c]
def get_rhs(json):
    """Returns the rhs value in the response to a currency query
    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the
    keyword
    "rhs".
    Examples:
    >>> get_rhs('{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }')
    '19995.85429186 Euros'
    >>> get_rhs('{ "lhs" : "1 USD", "rhs" : "81.63 INR", "err" : "" }')
    '81.63 INR'

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    a=json.find(':')
    b=json[a+3:]
    c=b.find(':')
    d=b[c+3:]
    e=d.find('"')
    return d[0:e]
def has_error(json):
    """Returns True if the query has an error; False otherwise.
    Given a JSON response to a currency query, this returns True if
    there is an error message.
    Examples:
    >>> has_error('{ "lhs" : "1 Bitcoin", "rhs" : "19995.85429186 Euros", "err" : "" }')
    False
    >>> has_error('{ "lhs" : "", "rhs" : "", "err" : "Currency amount is invalid." }')
    True

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query"""
    a=json.find(',')
    return a==12
def query_website(old,new,amt):
    """
    Returns a JSON string that is a response to a currency query A currency query converts amt money in currency old to the
    currency new.
    Examples:

    Doctests :
    >>> query_website('USD','CUP',1)
    '{ "lhs" : "1 United States Dollar", "rhs" : "25.75 Cuban Pesos", "err" : "" }'
    >>> query_website('US','INR',2)
    '{ "lhs" : "", "rhs" : "", "err" : "Source currency code is invalid." }'

    Parameter old: the currency on hand
    Precondition: old is a string with no spaces or non-letters

    Parameter new: the currency to convert to
    Precondition: new is a string with no spaces or non-letters

    Parameter amt: amount of currency to convert
    Precondition: amt is a float"""
    import requests
    json = (requests.get(f'http://cs1110.cs.cornell.edu/2022fa/a1?old={old}&new={new}&amt={amt}')).text
    return json
def is_currency(code):
    """
    Returns: True if code is a valid (3 letter code for a) currency
    It returns False otherwise.
    Examples:
    >>> is_currency('USD')
    True
    >>> is_currency('ABC')
    False

    Parameter code: the currency code to verify
    Precondition: code is a string with no spaces or non-letters."""
    code=code.upper()
    return  (has_error(query_website(code,code,'1.0'))==False)
def exchange(old,new,amt):
    """
    Returns the amount of currency received in the given exchange.
    In this exchange, the user is changing amt money in currency
    old to the currency new. The value returned represents the
    amount in currency new.
    The value returned has type float.
    Examples:
    >>> exchange('USD','INR',1.0)
    '79.788013'
    >>> exchange('BSD','CUC',1)
    '1'
    
    Parameter old: the currency on hand
    Precondition: old is a string for a valid currency code

    Parameter new: the currency to convert to
    Precondition: new is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition: amt is a float
    """
    a=query_website(old,new,amt)
    exchange_amt=get_rhs(a)
    return before_space(exchange_amt)
# if __name__=='__main__':
#     import doctest
#     doctest.testmod()

    



    







    



    





    


	
	
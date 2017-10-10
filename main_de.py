# -*- coding: utf-8 -*-
from OpenCager import geocode

"""
    IN this example variables are defined directly in this script
    The order of the variables is mandatory
"""

input_csv='test/de_sample.csv'
output_csv='test/de_result.csv'
one_result = 1
countrycode='de'
add_request=1
no_annotations=1
api_key='a9d71b105b794835a36a77feec9c0606'
sleep_sec=1  #free account limit 1 request per second

geocode(api_key,input_csv,output_csv,one_result,countrycode,add_request,no_annotations,sleep_sec)

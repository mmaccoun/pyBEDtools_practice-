
# FILE NAME: practice_intervals.py
# CREATED : 6.3.2019
# LAST UPDATED: 6.3.2019
#
# IN PROGRESS
#
# TUTORIAL LINK : https://daler.github.io/pybedtools/intervals.html
#                   topics intervals : operator overloading
#
# practice with intervals in pybedtools 

import pybedtools as BED

#################################################
# CODE COPIED FROM TUTORIAL
#   this module enables viewing of aspects of features
import sys

def show_value(s):
    if sys.version_info.major == 2:
        if isinstance(s, unicode):
            return str(s)
    return s
#################################################
#get example bedtool object 
a = BED.example_bedtool('a.bed')

feat = a[0]
print(feat.chrom)
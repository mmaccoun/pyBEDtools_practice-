
# FILE NAME: practice_intersection.py
# CREATED : 6.3.2019
# LAST UPDATED: 6.3.2019
#
# TUTORIAL LINK : https://daler.github.io/pybedtools/intersections.html
#                   topics intro : operator overloading
#
# practice with intersections in pybedtools 
# 

import pybedtools as BED

#import example files 
a = BED.example_bedtool('a.bed')
b = BED.example_bedtool('b.bed')

intersect_a_b = a.intersect(b)

#save intersect_a_b(pybedtools object) as file
c = intersect_a_b.saveas("intersection_of_a_and_b.bed")
print(c)

# use + for intersect() w. arg -u
checkADDopp = a +  b
print(checkADDopp)


# use - for intersect() w. arg -v
checkSUBopp = a - b
print(checkSUBopp)
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      bhagarwal
#
# Created:     18/06/2012
# Copyright:   (c) bhagarwal 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def main():
   f = open("MultipleFunctionArgument.txt","r")
   data = f.read()
   ch = ''
   l = len(data)
   print l
   print data[:]
if __name__ == '__main__':
    main()


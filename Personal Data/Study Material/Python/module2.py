#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      bhagarwal
#
# Created:     21/06/2012
# Copyright:   (c) bhagarwal 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def underline(title):
    a = '_'
    print title +"\\n"+ a*len(title)

def call(name):
    underline(name)
def main():
    call("Bhupender")

if __name__ == '__main__':
    main()

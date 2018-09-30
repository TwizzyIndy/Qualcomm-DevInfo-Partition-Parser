#!/usr/bin/python

# Qualcomm DevInfo Parser
# by
# TwizzyIndy
# 9/2018

import os
import struct

def usage():
    print("")
    print("Qualcomm DevInfo Parser")
    print("by TwizzyIndy")
    print("9/2018")
    
    print("usage : python read_devinfo.py devinfo.img")
    print("")
    
def main():
    if( len(os.sys.argv) < 2 ):
        usage()
        return
    size = os.path.getsize(os.sys.argv[1])
    arg1 = open(os.sys.argv[1], 'r')
    content = 0
    devinfo = 0
    
    if( size is 29):
        content = arg1.read(29)
        devinfo = struct.unpack('>13sIIII', content) # for CPU 32Bit devices (armv7, armv7s)
                                                        # its gonna be 4 bytes for boolean data types ( struct.unpack('>13sIIII') )
                                                        # but if CPU 64Bit devices like arm64
                                                        # its gonna be 8 bytes for boolean
                                                        # ( struct.unpack('>13sQQ') )        
        
    elif (size is 25):
        content = arg1.read(25)
        devinfo = struct.unpack('>13sIII', content) # for CPU 32Bit devices (armv7, armv7s)
                                # its gonna be 4 bytes for boolean data types ( struct.unpack('>13sIII') )
                                # but if CPU 64Bit devices like arm64
                                # its gonna be 8 bytes for boolean
                                # ( struct.unpack('>13sQQ') )         
    else:
        print("not supported file type")
        return
    

    
    magic = devinfo[0]
    is_unlocked = ( "TRUE" if devinfo[1] is 1 else "FALSE" )
    is_tampered = ( "TRUE" if devinfo[2] is 1 else "FALSE" )
    is_critical_unlocked = ("TRUE" if devinfo[3] is 1 else "FALSE")
    
    if( size is 29 ):
        is_charger_screen_enabled = ("TRUE" if devinfo[4] is 1 else "FALSE")
    
    print("")
    print("magic : " + magic )
    print("is unlocked : " + str(is_unlocked)  )
    print("tampered : " + str(is_tampered) )
    print("critical unlocked : " + str(is_critical_unlocked) )
    
    if( size is 29):
        print("charger_screen_enabled : " + str(is_charger_screen_enabled) )
    
    print("")
    
    arg1.close()
    return

if __name__ == "__main__":
    main()
    
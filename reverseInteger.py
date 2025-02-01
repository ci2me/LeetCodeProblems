# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit 
# integer range [-2^31, 2^31 - 1], then return 0.
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        # reverse string
        out = x[::-1]
    
        # check if the sign of original was negative
        # convert to int
        if out[-1] == '-':
            output = -1*int(out[0:-1])
        else:
            output = int(out)
        # ensure it is no more than 32 bits
        if abs(output) > 2147483647:
            output = 0 
        return output
        

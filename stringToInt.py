#Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
#The algorithm for myAtoi(string s) is as follows:
#Whitespace: Ignore any leading whitespace (" ").
#Signedness: Determine the sign by checking if the next character is 
#'-' or '+', assuming positivity if neither present.
#Conversion: Read the integer by skipping leading zeros until a non-digit 
#character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
#Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then round the integer 
#to remain in the range. Specifically, integers less than -2^31 should be rounded to -2^31, and integers greater 
#than 2^31 - 1 should be rounded to 2^31 - 1.
#Return the integer as the final result.


# scrappy solution, poor time complexity
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # remove whitespace
        s = s.strip()
        output = ''
        sign = 1
        
        # return 0 for empty string
        if s == '':
            return 0
        # if negative number remove - and flip sign to negative
        if s[0] == '-':
            s = s[1::]
            sign = -1
        # if + as first character ignore
        elif s[0] == '+':
            s = s[1::]
        # if first character isnt a number or sign return 0
        else:
            try:
                char = int(s[0])
            except:
                return 0
                
        # for each character, check if its an int and add to string
        for c in s:
            try:
                char = int(c)
                output = output + c
            except ValueError:
                break
        if output == '':
            return 0
            
        output = int(output)

        # multiply by sign to make negative
        output = sign * output

        #if output is out of range, round
        if output < -2**31:
            output = -2**31
        if output > 2**(31)-1:
            output = 2**(31)-1
        return output

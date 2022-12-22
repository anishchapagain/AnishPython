"""
String variable and format(): provides the ability to do complex variable substitutions and value formatting
https://pyformat.info/

%c	character
%s	string conversion via str() prior to formatting
%i	signed decimal integer
%d	signed decimal integer
%u	unsigned decimal integer
%o	octal integer
%x	hexadecimal integer (lowercase letters)
%X	hexadecimal integer (UPPERcase letters)
%e	exponential notation (with lowercase 'e')
%E	exponential notation (with UPPERcase 'E')
%f	floating point real number
%g	the shorter of %f and %e
%G	the shorter of %f and %E

Escape Characters:\s Space, \n Newline, \r Carriage Return, \t Tab, \e Escape, \b Backspace
"""

#HW
words = "I Love Python"
name = 'Peter C'#['Peter C','ABC']
age=14#[14,19]
weight = 42.50 #[42.50,55]

print("My name is %s , i'm %d year old and i'm %f kg" % (name,age,weight))

#Controlling number of decimal values
print("My name is %s , i'm %d year old and i'm %.2f kg" % (name,age,weight))

#using format()
print("\n using Format - New")
print("My name is {} , i'm {} year old and i'm {} kg".format(name,age,weight)) #0 1 2
print("My name is {2} , i'm {0} year old and i'm {1} kg".format(name,age,weight))#0 1 2
print("My name is {2} , i'm {1} year old and i'm {0} kg".format(name,age,weight))#0 1 2
print("My name is {0} , i'm {1} year old and i'm {2} kg".format(name,age,weight))#0 1 2

#Advanced Use of Format
# :N, :>N, :^N, :c^N,, :c<N  (c=char to display, N: total contained number)
print("\n Advance Use << http://pyformat.info >>")

nameDict = {'name':'Peter C.','age':'35'}
values = [10,20,30,40,50,60]
print("\nMy name is {name} and i'm {age} years old!".format(name="Peter",age=29))
print("\nMy name is {n[name]} and i'm {n[age]} years old!".format(n=nameDict))
print("\nValue is {v[0]} and {v[2]} ".format(v=values))

#Numbers and Float:
print("\n Formatting Number and Float ")
print("{:d}".format(1234))
print("{:10d}".format(1234))#padding 10
print("{:010d}".format(1234))#padding 10 with 0
print("{:f}".format(1.234565464564))
print("{:.1f}".format(1.234565464564))#two float value

print("\nPadding >> ");
print('Left: {:10}'.format("python")) #Padding Characters: align left 
print('Right: {:>10}'.format("python")) #Padding Characters: align right
print('Center: {:*^10}'.format("python"))
print('Left with _ : {:_<10}'.format("python"))
print('Center with _ : {:_^10}'.format("AM"))

print("\nTruncating >> ");
print('Only first 5 chars : {:.5}'.format("Programming With Python"))
print('padding : {:_^10.5}'.format("Programming With Python"))

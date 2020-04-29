# coding=utf-8
"""
Meaning	        Math Symbol	    Python Symbols
Less than     	        <	            <
Greater than	        >	            >
Less than or equal	    ≤	            <=
Greater than or equal	≥	            >=
Equals	                =	            ==
Not equal	            ≠	            !=
"""


print('2 < 5 ?')
print(2 < 5)
print('3 > 7 ?')
print(3 > 7)
x = 11
print('x = 10')
print('x > 10 ?')
print(x > 10)
print('x == 11 ?')
print(x == 11)
print('x != 11 ?')
print(x != 11)
print('2 * x < x ?')
print(2 * x < x)
print('What type is True?')
print(type(True))
print("'hi' == 'h' + 'i' ?")
print('hi' == 'h' + 'i')
print("'HI' != 'hi'?")
print('HI' != 'hi')
print('[1, 2] != [2, 1]?')
print([1, 2] != [2, 1])
print("'a' > 5 ?")
print('a' > 5)
#print("'a' = " + str(ord('a')))
print('\n')

weight = float(input("How many pounds does your suitcase weigh? "))
if weight > 50:
   print("\nThere is a $25 charge for luggage that heavy.")
print("\nThank you for your business.")
print('\n')

'''
The general Python syntax for a simple if statement is
	if condition :
		indentedStatementBlock

If the condition is true, then do the indented statements. If the condition is not
true, then skip the indented statements.
'''

temperature = float(input('What is the temperature? '))
if temperature > 70:
    print('\nWear shorts.')
else:
    print('\nWear long pants.')
print('Get some exercise outside.')

'''
The general Python if-else syntax is

if condition :
    indentedStatementBlockForTrueCondition
else:
    indentedStatementBlockForFalseCondition

These statement blocks can have any number of statements, and can include about any kind of statement.
'''

vals = ['this', 'is', 'it']
print("\nvals = ['this', 'is', 'it']")
print("Is 'is' in vals?")
print('is' in vals)
print("Is 'was' in vals")
print('was' in vals)
print("Is 'is' not in vals?")
print('is' not in vals)
print("Is 'was' not in vals")
print('was' not in vals)

'''
def letterGrade(score):
    if score >= 90:
        letter = 'A'
    else:   # grade must be B, C, D or F
        if score >= 80:
            letter = 'B'
        else:  # grade must be C, D or F
            if score >= 70:
                letter = 'C'
            else:    # grade must D or F
                if score >= 60:
                    letter = 'D'
                else:
                    letter = 'F'
    return letter

This repeatedly increasing indentation with an if statement as the else block can be annoying and distracting. 
A preferred alternative in this situation, that avoids all this indentation, 
is to combine each else and if block into an elif block:
'''

def letterGrade(score):
    if score >= 90:
        letter = 'A'
    elif score >= 80:
        letter = 'B'
    elif score >= 70:
        letter = 'C'
    elif score >= 60:
        letter = 'D'
    else:
        letter = 'F'
    return letter

"""
The most elaborate syntax for an if-elif-else statement is indicated in general below:

if condition1 :
    indentedStatementBlockForTrueCondition1
elif condition2 :
    indentedStatementBlockForFirstTrueCondition2
elif condition3 :
    indentedStatementBlockForFirstTrueCondition3
elif condition4 :
    indentedStatementBlockForFirstTrueCondition4
else:
    indentedStatementBlockForEachConditionFalse

The if, each elif, and the final else lines are all aligned. 
There can be any number of elif lines, each followed by an indented block. (Three happen to be illustrated above.) 
With this construction exactly one of the indented blocks is executed. 
It is the one corresponding to the first True condition, or, if all conditions are False, 
it is the block after the final else line.

Pro tip: a lot of elif conditions will force the code to possibly parse/evaluate all the statements wasting precious time
for time sensitive scripts. Use a switch-case function to optimize your code. 
https://jaxenter.com/implement-switch-case-statement-python-138315.html
"""
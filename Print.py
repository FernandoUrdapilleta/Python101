# object(s)	        Any object, and as many as you like. Will be converted to string before printed
# sep='separator'	Optional. Specify how to separate the objects, if there is more than one. Default is ' '
# end='end'	        Optional. Specify what to print at the end. Default is '\n' (line feed)
# file	            Optional. An object with a write method. Default is sys.stdout

# end
print("hello", end =" ")
print("world")
print("------------------------------------------------------------------------------------ Line 9")

# file
sample = open('samplefile.txt', 'w')
print('Hello World', file=sample)
sample.close()

# Print two messages, and specify the separator:

print("Hello", "how are you?", sep="---")
print("------------------------------------------------------------------------------------ Line 19")

# You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
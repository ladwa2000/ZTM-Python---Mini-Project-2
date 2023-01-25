#Built-In Functions and Methods

quote = 'When we are at our lowest point, we are open to the greatest change'

print(len(quote)) #Will print length of 'quote', i.e. 67 characters
print(quote[12:len(quote)].capitalize()) #Will capitalize and print 'quote' from the 12th index 
print(quote.upper()) #Will print 'quote' in all uppercase
print(quote.lower()) #Will print 'quote' in all lowercase
print(quote.find('o')) #Will find the index of the first appearance of 'o' in 'quote'
print(quote.replace('we are', 'we\'re')) #Will replace the string 'we are' in 'quote' to 'we're'

#Booleans

email = 'ladwa2000@gmail.com'

email = True
print(bool(email)) #True

email = False
print(bool(email)) #False

print(int(bool(True))) #True = 1
print(int(bool(False))) #False = 0

print(bool(1)) #True
print(bool(0)) #False

#NB: Booleans are either 'True' or 'False'
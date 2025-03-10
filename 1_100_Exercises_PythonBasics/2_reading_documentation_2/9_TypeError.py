'''The following code raises a TypeError:

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)
What does a TypeError indicate? Try running the above code, then use the resulting error message to determine exactly what is wrong. (You don't have to fix this code '''

# TypeError = when an operation or function is applied to an object of the wrong type
# in this case, can only concatenate str (not "int") to str, 
# correct code in last line len(tweet) + 5

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet) + 5

print (len(tweet))
print (length_of_tweet)

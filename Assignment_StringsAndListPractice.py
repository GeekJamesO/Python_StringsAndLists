"""
Find and Replace
In this string: words = "It's thanksgiving day. It's my birthday,too!"
print the position of the first instance of the word "day". Then create a
new string where the word "day" is replaced with the word "month".
"""
words = "It's thanksgiving day.  It's my birthday,too!"
querystr = "day"
month = "month"
index = words.find(querystr);
print 'Find and Replace:'
print 'Position of the first instance of the word "day" is %d' % index
newString = words.replace (querystr, month, 1)
print newString
print " "

"""
Min and Max
Print the min and max values in a list like this one: x = [2,54,-2,7,12,98].
Your code should work for any list.
"""
def MinAndMax(arr):
    print 'Min and Max'
    print 'The minumum is {0} and the maxiumum is {1}'.format(min(arr), max(arr) )
    return

x = [2,54,-2,7,12,98]
MinAndMax(x)
print " "

"""
First and Last
Print the first and last values in a list like this one: x =
["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the
first and last values in the original list. Your code should work for any list.
"""
def FirstAndLast(arr):
    print 'First and Last'
    print 'The first value is "{0}" and the last value is "{1}".'.format( arr[0], arr[-1] )
    return

arr = ["hello", 2, 54, -2, 7, 12, 98, "world"]
FirstAndLast(arr)
print " "

"""
New List
Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6].
Sort your list first. Then, split your list in half. Push the list created from
the first half to position 0 of the list created from the second half. The
output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98].
Stick with it, this one is tough!
"""
def NewListSplitAndJoin(aList):
    print 'New List'
    aList.sort()
    middleIndex = len(aList)  / 2
    top = aList[ : middleIndex]
    bottom = aList[middleIndex : ]
    newList = [ top ] + bottom
    print newList
    return;

x = [19,2,54,-2,7,12,98,32,10,-3,6]
NewListSplitAndJoin(x)

'''
Find and Replace
In this string: words = "It's thanksgiving day. It's my birthday,too!"
print the position of the first instance of the word "day".
Then create a new string where the word "day" is replaced with the word "month".
'''
words = "It's thanksgiving day. It's my birthday,too!"
print "Index of the first word 'day' is: {}".format(words.find("day"))
print words.replace("day", "month")

'''
Min and Max
Print the min and max values in a list like this one: x = [2,54,-2,7,12,98].
Your code should work for any list.
'''
def PrintMinAndMax(arr):
    if arr == None:
        print "There is no Min or Max for an empty set."
        return
    min = arr[0]
    max = arr[0]
    for k in arr:
        if min > k:
            min = k
        if max < k:
            max = k
    print "For array: {}".format(arr)
    print "Min = {} and max = {}".format(min, max)
x = [2,54,-2,7,12,98]
PrintMinAndMax(x)

'''
First and Last
Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"].
Now create a new list containing only the first and last values in the original list.
Your code should work for any list.
'''
def FirstAndList(arr):
    if arr == None:
        print "There is no first or last for an empty set."
        return
    first = arr[0]
    last = arr[len(arr)-1]
    print "First value is '[]', Last Value is '{}' ."
    newList = [first, last]
    print "New list is: '{}'.".format(newList)
x = ["hello",2,54,-2,7,12,98,"world"]
FirstAndList(x)

'''
New List
Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6].
Sort your list first. Then, split your list in half.
Push the list created from the first half to position 0 of the
list created from the second half.
The output should be:
[[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!
'''

def FoldListIntoSelf(arr):
    print "Input Array:", arr
    arr.sort()
    arrLen = len(arr)
    middle = len(arr) / 2
    front = arr[0 : middle]
    back = arr[middle : arrLen ]
    back.insert(0, front)
    print "Expected output: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]"
    print "  actual output:", back

InArray = [19,2,54,-2,7,12,98,32,10,-3,6]
FoldListIntoSelf(InArray)

def word_count(para):
    counts = {}
    words = para.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count(input("~enter your para to know no of each word")))


from re import I

introstring  = input("~enter your para if you want to count total no of word")
print (introstring)
characterCount =0
wordcount = 1
for character in introstring :
    characterCount+=1
    if (character== " "):
        wordcount=wordcount+1

print(characterCount-(wordcount-1))
print (wordcount)


def stutter(word):
    sep = "..."
    first2char = word[:2]
    print(first2char,sep,first2char,sep,word)
    
word = input( "Enter Word ")
stutter(word)

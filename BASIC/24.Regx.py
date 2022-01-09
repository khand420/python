        #    --------------Regular Expression----------


# * Regx are symbols representing text Pattern
# * Used for matching, Searching & Replacing Text
# * Formal Languages are interpreted by a regex expression proceesor 
# * Used by Programming Languages 


# --------APPLICATIONS---------

# * Testing email address format
# * Testing Credit Card Numbers whether it has valid number of digits
# * Searching a document for two spelling of a word "center" or "centre".
# * Replacing all occurences "I", "He" or "monu" with Mr.Monesh
# * Count the frequency of "training" is preceded by "Dance", "Youtube" etc.
# * Extrat data from a PDF invoice
# * "1(234)567-890"



# -----Regular Expression Marches with-----

# *matches
# *Text if it correctly describes the text.
# *Text matches a regular expression if it is correctly describe by the expression




# Extract Numbers from TextString Using Regex

sentence= "I am 89 years old. My father name is 120.3"
num = []

for words in sentence.split():
        # if words.isdigit():        #help when number is in intiger
        if not words.isalpha():      #help when number is in float
                num.append(words)
# print(num)    


# for proper way to find number we use reg
import re

digit=re.findall('\d*\.?\d+',sentence)
print(digit)
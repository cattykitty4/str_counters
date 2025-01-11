# What is str_counters?
This is three python code files which allows to count occurences and shows the most less words or letters in alphabetical order.  

# What is counting_occurences?
This programm creates list and finds indices of previous occurrences in words. For all first occurrences it sets default value -1.  
This might be helpful in searching unique wors in text.  
Programm awaits that input in def will be have sting type of data.  

# Example
Input: One Ring to rule them all One Ring to find them One Ring to bring them all and in the darkness bind them  
Output: -1, -1, -1, -1, -1, -1, 0, 1, 2, -1, 4, 6, 7, 8, -1, 10, 5, -1, -1, -1, -1, -1, 15  

# What is less_in_alphabetical_order?
This programm finds words which is apppear the most frquently in string. If multiple words have the same maximum number of occurrences, the program returns the first word in alphabetical order among those words.  
Programm awaits that input in def will be have sting type of data.  

# Example
Input: apple banana apple orange banana apple  
Output: apple  

# Example 2
Input: apple banana orange banana orange  
Output: banana  

# What is previous_occurence?
This programm returns amount of previous occurences in every word.  
Programm awaits that input in def will be have sting type of data.  

# Example
Input: apple banana apple orange banana  
Output: 0 0 1 0 1  

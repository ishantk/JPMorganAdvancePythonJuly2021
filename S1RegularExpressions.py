# Regular Expressions
# Flexible Pattern Matching

# PEP Standard -> https://pep8.org/

import re
regex = re.compile("\s+")
quote = "search the candle rather than cursing the darkness"
print(regex.split(quote))

data = ["        ", "john  ", "  jennie"]
for value in data:
    if regex.match(value):
        print(value, "matches")
    else:
        print(value, "does not matches")

regex = re.compile("the")
data = regex.search(quote)
print(data, type(data))
print(data.start())

# new_quote = quote.replace('the', 'a')
new_quote = regex.sub('a', quote)
print(new_quote)

# new_quote = re.sub("the", "a", quote)
# print(quote)
# print(new_quote)

# johne@example.com
email_reg_ex = re.compile('\w+@\w+\.[a-z]{3}')
message = "Hello, This is an email sent from john@example.com to the participants jennie@example.com and joe@abc.org"
results = email_reg_ex.findall(message)
print(results, type(results))

resultant_message = email_reg_ex.sub("xx@xx.xxx", message)
print(resultant_message)

message = "This is a very good day. is it going to rain ?"
regex = re.compile("is")
results = regex.findall(message)
print(results)

message = "Please Pay $50"
regex = re.compile(r'\$')
result = regex.findall(message)
print(result)

message = "john is 10 years old"
regex = re.compile(r"\w\s\w")
results = regex.findall(message)
print(results)

regex = re.compile('[aeiou]')
result = regex.split("regularexpressions")
print(result)

regex = re.compile('[A-Z][0-9]')
string = "109856, PB, A6, 44"
results = regex.findall(string)
print(results)

# Try writing a Regex -> to find vehicle number like -> PB10AL2937
message = "My Vehicle PB10AL2937 is towed away. Now i have a cab arriving with CH01BX1234 soon"
regex = re.compile(r'[A-Z]{2}\d{2}[A-Z]{2}\d{4}')
results = regex.findall(message)
print(results)

# regex = re.compile(r'\w\w\w')
regex = re.compile(r'\w{3}')
message = "This is going to be a great day"
results = regex.findall(message)
print(results)
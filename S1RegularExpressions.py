# Regular Expressions
# Flexible Pattern Matching

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
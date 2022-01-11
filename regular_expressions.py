import re


def find_amounts(string):
    money = re.compile(
        r'([£€$])?(?=(\d{1,3}(?:,\d{3})*(?:\.\d+)?(?![\d.,])(?:\s*(?:[tTbB]n|m|(?:[tT]r|[bBmM])i)\b)?)(\s*(?:[pP](?:ence)?|[cC](?:ents?)?|€|[eE]uros?|[dD]?|[pP]?)\b)?)(?(1)\2(?!\3)|(?<![£€$])\2\3)')
    return [''.join(m) for m in money.findall(string)]


def find_phone_numbers(string):
    money = re.compile(
        r'[+(]*[\d]+[)]*[\s.-]*[(]*[\d]+[)]*[\s.-]*[(]*[\d]+[)]*[\s.-]*[(]*[\d]+[)]*')
    return money.findall(string)


# testing

# testing currencies
print(find_amounts("Your expression should be able to deal with different formats and "
                   "currencies, for example £50,000 and £117.3m as well as 30p, 500m euro, "
                   "338bn euros, $15bn and $92.88. Make sure that you can at least detect "
                   "amounts in Pounds, Dollars and Euros. "))

# testing phone numbers
print(find_phone_numbers("Phone number : 555.123.4565"
                         "My Phone number is : +1-(800)-545-2468"
                         "Phone number : (243)-234-2342"
                         "Phone number : 3-800-545-2468"
                         "Phone number : 555 222 3342"
                         "Phone number : 12345678900"))

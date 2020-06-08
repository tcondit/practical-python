# extracting_individual_characters_and_substrings.md

## Exercise 1.13

```
>>> symbols = 'AAPL,IBM,MSFT,YHOO,SCO'
>>> symbols[0]
'A'
>>> symbols[1]
'A'
>>> symbols[2]
'P'
>>> symbols[-1]
'O'
>>> symbols[-2]
'C'

>>> symbols[0] = 'F'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

## Exercise 1.14

```
>>> symbols = symbols + 'GOOG'
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCOGOOG'

>>> symbols[:-4]
'AAPL,IBM,MSFT,YHOO,SCO'

>>> symbols = symbols[:-4] + ',GOOG'
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCO,GOOG'

>>> symbols = 'HPQ,' + symbols
>>> symbols
'HPQ,AAPL,IBM,MSFT,YHOO,SCO,GOOG'
```

## Exercise 1.15

```
>>> symbols
'HPQ,AAPL,IBM,MSFT,YHOO,GOOG'
>>> 'IBM' in symbols
True
>>> 'AA' in symbols
True
>>> 'CAT' in symbols
False
```

* `AA`: `symbols` is a single string. All membership testing is on the whole string. It's the same reason that `'T,Y' in symbols` returns True.

## Exercise 1.16

```
>>> symbols.lower()
'hpq,aapl,ibm,msft,yhoo,goog'
>>> symbols
'HPQ,AAPL,IBM,MSFT,YHOO,GOOG'

>>> lowersyms = symbols.lower()

>>> symbols.find('MSFT')
13

>>> symbols[13:17]
'MSFT'

>>> symbols = symbols.replace('SCO','DOA')
>>> symbols
'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'

>>> name = '   IBM   \n'
>>> name = name.strip()
>>> name
'IBM'
```

## Exercise 1.17

```
>>> name
'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{shares} of {name} at ${price:0.2f}'
'100 of IBM at $91.10'
```

## Exercise 1.18

```
>>> text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'
>>> import re
>>> re.findall(r'\d+/\d+/\d+', text)
['3/27/2018', '3/28/2018']

>>> re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
'Today is 2018-3-27. Tomorrow is 2018-3-28.'
```


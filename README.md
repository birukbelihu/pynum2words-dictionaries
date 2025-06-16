# pynum2words-language-packs

Language Packs For [pynum2words](https://github.com/BirukBelihu/pynum2words) Python Library

# How To Create A Language Dictionary

Creating a language dictionary for `pynum2words` python library very easy. all you need to do is to create a dedicated text file with .n2w extension and define the basic number that subsequent numbers will be derived from it. here is an example of a language dictionary for the English language:

```text
# English Language Dictionary

0 = Zero
1 = One
2 = Two
3 = Three
4 = Four
5 = Five
6 = Six
7 = Seven
8 = Eight
9 = Nine
10 = Ten
11 = Eleven
12 = Twelve
13 = Thirteen
14 = Fourteen
15 = Fifteen
16 = Sixteen
17 = Seventeen
18 = Eighteen
19 = Nineteen
20 = Twenty
30 = Thirty
40 = Forty
50 = Fifty
60 = Sixty
70 = Seventy
80 = Eighty
90 = Ninety
100 = Hundred
1000 = Thousand
1000000 = Million
1000000000 = Billion
```

```pynum2words``` Library also supports comments in the dictionary file, so you can add comments to explain the numbers or any other information you want like this.

```text

# Here I define the basic numbers in Amharic language from 1 to 10
1 = አንድ
2 = ሁለት
3 = ሶስት
4 = አራት
5 = አምስት
6 = ስድስት
7 = ሰባት
8 = ስምንት
9 = ዘጠኝ
10 = አስር
```

```text
Supported Comments ``#, //, /* */``
```

The ```pynum2words``` library will also show errors & warnings if there are any issues with the dictionary file. For example, if your definition have a syntax error, it will show a warning like this:

```text
0 = Zero
1One # Invalid pyum2words dictionary entry, it should be like this: 1 = One
2 = Two
3 = Three
```

```text
Line 2 Invalid Format: 1One — expected 'number = word'
```



Consider Supporting pynum2words Library By Providing A Language Dictionary For Your Language.

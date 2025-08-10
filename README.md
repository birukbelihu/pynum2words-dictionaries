# pynum2words-dictionaries

Language Dictionaries For [pynum2words](https://github.com/BirukBelihu/pynum2words) Python Library

# How To Create a Language Dictionary

Creating a language dictionary for `pynum2words` python library is very easy. All you have to do is to create a dedicated text file with .n2w extension and define the basic number that subsequent numbers will be derived from it. here is an example of a language dictionary for the English language:

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

# Here is Amharic language dictionary for pynum2words from 0 to 10
0 = ዜሮ
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
Invalid format at line 2: '1One' — expected 'number = word'
```

Once you've done creating your language dictionary, you can test it using the `pyn2wc` script. This script will help you to check if your dictionary is valid and can be used with the `pynum2words` library.

# How To Use The Language Dictionary

To use the language dictionary you created, you need to save it with a `.n2w` extension and place it in the current or any other directory you want(Note that you should use the absolute path if it's in another folder). After that, you can use it in your Python code like this:

```python
from pynum2words.pynum2words import PyNum2Words

amharic_converter = PyNum2Words("amharic.n2w")

# Number to words

print(amharic_converter.number_to_words(1995))  # Output: አንድ ሺህ ዘጠኝ መቶ ዘጠና አምስት
# Words to number

print(amharic_converter.words_to_number("ሁለት ሺህ አምስት"))  # Output: 2005
```
# How To Contribute
First of all thank you so much for your contribution. To contribute a language dictionary, you can create a pull request with your language dictionary file. Make sure to follow the format mentioned above and test it with the `pyn2wc` tool before submitting the pull request.

1. Clone the repository
```bash
git clone https://github.com/birukbelihu/pynum2words-dictionaries
```

2. Navigate to the project directory
```bash
cd pynum2words-dictionaries
```

3. Install the required dependencies
```bash
pip install -r requirements.txt
```

4. Run the `pyn2wc` script to with your dictionary path or name(If it's in the current directory)
```bash
python pyn2wc.py dummy.n2w
```

or the folder containing the dictionary files
```bash
python pyn2wc.py dictionaries/
```

## 📢 Social Media

- 📺 [YouTube: @pythondevs](https://youtube.com/@pythondevs?si=_CZxaEBwDkQEj4je)

---

## 📄 License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.

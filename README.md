# Strong-Custom-Password-Generator
Generates passwords with custom rules, characters, lengths, and prints their hashes.

Created on Python 3.6

The default is a randomly generated 16 character password.

There are (26+26+10+30)^16 possible combinations. That is about 2.634e31 possible combinations.
NOTE: There is a little bit less than that since the program does not allow 3 characters to repeat consecutively.

After each password generation, the MD5, SHA1, SHA224, SHA256, SHA384, and, SHA512 hashes are calculated and generated as well.

To Do in the Future:

~~- Use helper functions to check all the user inputs to condense the code~~
~~- Check user supplied symbols to remove any redundant characters (repeats, letters, and numbers)~~
- Color coordinate safe and outdated hash algorithms
~~- Although unlikely but possible, create a method to prevent starvation of a certain group (upper, lower, num, or symbol) if by random, program keeps excluding a certain group~~
- Export newly generated passwords to a file
- Encrypt newly exported file and add label

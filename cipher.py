import pyperclip
 5.
 6. LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 7.
 8. def main():
 9.     # This text can be downloaded from https://www.nostarch.com/
          crackingcodes/:
10.     myMessage = """Alan Mathison Turing was a British mathematician,
          logician, cryptanalyst, and computer scientist."""
11.     myKey = 'ASIMOV'
12.     myMode = 'encrypt' # Set to either 'encrypt' or 'decrypt'.
13.
14.     if myMode == 'encrypt':
15.         translated = encryptMessage(myKey, myMessage)
16.     elif myMode == 'decrypt':
17.         translated = decryptMessage(myKey, myMessage)
18.
19.     print('%sed message:' % (myMode.title()))
20.     print(translated)
21.     pyperclip.copy(translated)
22.     print()
23.     print('The message has been copied to the clipboard.')
24.
25.
26. def encryptMessage(key, message):
27.     return translateMessage(key, message, 'encrypt')
28.
29.
30. def decryptMessage(key, message):
31.     return translateMessage(key, message, 'decrypt')
32.
33.
34. def translateMessage(key, message, mode):
35.     translated = [] # Stores the encrypted/decrypted message string.
36.
37.     keyIndex = 0
38.     key = key.upper()
39.
40.     for symbol in message: # Loop through each symbol in message.
41.         num = LETTERS.find(symbol.upper())
42.         if num != -1: # -1 means symbol.upper() was not found in LETTERS.
43.             if mode == 'encrypt':
44.                 num += LETTERS.find(key[keyIndex]) # Add if encrypting.
45.             elif mode == 'decrypt':
46.                 num -= LETTERS.find(key[keyIndex]) # Subtract if
                      decrypting.
47.
48.             num %= len(LETTERS) # Handle any wraparound.
49.
50.             # Add the encrypted/decrypted symbol to the end of translated:
51.             if symbol.isupper():
52.                 translated.append(LETTERS[num])
53.             elif symbol.islower():
54.                 translated.append(LETTERS[num].lower())
55.
56.             keyIndex += 1 # Move to the next letter in the key.
57.             if keyIndex == len(key):
58.                 keyIndex = 0
59.         else:
60.             # Append the symbol without encrypting/decrypting:
61.             translated.append(symbol)
62.
63.     return ''.join(translated)

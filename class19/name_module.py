def vowel_or_not(word):
       vowels = 'aeiou'
       for w in word:
          if w in vowels:
               print(f'{w} is a vowel')
          else:
               print(f'{w} is not a vowel')
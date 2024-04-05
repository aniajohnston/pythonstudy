import re

'''
You are testing a string to a while loop. The string must pass the following tests or the user must start over, be sure to tell the user the error.

1. String must be at least 10 characters
2. String must contain at least 1 number
3. String must contain at least 1 capital letter
4. String must contain '@' symbol
5. String must contain no spaces

Test data
jdefwkwf - not enough characters
sdnesleuex - at least 10 characters but no number
sdksdjsdf0 - at least 10 characters, contains number, no caps
Sdksdjsdf0 - at least 10 characters, contains number, has caps, no @ symbol
Sd@sdjs df0 - at least 10 characters, contains number, has caps, @ symbol, contains a space
Sd@sdjsdf0 - should pass all tests
'''
user_input, re_prompt_user = '','' #initialization

while True:
    user_input = input("Please enter your string ")

    # Not enough characters
    if len(user_input) >= 10:
        print(f'Test Passed: {user_input} is greater than 10 characters')
    else:
        print(f'Test Failed: {user_input} is less than 10 characters')
        continue
    # Contain at least 1 number
    contains_num = re.search(f'\d', user_input)
    
    if contains_num:
        print(f'Test Passed: {user_input} contains a number') #searches whole string and '\d' checks for digits in the string, then seperated by comma is the variable that it tests for
    else:
        print(f'Test Failed: {user_input} does not contain a number')
        continue
    # Contains at least 1 capital letter
    any_uppercase = any(u.isupper() for u in user_input)
    if any_uppercase:
        print(f'Test Passed: {user_input} contains a capital letter')
    else:
        print(f'Test Failed: {user_input} does not contain a capital letter')
        continue
    
    # Contains '@' symbol
    if '@' in user_input:
        print(f'Test Passed: {user_input} contains an @')
    else:
        print(f'Test Failed: {user_input} does not contain an @')
        continue

    # Contains no spaces
    has_space = re.search(r'\s', user_input)
    
    if not has_space:
         print(f'Test Passed: {user_input} contains no spaces')
    else:
        print(f'Test Failed: {user_input} contains a space')
       
    re_prompt_user = input('Congrats on signing up, please login.')

    if user_input == re_prompt_user:
        print("Congrats on logging in")
        break
    else:
        print("Please start over.")
        continue
    
       
  

    
    
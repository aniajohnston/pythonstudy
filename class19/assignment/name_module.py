first_name = 'Ania'
last_name = 'Johnston'

def full_name(first,last):
    return first + ' ' + last

def reverse_name(first,last):
    return last + ' ' + first

def get_initials(first,last):
    return f'{first[0]}.{last[0]}.'
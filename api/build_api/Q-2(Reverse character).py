'''Reverse characters in words in a sentence'''


def reverse_character(p_str):
    
    rev_list = [i[::-1] for i in p_str] #reversed characters of each words in the array
    
    rev_string = " ".join(map(str,rev_list)) #coverted array back to string
    return rev_string
    


n_str = 'My name is Vikash Kumar'
rev_str = reverse_character(n_str.split(' ')) # passing string as an list
print('Original Character : {}'.format(n_str))
print('Reversed String : {}'.format(rev_str))

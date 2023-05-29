
big_num = 1120395495
this_is_a_tuple = 1,120,395,495
type(this_is_a_tuple)
easy_to_read = 1_120_395_495
placement_doesnt_matter = 11_20_39_54_95
big_num == easy_to_read == placement_doesnt_matter

# Some fun with strings
some_num = 1234.12555
'{0:,.3f}'.format(1234.12555)
f'{some_num:.3f}'

some_dec = .12555
'{0:.3%}'.format(some_dec)
f'{some_dec:.3%}'

address = '123 Main St, Buffalo NY 14221'
# Don't do this
print(f'address={address}')

# Do this instead
print(f'{address=}')

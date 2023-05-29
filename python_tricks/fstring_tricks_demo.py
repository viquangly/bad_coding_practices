
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

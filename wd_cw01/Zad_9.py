z_string = 'tekst'
z_float = 243
z_hexdec = hex(255)

print('string: %(zm)s' % {'zm': z_string})
print('float: %(zm)f' % {'zm': z_float})
print('szestnastkowe: %(zm)s' % {'zm': z_hexdec})
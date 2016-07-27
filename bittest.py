s3 = ['0' for i in range(8)] 


s3[0] = '1'
s3[1] = '0'
s3[2] = '1'
s3[3] = '1'
s3[4] = '0'
s3[5] = '0'
s3[6] = '0'
s3[7] = '0'

#print ''.join(list(reversed(s3)))

bits = '11011110'
print format(int(bits, 2), '02x')

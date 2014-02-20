# comments are preceded by hash
print '\n'
print '### hash character in string literal does NOT start a comment\n'

print '3.1.1 Numbers'
print '-------------'
print 'Integer division returns the floor'
print '+7/3 =', +7/3 # == 2
print '-7/3 =', -7/3 # == -3
print '' # newline

print 'Complex arithmetic supported using "j" or complex(real, imag)'
print '1j * 1J=', 1j * 1J # == (-1 + 0j)
print '1j * complex(0,1)=', 1j * complex(0,1) # == (-1 + 0j)
print ''
print 'Use .real .imag and abs() as needed. For z = (3 + 4j)...'
z = 3 + 4j
print 'z.real =', z.real # 3.0
print 'z.imag =', z.imag # 4.0
print 'abs(z) =', abs(z) # 5.0
print ''

print 'In INTERACTIVE MODE, "_" is a special variable for the last printed expression.'
print 'Treat it as read-only! Assigning a value to it will mask the magic built-in variable'
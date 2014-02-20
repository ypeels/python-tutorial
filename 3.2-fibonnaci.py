# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1 								# note multiple assignment 
while b < 10:								# nonzero values OR SEQUENCES are true. Comparison operators same as C (including !=)
    print b	
    a, b = b, a+b							# note non-trivial whitespace to demarcate blocks, instead of curly braces

print "\nand loop 2"    
while b < 100:								
  print b,                                  # trailing comma suppresses newline after output! but still inserts ' '						
  a, b = b, a+b							    # whitespace must be IDENTICAL for the entire block, including tab vs space!!
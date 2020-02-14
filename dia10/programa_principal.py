from soma import soma
import sys

a, b = [ int(i) for i in sys.argv[1:3] ]

print("Vou calcular a média agora...")
print( soma(a, b) )
print("Executei no programa principal")

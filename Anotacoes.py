"""

OPERADORES RELACIONAIS

== - É igual?
>  - É maior que?
>= - É maior ou igual a?
<  - É meno que?
<= - É menor que ou igual a? 
!= - É diferente?


A = 10
B = 20

oprel1 = A == B
oprel2 = A != B
oprel3 = A > B
oprel4 = A < B
oprel5 = A >= B
oprel6 = A <= B

print(oprel1)  # false
print(oprel2)  # true
print(oprel3)  # false
print(oprel4)  # true
print(oprel5)  # false
print(oprel6)  # true
-------------------------------------------------------------

OPERADORES LÓGICOS

and - E - resulta em True apenas se os dois valores também forem True
or - OU - resulta em True apenas se pelo menos um dos dois valores também forem True
not - NÃO/Negação 
in - dentro, na
not in - negação de in


a = True
b = False

oplog1 = a and b
oplog2 = a or b
oplog3 = not(a and b)

print(oplog1)  # false
print(oplog2)  # true
print(oplog3)  # true

-------------------------------------------------------------

Estrutura Condicional - IF, ELIF, ELSE, TRY, EXCEPT

if - significa 'se', permite que uma parte do programa seja 
executada apenas quando uma condição for verdadeira.

else - significa 'senão', permite que uma parte do programa 
seja executada apenas quando a condição do if seja falsa.

elif - else if, no caso de haver mais de uma condição else

Obs1 - A parte do código a ser executada com a estrutura 
condicional é aquela que está subordinada


try - tentar executar uma parte do código

except - se o try não der certo

try e except são bem parecidos com if-else, porém vai ignorar o erro de um bloco e não vai apresentá-lo

-------------------------------------------------------------

pass - ignora uma parte do código sem apresentar erro

Exemplo:

valor - True

if valor:
    pass  # dá pra usar ... também

else:
    print('Tchau')

-------------------------------------------------------------

"""

print('--------------------------------------------------')

print('\nOPERADORES RELACIONAIS\n')

A = 10
B = 20

oprel1 = A == B
oprel2 = A != B
oprel3 = A > B
oprel4 = A < B
oprel5 = A >= B
oprel6 = A <= B

print('A = 10')
print('B = 20')

print('')

print('oprel1 = A == B = ', oprel1)  # false
print('oprel2 = A != B = ', oprel2)  # true
print('oprel3 = A > B = ', oprel3)  # false
print('oprel4 = A < B = ', oprel4)  # true
print('oprel5 = A >= B = ', oprel5)  # false
print('oprel6 = A <= B = ', oprel6)  # true

print('')

print('--------------------------------------------------')

print('\nOPERADORES LÓGICOS\n')

a = True
b = False

oplog1 = a and b
oplog2 = a or b
oplog3 = not(a and b)

print('a = True')
print('b = False')

print('')

print('oplog1 = a and b =', oplog1)  # false
print('oplog2 = a or b =', oplog2)  # true
print('oplog3 = not(a and b) =', oplog3)  # true

print('')

print('--------------------------------------------------')
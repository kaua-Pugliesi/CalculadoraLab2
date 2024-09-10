num = float(input("Insira um número: "))
aux = num
operation = input("Digite o tipo de operação(+,-,*,/ ou '=' para finalizar): ")

while operation != "=":
    numprox = float(input("Insira um número"))
    
    if operation == "+":
        aux = aux + numprox
        
    if operation == "-":
        aux = aux - numprox
  
    if operation == "*":
        aux = aux * numprox
        
    if operation == "/":
        if numprox != 0:
            aux = aux / numprox
        else:
            print("nenhum numero pode ser dividido por 0!")
    print("operação atual = ", aux)
    operation = input("Digite o tipo de operação(+,-,*,/ ou '=' para finalizar): ")

    
print("resultado: ", aux)

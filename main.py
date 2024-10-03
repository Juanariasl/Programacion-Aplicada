import clase
import random

# Función que realiza un cálculo aleatorio
def calculo_aleatorio():
    operaciones = ["square", "add", "sub"]
    operacion = random.choice(operaciones)

    if operacion == "square":
        valor = random.randint(1, 10)  # Número aleatorio entre 1 y 10
        objeto_cuadrado = clase.Square(valor)
        print(f"Operación: Cuadrado de {valor}")
        print(f"Resultado: {objeto_cuadrado.getVal()}")
    
    elif operacion == "add":
        a, b = random.randint(1, 10), random.randint(1, 10)
        objeto_add_sub = clase.Add_Sub()
        print(f"Operación: Suma de {a} + {b}")
        print(f"Resultado: {objeto_add_sub.add(a, b)}")
    
    elif operacion == "sub":
        a, b = random.randint(1, 10), random.randint(1, 10)
        objeto_add_sub = clase.Add_Sub()
        print(f"Operación: Resta de {a} - {b}")
        print(f"Resultado: {objeto_add_sub.sub(a, b)}")

# Ejecutando el cálculo aleatorio
if __name__ == "__main__":
    calculo_aleatorio()

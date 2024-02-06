def fibonacci(n):
    """Berechnet die Fibonacci-Folge bis zur n-ten Zahl."""
    fib_sequence = [0, 1]  # Die ersten beiden Fibonacci-Zahlen
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]  # Die nächste Fibonacci-Zahl berechnen
        fib_sequence.append(next_fib)  # Die nächste Fibonacci-Zahl zur Liste hinzufügen
    return fib_sequence

# Beispielaufruf des Skripts
n = int(input("Geben Sie die Anzahl der Fibonacci-Zahlen ein, die Sie berechnen möchten: "))
fib_numbers = fibonacci(n)
print("Die Fibonacci-Folge bis zur", n, "-ten Zahl lautet:", fib_numbers)
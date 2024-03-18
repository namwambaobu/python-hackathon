def generate_fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        next_term = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_term)
    return fib_seq[:n]

def main():
    try:
        n = int(input("Enter the number of terms for Fibonacci sequence: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        fib_seq = generate_fibonacci(n)
        print("Fibonacci sequence up to term", n, ":", fib_seq)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()

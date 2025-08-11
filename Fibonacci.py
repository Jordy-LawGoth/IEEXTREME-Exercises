import sys

def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    ms = list(map(int, data[1:]))

    # Precomputar F_k % 10 para k = 0..60 (incluido)
    fib_mod10 = [0] * 61
    fib_mod10[0] = 0
    fib_mod10[1] = 1
    for i in range(2, 61):
        fib_mod10[i] = (fib_mod10[i-1] + fib_mod10[i-2]) % 10

    out_lines = []
    for m in ms:
        k = (m + 1) % 60
        if k == 0:
            k = 60
        # G_m = F_{m+1} --> resultado es F_k % 10
        out_lines.append(str(fib_mod10[k]))

    sys.stdout.write("\n".join(out_lines) + "\n")

if __name__ == "__main__":
    main()
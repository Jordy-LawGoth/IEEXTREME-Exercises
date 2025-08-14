import sys

# Leer todas las líneas
lines = sys.stdin.read().strip().split("\n")

topic_index = {}
topic_count = 0
books = []

# Procesar cada libro
for line in lines:
    parts = line.split()
    time = int(parts[0])
    topics = parts[1:]
    
    mask = 0
    for topic in topics:
        if topic not in topic_index:
            topic_index[topic] = topic_count
            topic_count += 1
        mask |= (1 << topic_index[topic])
    
    books.append((time, mask))

# DP: tiempo mínimo para cada conjunto de temas
INF = 10**12
dp = [INF] * (1 << topic_count)
dp[0] = 0

# Iterar sobre libros
for time, mask in books:
    for state in range((1 << topic_count) - 1, -1, -1):
        new_state = state | mask
        dp[new_state] = min(dp[new_state], dp[state] + time)

# Salida: todos los temas cubiertos
print(dp[(1 << topic_count) - 1])

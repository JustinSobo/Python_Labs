def avg_val(n):
    z = 0
    for y in n:
        z = z + y
    avg = z / len(n)
    return avg

print("The average is", avg_val([19, 2, 20, 1, 0, 18]))

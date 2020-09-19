def max_abs_val(lst):
    n = map(abs, lst)
    return max(n)
    
print(max_abs_val([-19, -3, 20, -1, 0, -25]))

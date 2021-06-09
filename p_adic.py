import math

def get_num_divisible(n, p):
    i = 1
    while n % p ** i == 0:
        i += 1
    return i - 1

def get_inv_elem(n, p):
    if n % p == 0:
        return False
    for i in range(1, p):
        if i * n % p == 1:
            return i

def get_p_adic(frac, p, prec=10):
    l = []
    index_dict = {}
    p_pow = get_num_divisible(frac[0], p) - get_num_divisible(frac[1], p)
    for i in range(p_pow, 10):
        p_pow = get_num_divisible(frac[0], p) - get_num_divisible(frac[1], p)
        if p_pow == i:
            if p_pow > 0:
                beta = [int(frac[0] / p ** p_pow), frac[1]]
            elif p_pow < 0:
                beta = [frac[0], int(frac[1] / p ** (- p_pow))]
            else:
                beta = frac
            x = get_inv_elem(beta[1], p)
            a = beta[0] * x % p
            l.append(a)
            index_dict[i] = a
            frac = [(beta[0] - a * frac[1]) * p ** p_pow, frac[1]]
        else:
            l.append(0)
            index_dict[i] = 0
    return l, index_dict

def convert_to_formula(index_dict, p):
    f = ''
    for k, v in index_dict.items():
        if v > 1:
            f += str(v) + '*' + str(p) + '^' + str(k) + ' + '
        elif v == 1:
            f += str(p) + '^' + str(k) + ' + '
        elif v  == 0:
            pass
    return f.strip(' + ')

if __name__ == '__main__':
    p = 3
    prec = 10
    p_adic, index_dict = get_p_adic([2, 5], p, prec)
    f = convert_to_formula(index_dict, p)
    print(f)

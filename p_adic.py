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
    if frac[1] == 0:
        return False
    index_dict = {}
    p_pow = get_num_divisible(frac[0], p) - get_num_divisible(frac[1], p)
    i = p_pow
    while i < prec:
        if frac[0] == 0:
            index_dict[i] = 0
            i += 1
            continue
        p_pow = get_num_divisible(frac[0], p) - get_num_divisible(frac[1], p)
        if p_pow == i:
            if p_pow > 0:
                beta = [int(frac[0] / p ** p_pow), frac[1]]
            elif p_pow < 0:
                beta = [frac[0], int(frac[1] / p ** - p_pow)]
            else:
                beta = frac
            x = get_inv_elem(beta[1], p)
            a = beta[0] * x % p
            index_dict[i] = a
            frac = [int((beta[0] - a * beta[1]) * p ** p_pow), beta[1]]
        else:
            index_dict[i] = 0
        i += 1
    return index_dict

def convert_to_formula(index_dict, p):
    if not index_dict:
        return False
    f = ''
    for k, v in index_dict.items():
        if v > 1:
            f += str(v) + '*' + str(p) + '^' + str(k) + ' + '
        elif v == 1:
            f += str(p) + '^' + str(k) + ' + '
        elif v  == 0:
            pass
    f += f'O({p}^{list(index_dict.keys())[-1] + 1})'
    return f

if __name__ == '__main__':
    p = 5
    prec = 100
    frac = [6369051672525773, 4503599627370496]
    index_dict = get_p_adic(frac, p, prec)
    f = convert_to_formula(index_dict, p)
    print('p = {}, alpha = {}/{} のp進展開:\n  {}'.format(p, frac[0], frac[1], f))

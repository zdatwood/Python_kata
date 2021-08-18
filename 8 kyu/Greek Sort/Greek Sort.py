#my solution

def greek_comparator(lhs, rhs):
    for i in range(len(greek_alphabet)):
        if greek_alphabet[i] == lhs:
            x = i
        if greek_alphabet[i] == rhs:
            y = i
    # the tuple greek_alphabet is defined in the global namespace
    return (x - y)


greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu',
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')


print(greek_comparator('alpha', 'beta'))
print(greek_comparator('psi', 'psi'))
print(greek_comparator('upsilon', 'rho'))

"""
best solution according to the website

def greek_comparator(lhs, rhs):
    return greek_alphabet.index(lhs) - greek_alphabet.index(rhs)
    
I did not know about the .index operator for list objects. Now I do.
"""
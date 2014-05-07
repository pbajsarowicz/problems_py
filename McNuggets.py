
'''McNuggets(n):
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
'''

def McNuggets(n):
    result = False

    if n < 6:
        return False
    if n % 6 == 0 or n % 9 == 0 or n % 20 == 0:
        return True

    if (result != True and n > 20):
        result = McNuggets(n - 20)
    if (result != True and n > 9):
        result = McNuggets(n - 9)
    if (result != True and n > 6):
        result = McNuggets(n - 6)
    return result

print McNuggets(1376)
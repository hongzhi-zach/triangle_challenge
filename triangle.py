def triangleType(a, b, c):
    if (not isinstance(a, int)) and (not isinstance(a, float)):
        print('a is NaN!')
        return None
    if (not isinstance(b, int)) and (not isinstance(b, float)):
        print('b is NaN!')
        return None
    if (not isinstance(c, int)) and (not isinstance(c, float)):
        print('c is NaN!')
        return None
    if a==b==c:
        triangle_type = 'equilateral'
    elif (a==b) or (b==c) or (c==a):
        triangle_type = 'isosceles'
    else:
        triangle_type = 'scalene'
    print('The triangle (a = ', a, ', b = ', b, ', c = ', c, ') is ', triangle_type, '.', sep ='')
    return triangle_type

# test cases
triangleType(1, 2, 3)
triangleType(1, 2, 2)
triangleType(2, 2, 2)
triangleType(1, 2.0, 3)
triangleType(1, 2.0, 2)
triangleType(2, 2.0, 2)
triangleType(None, 2, 2)
triangleType('e', 2, 2)
triangleType(2, None, 2)
triangleType(2, 'e', 2)
triangleType(2, 2, None)
triangleType(2, 2, 'e')

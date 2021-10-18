def newtons_method(x, function, function_differentiated, tol):
    x_i0 = x

    while abs(function(x_i0)) >= tol:
        x_i0 = x_i0 - function(x_i0) / function_differentiated(x_i0)
        print(x_i0)
    return x_i0
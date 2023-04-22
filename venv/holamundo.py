def persona(i):
    """
    >>> persona(1)
    'El toño'
    >>> persona(2)
    'La kimberly'
    >>> persona(3)
    'El yoni'
    """
    nombre = " "
    if i==1:
        nombre = "El toño"
    elif i==2:
        nombre = "La kimberly"
    elif i==3:
        nombre = "El yoni"
    return nombre


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
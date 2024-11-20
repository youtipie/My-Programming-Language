def i2f(intVal):
    if isinstance(intVal, int):
        return float(intVal)
    else:
        exit('ERROR: На вході {intVal}, очікувалось ціле число')


def f2i(floatVal):
    if isinstance(floatVal, float):
        return int(floatVal)
    else:
        exit(f'ERROR: На вході {floatVal}, очікувалось дійсне значенння')


def getValue(lex, tok):
    if tok == 'floatnum':
        return float(lex)
    elif tok == 'intnum':
        return int(lex)
    elif tok == 'boolval':
        return lex

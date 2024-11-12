def validate_number(valor: str, tipo: str) -> int|float|None:
    
    match tipo:
        case "int":
            if "." in valor:
                return None
            else:
                return int(valor)
        case "float":
            if "." not in valor:
                return None
            else:
                return float(valor)
        case _:
            return None
        


def validate_length(valor, min_length) -> str|None:
    if len(valor) > min_length:
        return valor
    else:
        return None
    


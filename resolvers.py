def resolve_hello(obj, info):
    return "Hello, world!"

def resolve_greeting(obj, info, name):
    return f"Hello, {name}!"

def resolve_getPerson(obj, info, id):
    return {"id": id, "name": "Iair", "age": 19}

def resolve_month_name(_, info, monthNumber):
    months = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    if 1 <= monthNumber <= 12:
        return months[monthNumber - 1]
    else:
        return "Número de mes inválido. Debe estar entre 1 y 12."

import ujson as json


# Простые типы, имеющие соответствия в стандарте json. Если передается объект другого типа, он приводится к str.
BASE_JSON_TYPES = (int, float, str, bool)

def get_item(item):
    for one in BASE_JSON_TYPES:
        if isinstance(item, one):
            return {'value': item, 'type': one.__name__}
    return {'value': str(item), 'type': type(item).__name__}

def json_vars(*args, **kwargs):
    """
    Преобразуем любые аргументы в json-объект. Каждый элемент в json-объекте сопровождается названием типа данных. Это полезно в случаях, когда тип данных не соответствует стандартным для json. Все нестандартные объекты приводятся к типу str.
    Функция не поддерживает глубокую рекурсию.
    """
    if not (len(args) + len(kwargs)):
        return None
    args = [get_item(x) for x in args]
    kwargs = {key: get_item(value) for key, value in kwargs.items()}
    result = {}
    if len(args):
        result['args'] = args
    if len(kwargs):
        result['kwargs'] = kwargs
    return json.dumps(result)

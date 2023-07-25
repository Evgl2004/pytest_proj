def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default
    :param collection: словарь
    :param key: ключ, по которому необходимо найти значение
    :param default: возвращает указанное значение, если значение по ключу не найдено
    :return:
    """
    if len(collection) == 0 or collection.get(key) == None:
        return default
    else:
        return collection.get(key)

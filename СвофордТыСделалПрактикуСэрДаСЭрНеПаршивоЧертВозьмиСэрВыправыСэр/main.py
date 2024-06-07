def calculate_phone_call_cost(duration, weekday):
    """
    Вычисляет стоимость разговора по телефону с учетом 20% скидки, предоставляемой по выходным.

    Parameters:
    duration (float): Длительность разговора в минутах.
    weekday (str): День недели, когда состоялся разговор (например, 'понедельник', 'вторник', ..., 'суббота', 'воскресенье').

    Returns:
    float: Стоимость разговора по телефону.
    """

    # Проверка валидности входных данных
    if not isinstance(duration, (int, float)) or duration <= 0:
        raise ValueError("Длительность разговора должна быть положительным числом.")
    if weekday.lower() not in ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье',
                               'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        raise ValueError("Неправильный день недели.")

    # Стоимость одной минуты разговора
    cost_per_minute = 0.5

    # Вычисление стоимости разговора с учетом скидки
    if weekday.lower() in ['суббота', 'воскресенье', 'saturday', 'sunday']:
        cost = duration * cost_per_minute * 0.8  # Скидка 20% по выходным
    else:
        cost = duration * cost_per_minute

    return cost


print(calculate_phone_call_cost(30, 'monday'))

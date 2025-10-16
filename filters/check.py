
import re

def is_valid_name(name: str) -> bool:
    
    name = name.strip()

    if not (2 <= len(name) <= 50):
        return False
    
    pattern = r"^[A-Za-zA-Яа-яЁё\s\-]+$"
    return bool(re.match(pattern,name))


def is_valid_phone(phone: str) -> bool:
    """
    Валидация номера телефона
    Поддерживает форматы: 
    +998901234567, 998901234567, 901234567
    """
    # Очищаем от пробелов и лишних символов
    phone = re.sub(r'[\s\-()]', '', phone)
    
    # Проверяем основные форматы узбекских номеров
    patterns = [
        r'^\+998\d{9}$',      # +998901234567
        r'^998\d{9}$',        # 998901234567  
        r'^90\d{7}$',         # 901234567
        r'^91\d{7}$',         # 911234567
        r'^93\d{7}$',         # 931234567
        r'^94\d{7}$',         # 941234567
        r'^95\d{7}$',         # 951234567
        r'^97\d{7}$',         # 971234567
        r'^99\d{7}$',         # 991234567
    ]
    
    return any(re.match(pattern, phone) for pattern in patterns)
def validate_integration_data(payload):
    """Проверка структуры данных перед интеграцией"""
    required_fields = ["client_id", "items", "total_price"]
    
    try:
        data = json.loads(payload)
        for field in required_fields:
            if field not in data:
                print(f"[Error] Отсутствует обязательное поле: {field}")
                return False
        return True
    except ValueError:
        return False

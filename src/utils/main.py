import json
import sqlite3
from datetime import datetime

class CertificationApp:
    """Система сертификации и тестирования программных модулей различных типов"""
    
    def __init__(self, db_path="src/database/reports_db.sqlite"):
        self.db_path = db_path
        self._setup_db()
        self.standards = {
            "1": {"type": "Игровой модуль", "std": "ГОСТ Р ИСО/МЭК 12119 (Геймдизайн)"},
            "2": {"type": "Системный драйвер", "std": "IEEE 1012 (Системная интеграция)"},
            "3": {"type": "UI Компонент", "std": "ISO 9241 (Эргономика и интерфейс)"}
        }

    def _setup_db(self):
        """Создание таблицы для реестра сертификации"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS cert_logs 
                         (id INTEGER PRIMARY KEY, module_type TEXT, 
                          standard TEXT, status TEXT, date TEXT)''')

    def start_testing(self):
        print("--- Модуль поддержки и тестирования ПМ.04 ---")
        print("Выберите тип программного модуля для сертификации:")
        for k, v in self.standards.items():
            print(f"{k}. {v['type']}")
        
        choice = input("Введите номер: ")
        if choice in self.standards:
            self.process_certification(self.standards[choice])
        else:
            print("Ошибка: Неверный выбор.")

    def process_certification(self, config):
        print(f"\n[Запуск] Тестирование модуля: {config['type']}")
        print(f"[Инфо] Применяемый стандарт: {config['std']}")
        
        # Имитация процесса тестирования по стандартам
        result = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "module_type": config['type'],
            "standard": config['std'],
            "verdict": "СООТВЕТСТВУЕТ СТАНДАРТАМ",
            "log": "Ошибок кодирования не обнаружено. Стандарты ЕСПД соблюдены."
        }
        
        self.save_to_file(result)
        self.save_to_db(result)

    def save_to_file(self, data):
        filename = f"reports/report_{datetime.now().strftime('%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"[Файл] Отчет успешно сохранен в {filename}")

    def save_to_db(self, data):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("INSERT INTO cert_logs (module_type, standard, status, date) VALUES (?,?,?,?)",
                         (data['module_type'], data['standard'], data['verdict'], data['timestamp']))
        print("[БД] Результат внесен в реестр сертификации.")

if __name__ == "__main__":
    app = CertificationApp()
    app.start_testing()

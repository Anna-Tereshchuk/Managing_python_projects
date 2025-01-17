# Загальна ціль. Викликається за замовчуванням, якщо не вказано іншу ціль.
# Виводить помилку, що потрібно вибрати конкретну ціль.
all:
	$(error please pick a target)

# Ціль для створення віртуального середовища та встановлення продакшн залежностей.
env:
	# Перевіряє, чи існує директорія `venv`. Якщо ні, створює її.
	test -d venv || virtualenv venv
	# Оновлює pip у віртуальному середовищі та встановлює залежності з requirements.txt.
	./venv/bin/python -m pip install --upgrade pip
	./venv/bin/python -m pip install -r requirements.txt

# Ціль для створення середовища розробки, яке включає залежності для продакшн і розробки.
dev-env: env
	# Встановлює залежності для розробки з requirements-dev.txt.
	./venv/bin/python -m pip install -r requirements-dev.txt

# Ціль для тестування проєкту.
test:
	# Видаляє всі файли кешу Python (.pyc) у проєкті.
	find . -name '*.pyc' -exec rm -f {} \;
	# Запускає перевірку стилю коду за допомогою flake8 у папках `nlp` і `tests`.
	./venv/bin/flake8 nlp tests
	# Запускає модульні тести за допомогою pytest з додатковими параметрами.
	./venv/bin/python -m pytest \
	    --doctest-modules \        # Тестує приклади з документації.
	    --disable-warnings \       # Приховує попередження у виводі тестів.
	    --verbose \                # Вмикає детальний вивід.
	    nlp tests                  # Тестує папки `nlp` і `tests`.

# Ціль для створення дистрибутиву пакета.
package:
	# Створює архів з вихідним кодом (source distribution) пакета.
	python setup.py sdist

# Ціль для очищення проєкту від тимчасових файлів і залишків збірки.
clean:
	# Видаляє директорії збірки та метадані пакета.
	rm -rf build dist venv nlp.egg-info

# Додаткова ціль для запуску проєкту (якщо є головний скрипт main.py).
run:
	# Запускає головний файл проєкту у віртуальному середовищі.
	./venv/bin/python main.py


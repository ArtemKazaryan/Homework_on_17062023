
# !!!!!!  ДЛЯ ЗАПУСКА ОТДЕЛЬНЫХ ЗАДАНИЙ РАСКОММЕНТИРУЙТЕ ИХ РЕШЕНИЕ  !!!!!!


# Домашняя работа на 17.06.2023.

# 1. Создайте программу Python для интернет-магазина, состоящую из двух основных классов:
# CustomerManager и ProductInventory.
# Класс CustomerManager должен отвечать за обработку операций, связанных с клиентами, таких как добавление новых клиентов,
# обновление информации о клиентах и получение данных о клиентах. Он должен иметь такие методы,
# как add_customer(), update_customer() и get_customer().
# Класс ProductInventory должен отвечать за управление запасами товаров в магазине.
# Он должен обрабатывать такие операции, как добавление продуктов, обновление информации о продукте
# и получение сведений о продукте. Он должен иметь такие методы, как add_product(), update_product() и get_product().
# Разделяя управление клиентами и запасами продуктов на отдельные классы, вы гарантируете,
# что каждый класс несет единую ответственность, делая программу более модульной и простой в обслуживании.

# Решение:
# Менеджер по работе с клиентами
# class CustomerManager:
#     customers = []
#
#     def add_customer(self, name, age, phone):
#         self.name = name
#         self.age = age
#         self.phone = phone
#         self.customer = {'Имя': self.name, 'Телефон': self.phone, 'Возраст': self.age}
#         self.customers.append(self.customer)
#         print(f'Добавлен новый покупатель: {self.name}, {self.phone}, {self.age} лет')
#
#     def update_customer(self, search_name):
#         print(f'Выполняется поиск данных о покупателей для обновления: {search_name} ...')
#         for i in range(len(self.customers)):
#             if self.customers[i]['Имя'] == search_name:
#                 print(f'Найден покупатель: {self.customers[i]}')
#                 while True:
#                     atr = input(f'Обновить: 1. Имя покупателя\n'
#                                 f'          2. Номер телефона\n'
#                                 f'          3. Возраст покупателя\n'
#                                 f'          0. Выйти из режима обновления\n'
#                                 f'                             ?  : ')
#                     if atr == '1':
#                         new_name = input(f'Введите новое имя: ')
#                         self.customers[i]['Имя'] = new_name
#                     if atr == '2':
#                         new_phone = input(f'Введите новый номер телефона, лет: ')
#                         self.customers[i]['Телефон'] = new_phone
#                     if atr == '3':
#                         new_age = input(f'Введите новый возраст, лет: ')
#                         self.customers[i]['Возраст'] = new_age
#                     if atr == '0':
#                         break
#                     print(f'Данные о покупателе обновлены!')
#
#     def get_customer(self, search_name):
#         print(f'Выполняется поиск информации о покупателе {search_name} ...')
#         print(f'Найдены покупатели:')
#         if search_name == 'all':
#             print(self.customers)
#         else:
#             for i in range(len(self.customers)):
#                 if self.customers[i]['Имя'] == search_name:
#                     print(f'{self.customers[i]}')
#
# custom_manager = CustomerManager()
# custom_manager.add_customer('Иван', '+7-956-389-13-42', '20')
# custom_manager.add_customer('Олег', '+7-961-138-44-75', '30')
# custom_manager.add_customer('Мария', '+7-974-259-75-78', '25')
# custom_manager.add_customer('Мария', '+7-932-795-71-22', '33')
# custom_manager.get_customer('Иван')
# custom_manager.get_customer('Мария')
# custom_manager.update_customer('Олег')
# custom_manager.get_customer('all')
#
#
# # Товарный запас
# class ProductInventory:
#     products = []
#
#     def add_product(self, product_name, weight, price):
#         self.product_name = product_name
#         self.weight = weight
#         self.price = price
#         self.product = {'Наименование': self.product_name, 'Вес': self.weight, 'Цена': self.price}
#         self.products.append(self.product)
#         print(f'Добавлен новый товар: {self.product_name}, {self.weight} кг, {self.price} руб.')
#
#     def update_product(self, search_name):
#         print(f'Выполняется поиск данных о товаре для обновления: {search_name} ...')
#         for i in range(len(self.products)):
#             if self.products[i]['Наименование'] == search_name:
#                 print(f'Найден товар: {self.products[i]}')
#                 while True:
#                     atr = input(f'Обновить: 1. Наименование\n'
#                                 f'          2. Вес\n'
#                                 f'          3. Цена\n'
#                                 f'          0. Выйти из режима обновления\n'
#                                 f'                             ?  : ')
#                     if atr == '1':
#                         new_product_name = input(f'Введите новое наименование: ')
#                         self.products[i]['Наименование'] = new_product_name
#                     if atr == '2':
#                         new_weight = input(f'Введите новый вес, кг: ')
#                         self.products[i]['Вес'] = new_weight
#                     if atr == '3':
#                         new_price = input(f'Введите новый возраст, лет: ')
#                         self.products[i]['Цена'] = new_price
#                     if atr == '0':
#                         break
#                     print(f'Данные о товаре обновлены!')
#
#     def get_product(self, search_name):
#         print(f'Выполняется поиск информации о товаре {search_name} ...')
#         print(f'Найдены товары:')
#         if search_name == 'all':
#             print(self.products)
#         else:
#             for i in range(len(self.products)):
#                 if self.products[i]['Наименование'] == search_name:
#                     print(f'{self.products[i]}')
#
# product_inventory = ProductInventory()
# product_inventory.add_product('Хлеб', '0.5', '30')
# product_inventory.add_product('Молоко', '1', '55')
# product_inventory.add_product('Творог', '0.5', '35')
# product_inventory.add_product('Творог', '0.5', '45')
# product_inventory.get_product('Хлеб')
# product_inventory.get_product('Молоко')
# product_inventory.update_product('Молоко')
# product_inventory.get_product('all')


# 2. Разработайте систему управления библиотекой Python, позволяющую добавлять новые типы книг без изменения
# существующей кодовой базы.
# В системе должен быть базовый класс Book, определяющий общие свойства и методы для всех типов книг.
# Подклассы, такие как FictionBook, NonFictionBook и ReferenceBook, должны наследоваться от класса Book
# и предоставлять определенные реализации для соответствующих типов.
# Чтобы добавить новый тип книги, вы должны иметь возможность создать новый подкласс книги
# и реализовать необходимые функции без изменения существующего кода. Библиотечная система
# должна по-прежнему иметь возможность беспрепятственно обрабатывать новый тип книг.
# Придерживаясь принципа открытости/закрытости, система управления библиотекой позволит
# легко расширять ее без необходимости изменения основной кодовой базы, повышая удобство сопровождения
# и снижая риск появления ошибок.

# Решение:

# from abc import ABC, abstractmethod
#
# class Book(ABC):
#     @abstractmethod
#     def add_book(self, author, title: list):
#         pass
#
#     @abstractmethod
#     def get_book(self, author):
#         pass
#
#     @abstractmethod
#     def delete_book(self, author):
#         pass
#
# # Художественная книга
# class FictionBook(Book):
#     author_books = {}
#     books_entire_list = []
#
#     def add_book(self, author, title: list):
#         self.author = author
#         self.title = title
#         self.author_books = {'Автор': self.author, 'Название книг': self.title}
#         self.books_entire_list.append(self.author_books)
#         print(f'Добавлено: {self.author_books}')
#
#     def get_book(self, author):
#         print()
#         print(f'Запрос на поиск книг активирован!')
#         print(f'Выполняется поиск книг...')
#         for i in range(len(self.books_entire_list)):
#             if self.books_entire_list[i]['Автор'] == author:
#                 print(f'Перечень найденных книг:')
#                 print(f'Автор: {author}: ', self.books_entire_list[i]['Название книг'], "\n")
#         print()
#
#     def delete_book(self, author):
#         print()
#         print(f'Запрос на поиск книг активирован!')
#         print(f'Выполняется поиск книг для удаления...')
#         for i in range(len(self.books_entire_list)):
#             if self.books_entire_list[i]['Автор'] == author:
#                 print(f'Перечень найденных книг:')
#                 print(f'Автор: {author}: ', self.books_entire_list[i], "\n")
#                 title_del_book = input('Введите название удаляемой книги автора: ')
#                 for j in range(len(self.books_entire_list[i]['Название книг'])):
#                     if self.books_entire_list[i]['Название книг'][j] == title_del_book:
#                         del self.books_entire_list[i]['Название книг'][j]
#                         print(f'Книга "{title_del_book}" удалена!')
#                         break
#
# fict_book_db = FictionBook()
# print()
# fict_book_db.add_book('Фёдор Михайлович Достоевский', ['Преступление и наказание', 'Идиот'])
# fict_book_db.add_book('Лев Николаевич Толстой', ['Анна Каренина', 'Война и мир', 'Воскресение'])
# fict_book_db.get_book('Лев Николаевич Толстой')
# fict_book_db.add_book('Алексей Николаевич Толстой', ['Граф Калиостро'])
# fict_book_db.delete_book('Фёдор Михайлович Достоевский')
# fict_book_db.get_book('Фёдор Михайлович Достоевский')
#
# # Аналогичным образом работают остальные классы типов книг
# # Подробно расписывать не буду
#
# # Научно-популярная книга
# class NonFictionBook(Book):
#     def add_book(self, author, title):
#         pass
#
#     def get_book(self, author):
#         pass
#
#     def delete_book(self, author):
#         pass
#
# # Справочник
# class ReferenceBook(Book):
#     def add_book(self, author, title):
#         pass
#
#     def get_book(self, author):
#         pass
#
#     def delete_book(self, author):
#         pass
#
# # Добавляем новый тип книг "Учебные книги"
# class EducationalBook(Book):
#     def add_book(self, author, title):
#         pass
#
#     def get_book(self, author):
#         pass
#
#     def delete_book(self, author):
#         pass




# 3. Создайте программу Python, определяющую иерархию классов для различных геометрических фигур,
# таких как Shape, Circle, Rectangle и Triangle.
# Класс Shape должен служить базовым классом, предоставляя общие свойства и методы для всех фигур.
# Каждый конкретный класс формы (Circle, Rectangle, Triangle) должен наследоваться от Shape
# и реализовывать свои собственные методы, такие как calculate_area() и calculate_perimeter().
# Программа должна позволять вам рассматривать любую фигуру как экземпляр класса Shape,
# обеспечивая соблюдение принципа подстановки Лисков. Это означает, что вы должны иметь
# возможность заменить любую конкретную фигуру объектом Shape в любой части программы, не влияя на её выполнение.
# Разрабатывая иерархию классов в соответствии с принципом замещения Лискова, вы создаете систему,
# которая является более гибкой, расширяемой и способной единообразно обрабатывать операции, связанные с формами.

# Решение:
# class Shape:
#     def __init__(self):
#         pass
#
# class Circle(Shape):
#     @staticmethod
#     def calculate_area(r):
#         return 3.14 * r * r
#
#     @staticmethod
#     def calculate_perimeter(r):
#         return 2 * 3.14 * r
#
# class Rectangle(Shape):
#     @staticmethod
#     def calculate_area(a, b):
#         return a * b
#
#     @staticmethod
#     def calculate_perimeter(a, b):
#         return (a + b) * 2
#
# class Triangle(Shape):
#     @staticmethod
#     def calculate_area(a, b, c):
#         p = (a + b + c) / 2  # - полупериметр
#         return (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
#
#     @staticmethod
#     def calculate_perimeter(a, b, c):
#         return a + b + c
#
# triangle = Triangle()
# print(triangle.calculate_area(2, 2, 2))
# print(triangle.calculate_perimeter(2, 2, 2))


# 4. Разработайте программу Python для службы обмена сообщениями, которая включает два отдельных интерфейса:
# TextMessaging и MultimediaMessaging.
# Интерфейс TextMessaging должен определять методы, специфичные для текстовых сообщений,
# такие как send_text_message(), receive_text_message() и get_message_history().
# Интерфейс MultimediaMessaging должен включать методы, специфичные для мультимедийных сообщений,
# такие как send_multimedia_message(), receive_multimedia_message() и view_media_gallery().
# Классы, представляющие различные службы обмена сообщениями, должны реализовывать соответствующие интерфейсы
# в зависимости от их возможностей. Например, класс, реализующий TextMessaging, может обрабатывать текстовые сообщения,
# а класс, реализующий MultimediaMessaging, может обрабатывать как текстовые, так и мультимедийные сообщения.
# Разделяя интерфейсы, вы гарантируете, что классам нужно будет реализовать только соответствующие методы,
# предотвращая их принуждение к предоставлению ненужной функциональности. Это способствует лучшей организации кода
# и снижает вероятность раздувания классов или нарушения принципа единой ответственности.

# Решение:
# # Текстовые сообщения
# class TextMessaging:
#     text_message_history = []
#
#     def send_text_message(self, shipped_text_message):
#         self.shipped_text_message = shipped_text_message
#         self.text_message_history.append(self.shipped_text_message)
#         print(f'Отправлено текстовое сообщение: {self.shipped_text_message}')
#
#     def receive_text_message(self, accept_text_message):
#         self.accept_text_message = accept_text_message
#         print(f'Принято текстовое сообщение: {self.accept_text_message}')
#         self.text_message_history.append(self.accept_text_message)
#
#     def get_message_history(self):
#         print(f'История текстовых сообщений:')
#         print(self.text_message_history)
#
# # Мультимедийные сообщения
# class MultimediaMessaging(TextMessaging):
#     mult_message_history = []
#
#     def send_multimedia_message(self, shipped_mult_message):
#         self.shipped_mult_message = shipped_mult_message
#         self.mult_message_history.append(self.shipped_mult_message)
#         print(f'Отправлено мультимедийное сообщение: {self.shipped_mult_message}')
#
#     def receive_multimedia_message(self, accept_mult_message):
#         self.accept_mult_message = accept_mult_message
#         print(f'Принято мультимедийное сообщение: {self.accept_mult_message}')
#         self.mult_message_history.append(self.accept_mult_message)
#
#     def view_media_gallery(self):
#         print(f'Содержимое медиа-галереи:')
#         print(self.mult_message_history)
#
# text_mes_serv = TextMessaging()
# text_mes_serv.send_text_message('Привет, Мир!')
# text_mes_serv.receive_text_message('Привет!')
# print()
# text_mes_serv.get_message_history()
# print()
# mult_mes_serv = MultimediaMessaging()
# mult_mes_serv.send_text_message('Здравствуй, Мир!')
# mult_mes_serv.receive_text_message('Здравствуй!')
# print()
# mult_mes_serv.get_message_history()
# print()
# mult_mes_serv.send_multimedia_message('КАРТИНКА')
# mult_mes_serv.receive_multimedia_message('ВИДЕО-КЛИП')
# print()
# mult_mes_serv.view_media_gallery()


# 5. Разработайте систему ведения журнала Python, которая поддерживает различные типы средств ведения журнала,
# например ConsoleLogger, FileLogger и DatabaseLogger. Реализуйте принцип инверсии зависимостей,
# используя абстракции (интерфейсы) для ведения журнала.
# Определите интерфейс с именем Logger, который включает такие методы, как log_info(), log_warning() и log_error().
# Каждый класс регистратора (ConsoleLogger, FileLogger, DatabaseLogger) должен реализовать этот интерфейс
# и предоставить собственную реализацию методов ведения журнала.
# Модули высокого уровня в системе должны зависеть от интерфейса регистратора, а не от конкретных реализаций регистратора.
# Это позволяет легко подключать или заменять различные типы регистраторов,
# не влияя на функциональность модулей высокого уровня.
# Придерживаясь принципа инверсии зависимостей, вы создаете гибкую и расширяемую систему ведения журналов,
# которая обеспечивает слабую связанность и модульность вашей кодовой базы.

# Решение:
# Консольный регистратор
#
# from abc import ABC, abstractmethod
#
# class Logger(ABC):
#     @abstractmethod
#     def log_info(self):
#         pass
#
#     @abstractmethod
#     def log_warning(self):
#         pass
#
#     @abstractmethod
#     def log_error(self):
#         pass
#
# class ConsoleLogger(Logger):
#     def log_info(self):
#         print(f'Информация от консольного регистратора!')
#
#     def log_warning(self):
#         print(f'Предупреждение от консольного регистратора!')
#
#     def log_error(self):
#         print(f'Ошибка от консольного регистратора!')
#
# # Файловый регистратор
# class FileLogger(Logger):
#     def log_info(self):
#         print(f'Информация от файлового регистратора!')
#
#     def log_warning(self):
#         print(f'Предупреждение от файлового регистратора!')
#
#     def log_error(self):
#         print(f'Ошибка от файлового регистратора!')
#
# # Регистратор базы данных
# class DatabaseLogger(Logger):
#     def log_info(self):
#         print(f'Информация от регистратора базы данных!')
#
#     def log_warning(self):
#         print(f'Предупреждение от регистратора базы данных!')
#
#     def log_error(self):
#         print(f'Ошибка от регистратора базы данных!')
#
# console = ConsoleLogger()
# file = FileLogger()
# database = DatabaseLogger()
# print()
# console.log_info()
# console.log_warning()
# console.log_error()
# print()
# file.log_info()
# file.log_warning()
# file.log_error()
# print()
# database.log_info()
# database.log_warning()
# database.log_error()


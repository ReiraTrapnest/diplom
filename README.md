#### Рысс Руслана, поток 08-a venus

# Сдача финального проекта

## Работа с базой данных

#### Задание 1
- Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 

#### Задание 2
- Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:
Если поле finished == true, то вывести статус 2.
Если поле canсelled == true, то вывести статус -1.
Если поле inDelivery == true, то вывести статус 1.
Для остальных случаев вывести 0.

##### Технические примечания:
Доступ к базе осуществляется с помощью команды psql -U morty -d scooter_rent. Пароль: smith.
У psql есть особенность: если таблица в базе данных с большой буквы, то её в запросе нужно брать в кавычки. Например, select * from “Orders”.

## Автоматизация теста к API

### Теперь автоматизируй сценарий, который подготовили коллеги-тестировщики:
- Клиент создает заказ.
Проверяется, что по треку заказа можно получить данные о заказе.
##### Шаги автотеста:
1. Выполнить запрос на создание заказа.
2. Сохранить номер трека заказа.
3. Выполнить запрос на получения заказа по треку заказа.
4. Проверить, что код ответа равен 200.

К проекту добавь файлы .gitignore и README.MD .
Технические примечания:
Логи лежат в файле error.log в папке /var/www/backend/logs.
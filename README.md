# Практикум по языку Python

Задание 1. 
Используя Python и модули requests и re написать скрипт, извлекающий из веб-страницы (например, mosigra.ru) все адреса электронной почты.

Задание 2.
Используя Python и модули requests и re написать скрипт, получающий все адреса подразделов сайта (относительные url) и для каждой из них выполнить поиск адресов электронной почты (см. задание 1).

Задание 3. 
Используя Python и модуль requests и bs4 написать скрипт, извлекающий новости (отдельно заголовок, аннотацию, авторов) из веб-страницы новостного агентства (напр. washingtonpost.com). Требуется использовать поиск по дереву html, а не регулярные выражения.

Задание 4. 
Используя Python  и библиотеки Queue и Thread, а так же код из 3 задания, написать скрипт, который создает фоновый поток и в нем периодично обновляет страницу новостного агентства и отслеживает новые новости (которые ещё не выводились). Фоновый поток использует объект очередь для передачи в основной поток новый новостей. Новости выводятся на печать из основного потока.

# Скрипты для работы с электронным дневник школы

В проекте 3 скрипта для "взлома" электронного дневника школы со стороны интерфейса для учеников
Код сайта находится по адресу: https://dvmn.org/filer/canonical/1562234129/166/

## Описание скриптов

- `def fix_marks(schoolkid)` - поиск оценок ниже 4 для заданного ученика и их изменение на 5
- `def remove_chastisements(schoolkid)` - поиск замечаний для заданного ученика и их удаление
- `def def create_commendation(schoolkid, to_change)` - добавление похвалы для заданного ученика и заданного предмета. 
Текст похвалы формируется случайным образом из 30 возможных вариантов.


## Описание моделей

На сайте есть ученики: `Schoolkid`. Класс ученика определяется через комбинацию его полей `year_of_study` — год обучения и `group_letter` — литера класса. Вместе получается, например, 10А. Ученик связан со следующими моделями:

- `Mark` — оценка на уроке, от 2 до 5.
- `Commendation` — похвала от учителя, за особые достижения.
- `Chastisement` — замечание от учителя, за особые проступки.

Все 3 объекта связаны не только с учителем, который их создал, но и с учебным предметом (`Subject`). Примеры `Subject`:

- Математика 8 класса
- Геометрия 11 класса
- Русский язык 1 класса
- Русский язык 4 класса

`Subject` определяется не только названием, но и годом обучения, для которого учебный предмет проходит.

За расписание уроков отвечает модель `Lesson`. Каждый объект `Lesson` — урок в расписании. У урока есть комбинация `year_of_study` и `group_letter`, благодаря ей можно узнать для какого класса проходит этот урок. У урока есть `subject` и `teacher`, которые отвечают на вопросы "что за урок" и "кто ведёт". У урока есть `room` — номер кабинета, где он проходит. Урок проходит в дату `date`.

Расписание в школе строится по слотам:

- 8:00-8:40 — 1 урок
- 8:50-9:30 — 2 урок
- ...

У каждого `Lesson` есть поле `timeslot`, которое объясняет, какой номер у этого урока в расписании.

## Запуск

- Скачайте код сайта по адресу https://dvmn.org/filer/canonical/1562234129/166/
- Установка кода сайта и его запуск по его документации.
- Для использования файла со скриптами рядом с файлом manage.py и подключите через импорт
- Также возможно запускать скрипты из shell django, для этого скопируйте код из scripts.py
в shell
- Имя ученика и название предмета надо вводит в строковом формате, например "Музыка"

## Сообщения об ошибках

- При вводе имени не существующего ученика вызывается ошибка `DoesNotExist` 
- Если ввели имя ученика, а таких учеников несколько (например просто "Петр") то вызывается ошибка `MultipleObjectsReturned` 
- При вводе названия предмета с ошибкой или не существующего предмета выдается сообщение `Неправильное название предмета`

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
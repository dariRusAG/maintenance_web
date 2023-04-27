# Отчет по сопровождению программного средства

## Глава 1.
Название программного средства: сайт-агрегатор мероприятий ДВФУ
Авторы: Агапова Дарья, Накао Полина

## Глава 2. Исходное описание функционала (до сопровождения)
**Просмотр афиши:**
1.	Просмотр всех мероприятий на сайте
2.	Просмотр подробной информации о мероприятии: название, тип, тема, организатор, количество участников, количество зарегистрировавшихся на мероприятие, дата мероприятия, время, площадка, место проведения, статус, описание
3.	Выбор фильтров для поиска: тип, тема, организатор, дата, время, площадка, статус
4.	Просмотр мероприятий по выбранным фильтрам на сайте
5.	Просмотр числа мероприятий для каждой категории фильтра – тип, тема, организатор, площадка, статус
6.	Очистка фильтров для поиска
7.	Возможность записи на мероприятие
8.	Возможность отмены записи на мероприятие
9.	Запрет записи на мероприятия, в случае исчерпания количества свободных мест

**Авторизация:**
1.	Возможность авторизоваться на сайте
2.	Уведомление о некорректности данных в случае введения неправильного логина или пароля

**Просмотр личного кабинета:**
1.	Просмотр всех мероприятий, в которых участвует пользователь
2.	Просмотр подробной информации о мероприятии: название, тип, тема, организатор, количество участников, количество зарегистрировавшихся на мероприятие, дата мероприятия, время, площадка, место проведения, статус, описание
3.	Просмотр мероприятий по выбраному фильтру на сайте
4.	Выбор фильтра для поиска: статус мероприятия
5.	Возможность отмены записи на мероприятие
6.	Возможность оценить завершенное мероприятие – поставить оценку и написать отзыв
7.	Для мероприятий статусов «завершено» и «отменено» выводятся дополнительные  сообщения, информирующие об изменении их статуса
8.	Для мероприятий статуса «перенесено» выводится дополнительное сообщение с новой и актуальной датой мероприятия
9.	Для пользователей, не участвующих в мероприятиях, вывод информации об отсутствии записей

## Глава 3. Новое описание функционала (после сопровождения)
**Функции администратора:**
1.	Добавление новых мероприятий и информации о них
2.	Редактирование информации о мероприятиях
3.	Удаление мероприятий
4.	Просмотр пользовательских оценок мероприятий
5.	Возможность добавления или отклонения предложенных пользователями мероприятий

**Просмотр афиши:**
1.	Вывод афиш для каждого мероприятия (изменение визуального представления каталога – добавление картинок афиш)
2.	Вывод информации о количестве найденных по фильтрам мероприятий
3.	Сортировка мероприятий по дате, алфавиту и статусу
4.	Выделение наиболее популярных мероприятий на площадке по проценту зарегистрированных участников от общего их числа
5.	Возможность предложить свое мероприятие от лица организатора

**Регистрация**
1.	Возможность регистрации для новых пользователей
2.	Уведомление о некорректности данных в случае введения существующего логина, некорректного пароля или логина

**Просмотр личного кабинета:**
1.	Сортировка мероприятий по дате, алфавиту и статусу
2.	Удаление аккаунта

## Глава 4. Перечень изменений в интерфейсе (в режиме «до и после»)
**Изменения в блоках мероприятий:**
•	добавлены афиши мероприятий;
•	изменено расположение и стиль текста о мероприятии;
•	название, тип и статус мероприятия выделены особым стилем;
•	изменено визуальное оформление кнопок;
•	исправлен стиль рамки блока;
•	изменен стиль информации об отмене или переносе мероприятия.
![image](https://user-images.githubusercontent.com/91362737/234792827-5cff47d8-55d8-4164-99d9-6f00d3a9bc12.png)

**Изменения в блоке подробной информации о мероприятии:**
•	изменен общий стиль и положение текста в блоке;
•	название и тип мероприятия, а также текст описания выделены особым стилем;
•	добавлено визуальное отображения нажатия кнопки выхода из окна;
•	стиль серого экрана модального окна изменен на более прозрачный;
•	исправлена ошибка прокрутки главной страницы вместо модального окна просмотра информации о мероприятии;
•	исправлены отступы между информацией о мероприятии (в старой версии отступ между количеством зарегистрировавшихся на мероприятие и датой мероприятия отсутствовал).
![image](https://user-images.githubusercontent.com/91362737/234793001-9dc3582d-7419-4d9b-a5bc-ef5e465d5360.png)

**Изменения в окне поиска мероприятий:**
•	изменена рамка фильтров для поиска мероприятий на адаптируемую (в старой версии рамка съезжала при разных размерах девайсов);
•	изменены отступы между категориями мероприятий на более большие(рис. 3);
•	изменен стиль кнопок в блоке фильтров мероприятий;
•	изменен баг в стиле кнопки «Личный кабинет» (в старой версии текст иногда отображался синим вместо белого).
![image](https://user-images.githubusercontent.com/91362737/234793063-30875c53-5fc9-43df-b963-3d703e5cb9c3.png)

**Изменения в окне авторизации:**
•	изменен размер окна авторизации;
•	добавлено визуальное отображения нажатия кнопки выхода из окна;
•	изменены размеры полей ввода данных;
•	изменен стиль кнопки «Войти»;
•	изменен стиль рамки блока;
•	стиль серого экрана модального окна изменен на более прозрачный.
![image](https://user-images.githubusercontent.com/91362737/234793766-66d0d986-2e04-4dc8-958d-67dbfd77df7a.png)

**Изменения в личном кабинете пользователя:**
•	изменен стиль и расположение надписи «Мероприятия, на которые вы зарегистрировались»;
•	изменен стиль рамки фильтров мероприятия на адаптируемую;
•	изменен стиль и расположение кнопок «Найти» и «Очистить».
![image](https://user-images.githubusercontent.com/91362737/234794111-5ca860fd-bd71-46d0-a9cc-d63d0f47f6e0.png)

Добавление новых функций:
•	добавление новых мероприятий и информации о них;
![image](https://user-images.githubusercontent.com/91362737/234794166-ba63ea54-2829-4051-b1d5-595c7e4e18c5.png)

•	редактирование информации о мероприятиях;
![image](https://user-images.githubusercontent.com/91362737/234794251-d9fd28b8-7cf1-4173-ad14-20ae0dfb864d.png)

•	удаление мероприятий;
![image](https://user-images.githubusercontent.com/91362737/234794309-9c98baa8-4f55-41a1-82b0-d2ef03cfaa0b.png)

•	просмотр пользовательских оценок мероприятий;
![image](https://user-images.githubusercontent.com/91362737/234794344-98d079d7-4166-42c4-a75c-1e2e5a353de3.png)

•	возможность добавления или отклонения предложенных пользователями мероприятий;
![image](https://user-images.githubusercontent.com/91362737/234794392-c1e4513a-b4b1-4dcc-a4ff-3371376e3308.png)

•	вывод информации о количестве найденных по фильтрам мероприятий;
![image](https://user-images.githubusercontent.com/91362737/234794417-8d869697-9064-4085-a955-62542f70c0d7.png)

•	сортировка мероприятий по дате, алфавиту и статусу;
![image](https://user-images.githubusercontent.com/91362737/234794461-7d3337dc-f9ca-45db-a757-5e4f52d7a9a7.png)

•	выделение наиболее популярных мероприятий на площадке по проценту зарегистрированных участников от общего их числа (если больше 30% мест занято, то мероприятие выделяется цветной рамкой);
![image](https://user-images.githubusercontent.com/91362737/234794510-241353c6-358b-4b39-bbdb-281a533ac3a9.png)

•	возможность предложить свое мероприятие от лица организатора;
![image](https://user-images.githubusercontent.com/91362737/234794540-c2c0ddd4-b910-4946-b348-2435ab002e5e.png)

•	возможность регистрации для новых пользователей;
![image](https://user-images.githubusercontent.com/91362737/234794575-92fae736-f0b6-45a1-813a-d3747dd6f9a8.png)

•	уведомление о некорректности данных в случае введения существующего логина, некорректного пароля или логина;
![image](https://user-images.githubusercontent.com/91362737/234794606-47847897-0bd2-4469-a577-959066b5e357.png)

•	удаление аккаунта.
![image](https://user-images.githubusercontent.com/91362737/234794643-267751ac-a08a-478a-936a-665e1672cebc.png)

## Глава 5. Описание рефакторинга кода
### Фаза 1: очистка кода
**Проблема:** В проекте присутствуют много закомментированных участков кода, лишние отступы, слишком длинные строки кода, излишние комментарии. Из-за этого код был труднопонимаемым и тяжело читаемым.
**Решение:**
•	убрать мертвый код (переменные, функции, библиотеки);
![image](https://user-images.githubusercontent.com/91362737/234795164-c8c5b1a4-90d5-453a-9b74-5744643ccb9a.png)
•	убрать излишние комментарии;
•	добавить недостающие отступы;
![image](https://user-images.githubusercontent.com/91362737/234795195-3da54612-c4af-4fd2-a170-4c8cdec7590f.png)
•	добавить переносы строк;
![image](https://user-images.githubusercontent.com/91362737/234795238-2db52d4c-ef2a-4b92-b286-05ae0da1c6fd.png)
•	добавить пробелы между идентификаторами и операторами;
![image](https://user-images.githubusercontent.com/91362737/234795259-fc2dd7b5-0f3f-4840-9ecc-02e533b078f5.png)

### Фаза 2: понимание кода
**Проблема:** В проекте присутствует большое количество функций и условий без комментариев, а также переменных с трудно интерпретируемыми названиями, из-за чего код тяжело понять.
**Решение:**
•	добавление комментариев к основным условиям и функциям;
![image](https://user-images.githubusercontent.com/91362737/234795566-ed717720-a186-4542-a8e0-74b1a4990aca.png)
•	переименование переменных на легко интерпретируемые;
![image](https://user-images.githubusercontent.com/91362737/234795599-0a6793d4-dc1e-4fc1-b49a-aaadb6374812.png)

### Фаза 3: переработка стилей
**Проблема:** В проекте нет адаптируемого и универсального стиля написания стилей, из-за чего интерфейс ломается при использовании различных девайсов.
**Решение:**
•	вынести в отдельный файл стили, написанные в html;
![image](https://user-images.githubusercontent.com/91362737/234795764-2236f66a-bbc1-4703-aa6f-7e2acf45d612.png)
•	заменить теги наподобие <br> и <p> соответствующими классами в файле стилей; 
![image](https://user-images.githubusercontent.com/91362737/234795790-ec28d4aa-3cb4-49a8-9f8c-a523e1490ae7.png)
•	заменить однотипные классы, использующие одинаковые стили на меньшее количество универсальных классов;
![image](https://user-images.githubusercontent.com/91362737/234795817-79b161ad-2a12-491e-9197-7d07765d09c9.png)
•	заменить все размерные значения стилей в css на адаптируемые.
![image](https://user-images.githubusercontent.com/91362737/234795853-b322eaed-438a-4fe0-9b36-fa5ca12edb36.png)

### Фаза 4: вынос дублирующегося кода
**Проблема:** В проекте присутствует большое количество дублирующегося кода, из-за чего программная система слишком перегружена. 
**Решение:**
•	вынести дублирующий код из html в отдельный макрос;
![image](https://user-images.githubusercontent.com/91362737/234795972-7563fe3b-1f09-4141-92fd-c65f59ee43dd.png)
•	вынести дублирующий код из python в отдельный файл;
![image](https://user-images.githubusercontent.com/91362737/234795993-049b7658-0703-4fc4-b4ed-8712a3cc1546.png)

### Фаза 4: оптимизация кода
**Проблема:** В проекте есть функции и куски кода, в которых усложненные условия, а также используется много ненужных переменных, из-за чего такие функции усложняют и перегружают код.
**Решение:**
• Оптимизировать такие функции с помощью условий case, новых универсальных переменных и т.д. 
![image](https://user-images.githubusercontent.com/91362737/234796132-75994433-0f24-4d8e-b707-3e57e210a9c9.png)

### Фаза 5: создание универсального шаблона
**Проблема:** В проекте для каждой функции вывода информации о мероприятиях используется свой html-код.
**Решение:**
•	Создать универсальный html-шаблон для вывода как информации обо всех мероприятиях, так и подробной информации об одном мероприятии.
![image](https://user-images.githubusercontent.com/91362737/234796304-2fcaba89-2e3e-4f95-91eb-edc323c3648a.png)
![image](https://user-images.githubusercontent.com/91362737/234796320-dbc771aa-da2a-4603-b224-56a7870dfbe3.png)

## Глава 6. Заключение
Таким образом, в процессе сопровождения функционал программного средства был изменен примерно на 41% от общего числа функций, интерфейс – примерно на 64% от общего числа элементов и экранных форм, рефакторинг затронул примерно 77% кода.


 

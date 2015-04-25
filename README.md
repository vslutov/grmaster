# group-master

## License

    group-master - tool for dividing students into groups
    Copyright (C) 2015  Lutov V. S. <vslutov@yandex.ru>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

## Введение

Данная прогоамма предназначена для удобного и быстрого распределения студентов
первого курса на группы с учетом их пожеланий и их уровня английского.

Программа писалась для факультета ВМК и учитывает его специфику.

- В каждой группе две английские подгруппы, которые могут быть как одного
  уровня знаний, так и разных.
- На каждом потоке свое количество групп, примерно одинакового размера.
- Потоки принципиально ничем не отличаются (разве что, студент может захотеть
  на какой-то конкретный поток.

Если у вас другие требования для распределения, то меняйте код программы так,
как вам нужно, в рамках соблюдения лицензии GNU AGPL. Подробнее о коде
читайте в разделе [для программистов](#Для-программистов).

## Установка и запуск

Если не хотите заморачиваться с установкой - откройте эту ссылку
[http://lutov.net/grmaster](http://lutov.net/grmaster) и переходите к следущему
пункту [использование](#Использование).

Если вы по каким-то причинам, решили настроить свой сервер или запустить
приложение из консоли, то все равно прочитайте раздел
[использование](#Использование), а потом переходите в раздел
[для программистов](#Для-программистов).

## Использование

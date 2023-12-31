#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Необходимо использовать словарь, содержащий следующие ключи: название пункта
# назначения, номер поезда, время отправления. Написать программу, выполняющую
# следующие действия: ввод с клавиатуры данных в список, состоящий из словарей
# заданной структуры; записи должны быть упорядочены по времени отправления поезда;
# вывод на экран информации о поездах, направляющихся в пункт, название которого
# введено с клавиатуры; если таких поездов нет, выдать на дисплей соответствующее сообщение.

import sys


if __name__ == '__main__':
    # Список пунктов (станций).
    stations = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о пункте.
            name = input("Название пункта: ")
            # Создать словарь.
            station = {'name': name}
            print("Добавить поезд? n/y")
            cucle = input()
            if cucle == 'n':
                station['train'] = 'Поездов нет'
                station['time'] = ' '
            else:
                train = input("Номер поезда: ")
                dep_time = input("Время отправления поезда: ")
                # Добавить в словарь поезд и время.
                station['train'] = train
                station['time'] = dep_time

            # Добавить словарь в список.
            stations.append(station)

            # Отсортировать список в случае необходимости по времени поезда.
            if len(stations) > 1:
                stations.sort(key=lambda item: item.get('time', ''))

        elif command.startswith('info '):
            # Инициализировать счетчик.
            count = 0

            # Разбить команду на части для выделения названия пункта.
            name_station = command.split(' ', maxsplit=1)
            name_station = name_station[1]
            for station in stations:
                if station.get('name') == name_station:
                    count += 1
                    print("Номер поезда пункта: ", station.get('train'),
                          "Время отправления: ", station.get('time'))

            # Если счетчик равен 0, то станции не найдены.
            if count == 0:
                print("Станции не найдены.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить станцию;")
            print("info <станция> - запросить информацию о станции;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)

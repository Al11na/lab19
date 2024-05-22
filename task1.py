#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import os

def add_flight(flights):
    """
    Функция для ввода данных о рейсах с клавиатуры и добавления их в список.
    """
    destination = input("Введите пункт назначения: ")
    flight_number = input("Введите номер рейса: ")
    airplane_type = input("Введите тип самолета: ")
    flights.append({"destination": destination, "flight_number": flight_number, "airplane_type": airplane_type})
    flights.sort(key=lambda x: x["flight_number"])
    save_flights(flights)

def display_flights(flights, destination):
    """
    Функция для отображения номеров рейсов и типов самолетов, вылетающих в заданный пункт назначения.
    """
    found = False
    for flight in flights:
        if flight["destination"] == destination:
            print(f"Номер рейса: {flight['flight_number']}, Тип самолета: {flight['airplane_type']}")
            found = True
    if not found:
        print("Рейсов в заданный пункт назначения нет.")

def save_flights(flights):
    """
    Функция для сохранения данных о рейсах в файл JSON.
    """
    with open("flights.json", "w") as file:
        json.dump(flights, file, ensure_ascii=False, indent=4)

def load_flights():
    """
    Функция для загрузки данных о рейсах из файла JSON.
    """
    if os.path.exists("flights.json"):
        with open("flights.json", "r") as file:
            return json.load(file)
    return []

def main():
    """
    Основная функция программы.
    """
    flights = load_flights()
    while True:
        print("1. Добавить рейс")
        print("2. Показать рейсы в пункт назначения")
        print("3. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            add_flight(flights)
        elif choice == '2':
            destination = input("Введите пункт назначения для поиска: ")
            display_flights(flights, destination)
        elif choice == '3':
            break
        else:
            print("Неправильный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

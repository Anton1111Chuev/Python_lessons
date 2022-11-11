import sqlite3
from sqlite3 import Error
import json
import csv

class PhoneDirectory:

    def __init__(self):
        self.connection = sqlite3.connect('sqlite_phone.db')

    def get_by_name(self, name):
        query = f'select a.phone_numner, a.descriptions from phone_number as a inner ' \
                f'join people as b on a.people_id=b.people_id  where b.name like "%{name}%"'
        return self.__get_request(query)

    def save_file(self, format="json"):
        format_dict = {'json': self.__save_json,
                       'csv': self.__save_csv}
        if not format_dict.get(format):
            return 'Не известный формат файла'

        query = f'select a.people_id, b.name , a.phone_numner, a.descriptions from phone_number as a inner ' \
                f'join people as b on a.people_id=b.people_id order by a.people_id'
        data = self.__get_request(query, False)

        if not data:
            return ' файл не может быть сформирован не корректный запрос к субд'

        return format_dict[format](data)

    def __save_json(self, data):
        result = []
        for row in data:
            result.append({"people_id": row[0],
                           "name": row[1],
                           "phone_numner": row[2],
                           "descriptions": row[3]
                           })

        try:
            with open('data.txt', 'w', encoding="utf-8") as outfile:
                json.dump(result, outfile, ensure_ascii=False, indent=4)
            return 'записан json файл  data.txt'
        except:
            return 'При записи файла возникла ошибка'

    def __save_csv(self, data):
        try:
            file = open('data.csv', 'w')
            with file:
                writer = csv.writer(file)
                writer.writerows(data)
            return 'записан csv файл  data.csv'
        except:
             return 'При записи файла возникла ошибка'


    def __get_request(self, query, text_on_error=True):
        cursor = self.connection.cursor()
        result = ""
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
        except Error as e:
            if text_on_error:
                result = "При обращении к СУБД произошла ошибка"
        finally:
            return result


    def load_file_in_data(self, filename, format="json"):
        format_dict = {'json': self.__getdata_json,
                       'csv': self.__getdata_csv}

        if not format_dict.get(format):
            return 'Не известный формат файла'
        try:
            list_people, list_phone_num = format_dict[format](filename)
        except:
            return "Ошибка чтения файла"

        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM phone_number"
            cursor.execute(query)
            query = "DELETE FROM people"
            cursor.execute(query)
            cursor.executemany("INSERT INTO people VALUES(?, ?);", list_people)
            cursor.executemany("INSERT INTO phone_number VALUES(?, ?, ?);", list_phone_num)
            self.connection.commit()
            cursor.close()
        except:
            return "Ошибка при работе с СУБД"

        return "Данные загружены"


    def __getdata_json(self, filename):
        with open(filename, encoding="utf-8") as json_file:
            data = json.load(json_file)

        list_people = []
        list_phone_num = []
        for el in data:
            list_people.append((int(el['people_id']), el['name']))
            list_phone_num.append((int(el['people_id']), el['phone_numner'], el['descriptions']))

        list_people1 = list(set(list_people))
        return (list_people1, list_phone_num)


    def __getdata_csv(self, filename):
        list_people = []
        list_phone_num = []
        with open(filename) as file:
            file_reader = csv.reader(file, delimiter=",")
            #1,Иванов Иван Иванович,777-77-77,рабочий
            for row in file_reader:
                if len(row) >= 4:
                    list_people.append((int(row[0]), row[1]))
                    list_phone_num.append((int(row[0]), row[2], row[3]))
        list_people1 = list(set(list_people))
        return (list_people1, list_phone_num)





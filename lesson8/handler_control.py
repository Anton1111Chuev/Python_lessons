import json

from lesson8.model import PeopleData

class Handler_control():

    def __init__(self):
        self.data_object = PeopleData()

    def get_all_category_name(self):
        return self.data_object.get_all_category_name()

    def get_data(self, person_name=' ', person_category_name=' '):
        data = self.data_object.get_person_info(person_name, person_category_name)
        return "\n".join(map(str, data))

    def del_person_info(self, id_contact):
        return self.data_object.del_person_info(id_contact)

    def save_json(self):
        data = self.data_object.get_all_contact()

        try:
            with open('data.txt', 'w', encoding="utf-8") as outfile:
                json.dump(data, outfile, ensure_ascii=False, indent=4)
            return 'записан json файл  data.txt'
        except:
            return 'При записи файла возникла ошибка'


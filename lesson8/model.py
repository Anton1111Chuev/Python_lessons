import logging

from sqlalchemy import create_engine, MetaData, Table, select, delete

from lesson8.log_project import init_logger


class PeopleData():
    def __init__(self):
        self.engine = create_engine('sqlite:///db_people.db', encoding='UTF-8')
        self.conn = self.engine.connect()  # (close_with_result=True)
        self.metadata = MetaData()
        self.people = Table('people', self.metadata, autoload_with=self.engine)
        self.contacts = Table('contacts', self.metadata, autoload_with=self.engine)
        self.contact_types = Table('contact_types', self.metadata, autoload_with=self.engine)
        self.category = Table('category', self.metadata, autoload_with=self.engine)
        init_logger(__name__)
        self.logger = logging.getLogger(__name__)
    def get_person_info(self, person_or_phone_name=' ', person_category_name=' '):
        self.logger.debug(f'get_person_info name=  {person_or_phone_name} category = {person_category_name}')
        person_or_phone_name = f'%{person_or_phone_name}%'
        if person_category_name == ' ':
            s = select([
                self.contacts.c.value,
                self.people.c.name,
                self.contact_types.c.type,
                self.category.c.name_category
            ]).select_from(
                self.contacts.join(self.people).join(self.category).join(self.contact_types)
            ).where(self.contacts.c.value.like(person_or_phone_name) |
                    (self.people.c.name.like(person_or_phone_name)))
        else:
            s = select([
                self.contacts.c.value,
                self.people.c.name,
                self.contact_types.c.type,
                self.category.c.name_category
            ]).select_from(
                self.contacts.join(self.people).join(self.category).join(self.contact_types)
            ).where(
                ((self.contacts.c.value.like(person_or_phone_name)) |
                 (self.people.c.name.like(person_or_phone_name))) &
                (self.category.c.name_category == person_category_name)
            )
        try:
            rs = self.conn.execute(s)
        except Exception as e:
            self.logger.error(str(e))
            return "Возникла ошибка"

        return rs.fetchall()

    def get_all_category_name(self):
        self.logger.debug(f'get_all_category_name')
        s = select([
            self.category.c.name_category
        ]).select_from(self.category)
        rs = self.conn.execute(s)
        result = []

        for row in rs:
            result.append(row.name_category)
        return result

    def del_person_info(self, id_contact):
        self.logger.debug(f'del_person_info id_contact = {id_contact}')
        try:
            id = int(id_contact)
        except:
            self.logger.error(f'del_person_info  Введено не число id_contact = {id_contact}')
            return "Введено не число повторите ввод"

        s = delete(self.contacts).where(
            self.contacts.c.id == id
        )
        rs = self.conn.execute(s)

        return f'Запись с ИД {id_contact} удалена или отсутсвует'

    def get_all_contact(self):
        self.logger.debug(f'get_all_contact')
        s = select([
            self.people.c.name,
            self.contacts.c.value,
            self.contact_types.c.type,
            self.category.c.name_category
        ]).select_from(
            self.contacts.join(self.people).join(self.category).join(self.contact_types))
        rs = self.conn.execute(s)
        result = []

        for row in rs:
            result.append(dict(row))

        return result

    def __del__(self):
        self.conn.close()

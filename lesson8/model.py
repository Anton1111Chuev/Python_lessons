from sqlalchemy import create_engine, MetaData, Table, select, delete


class PeopleData():
    def __init__(self):
        self.engine = create_engine('sqlite:///db_people.db', encoding='UTF-8')
        self.conn = self.engine.connect()  # (close_with_result=True)
        self.metadata = MetaData()
        self.people = Table('people', self.metadata, autoload_with=self.engine)
        self.contacts = Table('contacts', self.metadata, autoload_with=self.engine)
        self.contact_types = Table('contact_types', self.metadata, autoload_with=self.engine)
        self.category = Table('category', self.metadata, autoload_with=self.engine)

    def get_person_info(self, person_or_phone_name=' ', person_category_name=' '):
        person_or_phone_name = f'%{person_or_phone_name}%'
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

        rs = self.conn.execute(s)
        return rs.fetchall()

    def get_all_category_name(self):
        s = select([
            self.category.c.name_category
        ]).select_from(self.category)
        rs = self.conn.execute(s)
        result = []

        for row in rs:
            result.append(row.name_category)
        return result

    def del_person_info(self, id_contact):
        try:
            id = int(id_contact)
        except:
            return "Введено не число повторите ввод"

        s = delete(self.contacts).where(
            self.contacts.c.id == id
        )
        rs = self.conn.execute(s)

        return f'Запись с ИД {id_contact} удалена или отсутсвует'

    def get_all_contact(self):
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

from model import PhoneDirectory

def get_action(phone_directory = PhoneDirectory(), action="", *args, **kwargs):
    if action == "get_by_name":
        return phone_directory.get_by_name(kwargs['name'])
    elif action == "save_json":
        return phone_directory.save_file(format="json")
    elif action == "save_csv":
        return phone_directory.save_file(format="csv")
    elif action == "load_json":
        return phone_directory.load_file_in_data(kwargs['filename'], format='json')
    elif action == "load_csv":
        return phone_directory.load_file_in_data(kwargs['filename'], format='csv')
    else:
        return "Действие не определено"











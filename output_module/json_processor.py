import json
#CREATE JSON FILE FOR OUTPUT
class JSON_PROCESSOR:
    def __init__(self, data_from_input_json, data_from_text, path_output_json):
        self.data_from_input_json = data_from_input_json
        self.data_from_text = data_from_text
        self.path_output_json = path_output_json


    def create_json(self):
            i = 1
            dict = {}
            for element in self.data_from_text:
                value_dict = {}
                num = str(element["number"])

                # во входящем JSON перепутаны ключи фамилий и имен, поэтому пришлось изменить здесь
                surname = self.data_from_input_json[num]["Name"]
                name = self.data_from_input_json[num]["Surname"]

                result = element["time"]

                minuts, seconds = divmod(result.seconds, 60)
                time_str_micro = result.microseconds // 1000
                time_str_micro = f"{time_str_micro:02d}"[:2]

                full_time = f"{minuts:02d}:{seconds:02d},{time_str_micro}"

                value_dict["Нагрудный номер"] = num
                value_dict["Имя"] = surname
                value_dict["Фамилия"] = name
                value_dict["Результат"] = full_time

                dict[i] = value_dict

                i += 1

            output_path = self.path_output_json

            with open(output_path, "w") as json_file:
                json.dump(dict, json_file, ensure_ascii=False, indent=4)

            print(f"Файл JSON '{output_path}' создан успешно.")




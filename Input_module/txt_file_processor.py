import re
from datetime import datetime
#CREATE DICTIONARY FROM TXT FILE

def create_runner_numbers_times_dict(file_path):
    number_results = []
    with open(file_path, "r",encoding="utf-8-sig") as file:
        lines = file.readlines()

        output_dict = {}

        for line in lines:
            if line[0].isdigit():
                num = int(re.search(r'\d+', line).group())
                if num not in output_dict:
                    output_dict[num] = []
                if "start" in line:
                    start_time = re.search(r'\d{2}:\d{2}:\d{2},\d{6}', line).group()
                    array = output_dict[num]
                    temp_dict = {"START": start_time}
                    array.append(temp_dict)
                elif "finish" in line:
                    finish_time = re.search(r'\d{2}:\d{2}:\d{2},\d{6}', line).group()
                    array = output_dict[num]
                    temp_dict = {"FINISH": finish_time}
                    array.append(temp_dict)

    for key, value in output_dict.items():
        #print(f"Ключ: {key}, Значение: {value}")
        start_value = datetime.strptime(value[0]["START"],'%H:%M:%S,%f')
        finish_value = datetime.strptime(value[1]["FINISH"],'%H:%M:%S,%f')


        result = {"number": key, "time": (finish_value - start_value)}

        number_results.append(result)

    number_results = sorted(number_results, key = lambda x: x["time"])

    return number_results





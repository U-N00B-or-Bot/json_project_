from Input_module import json_parcer
from Input_module import txt_file_processor
from output_module import json_processor

input_json_path = "resources/competitors2.json"
txt_file_path = "resources/results.txt"
out_path = "resources/final_results.json"

parcer = json_parcer.parser(input_json_path)
text_file_processor = txt_file_processor.create_runner_numbers_times_dict(txt_file_path)
output_processor = json_processor.JSON_PROCESSOR(data_from_input_json=parcer,
                                          data_from_text= text_file_processor,
                                          path_output_json=out_path)

result = output_processor.create_json()






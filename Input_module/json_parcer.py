import re
import json



def parser(file_path):
    with open(file_path, 'rb') as json_file:
        content = json_file.read()
        utf8_boms = [b'\xef\xbb\xbf', b'\x00\x00\xfe\xff', b'\xff\xfe\x00\x00']
        found_boms = [bom for bom in utf8_boms if re.search(re.escape(bom), content)]
        if found_boms:
            print(f"Найдены следующие BOM для UTF-8: {found_boms}")
            for bom in utf8_boms:
                content = content.replace(bom, b'')
                content = content.decode('utf-8')
        else:
            print("BOM для UTF-8 не найдены в файле.")
            content = content.decode('utf-8-sig')
        return (json.loads(content))

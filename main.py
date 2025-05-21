from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    with open(path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    
    def process_file(file):
        file = file.replace('\\', '\\\\')  # 백슬래시 escape
        file = file.replace('/', '\\/')    # 슬래시 escape
        file = file.replace('"', '\\"')    # 큰따옴표 escape
        return file

    template_start = '{\"English\":\"'
    template_mid = '\",\"German\":\"'
    template_end = '\"}'

    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        german_file = process_file(german_file)

        json_string = template_start + english_file + template_mid + german_file + template_end
        processed_file_list.append(json_string)

    return processed_file_list

def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w', encoding='utf-8') as f:
        for file in file_list:
            f.write(file + '\n')

if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    write_file_list(processed_file_list, path + 'concated.json')

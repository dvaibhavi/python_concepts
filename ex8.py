

def count_uppercase_letters(file_name):
    count = 0

    try:
        with open(file_name, 'r') as file:
            for line in file:
                for char in line:
                    if char.isupper():
                        count += 1
    except FileNotFoundError:
        print(f"file {file_name} for found.")
    except PermissionError:
        print(f" Cannot read {file_name}. Access denied")
    except Exception as e:
        print(e)
    
    return count


def hash_display(file_path):
    #file_path = "matter.txt"

    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
            formatted_content = "#".join(content)
            print(formatted_content)
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied. Unable to read the file.")
    except Exception as e:
        print("An error occurred:", str(e))

# print(count_uppercase_letters("exercise.txt"))
print(count_uppercase_letters("error.txt"))
print(hash_display("error.txt"))
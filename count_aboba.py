def count_aboba(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            count = content.lower().count('aboba')
            return count
    except FileNotFoundError:
        return "File not found"

file = "C:/Users/Student/AlyAri/coolstory.txt"

result = count_aboba(file)
print(f"Count of 'aboba': {result}")
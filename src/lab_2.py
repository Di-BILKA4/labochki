#задание 1.1
def min_max(nums):
    if len(nums) == 0:
        raise ValueError('Список пуст')
    return (min(nums), max(nums))
#задание 1.2
def unique_sorted(nums):
    return sorted(set(nums))
#задание 1.3
def flatten(mat):
    result = []
    for row in mat:
        if type(row) != list and type(row) != tuple:
            raise TypeError('Строка/элемент не является списком/кортежем')
        result.extend(row)
    return result



#задание 2.1
def transpose(mat):
    if len(mat) == 0:
        return []
    cols = len(mat[0])
    for row in mat:
        if len(row) != cols:
            raise ValueError('Строки разной длины')
    result = []
    for j in range(cols):
        new_row = []
        for i in range(len(mat)):
            new_row.append(mat[i][j])
        result.append(new_row)
    return result
#задание 2.2
def row_sums(mat):
    if len(mat) == 0:
        return []
    cols = len(mat[0])
    for row in mat:
        if len(row) != cols:
            raise ValueError('Строки разной длины')
    return [sum(row) for row in mat]
#задание 2.3
def col_sums(mat):  # 3
    if len(mat) == 0:
        return []
    cols = len(mat[0])
    for row in mat:
        if len(row) != cols:
            raise ValueError('Строки разной длины')
    sums = [0] * cols
    for row in mat:
        for j in range(cols):
            sums[j] += row[j]
    return sums



#задание 3.1
def format_record(rec):
    if type(rec) is not tuple or len(rec) != 3:
        raise ValueError('Ожидается кортеж из 3 элементов')
    fio = rec[0]
    group = rec[1]
    gpa = rec[2]
    if type(gpa) not in (int, float):
        raise TypeError('GPA введён неверно')
    if type(fio) is not str or len(fio.strip()) == 0:
        raise ValueError('ФИО введены неверно')
    if type(group) is not str or len(group.strip()) == 0:
        raise ValueError('Группа введена неверно')
    group = group.strip()
    parts = fio.strip().split()
    if len(parts) < 2:
        raise ValueError('ФИО должно содержать минимум фамилию и имя')
    surname = parts[0].capitalize()
    initials = ''
    for name in parts[1:3]:
        initials += name[0].upper() + '.'
    return f'{surname} {initials}, гр. {group}, GPA {gpa:.2f}'
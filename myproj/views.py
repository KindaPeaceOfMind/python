import json
import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Путь к файлу с данными
JSON_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'json_data.json')


def load_json_data():
    """Загрузка данных из JSON-файла"""
    with open(JSON_FILE_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def index(request):
    """Обработчик главной страницы - простой текст"""
    return HttpResponse("Hello, world!")


def indexRender(request):
    """Обработчик страницы с рендерингом шаблона"""
    return render(request, 'index.html', {})


def universityInfo(request):
    """Задание 8: Информация об университете"""
    data = load_json_data()
    
    # Подсчёт подразделений
    admin_units = len(data.get('administrative_units', []))
    scientific_units = data.get('scientific_educational_units', [])
    
    mega_faculties_count = len(scientific_units)
    faculties_count = 0
    departments_count = 0
    
    for mega in scientific_units:
        faculties = mega.get('faculties', [])
        faculties_count += len(faculties)
        for faculty in faculties:
            departments_count += len(faculty.get('departments', []))
    
    context = {
        'university': data,
        'admin_count': admin_units,
        'scientific_count': mega_faculties_count,
        'mega_faculties_count': mega_faculties_count,
        'faculties_count': faculties_count,
        'departments_count': departments_count,
    }
    return render(request, 'universityInfo.html', context)


def disciplineInfo(request):
    """Задание 9: Информация о дисциплине (берём первую для примера)"""
    data = load_json_data()
    
    # Поиск первой образовательной программы
    program = None
    for mega in data.get('scientific_educational_units', []):
        for faculty in mega.get('faculties', []):
            for dept in faculty.get('departments', []):
                programs = dept.get('educational_programs', [])
                if programs:
                    program = programs[0]
                    program['department_name'] = dept.get('name')
                    break
            if program:
                break
        if program:
            break
    
    # Подсчёт групп
    groups_count = 0
    if program and 'study_years' in program:
        for year in program['study_years']:
            groups_count += len(year.get('groups', []))
        program['groups_count'] = groups_count
    
    context = {'program': program}
    return render(request, 'disciplineInfo.html', context)


def groupsInfo(request):
    """Задание 10: Информация о студентах всех групп"""
    data = load_json_data()
    
    all_groups = []
    
    for mega in data.get('scientific_educational_units', []):
        for faculty in mega.get('faculties', []):
            for dept in faculty.get('departments', []):
                for prog in dept.get('educational_programs', []):
                    for year in prog.get('study_years', []):
                        for group in year.get('groups', []):
                            # Добавляем информацию о группе
                            group_data = {
                                'group_name': group.get('name'),
                                'students': []
                            }
                            for student in group.get('students', []):
                                student_info = {
                                    'tab_number': student.get('tab_number'),
                                    'fullname': f"{student.get('lastname')} {student.get('firstname')} {student.get('middlename')}",
                                    'scholarship': student.get('scholarship')
                                }
                                group_data['students'].append(student_info)
                            all_groups.append(group_data)
    
    context = {'groups': all_groups}
    return render(request, 'groupsInfo.html', context)


def departmentsInfo(request):
    """Задание 11: Информация о кафедрах"""
    data = load_json_data()
    
    departments = []
    
    for mega in data.get('scientific_educational_units', []):
        for faculty in mega.get('faculties', []):
            for dept in data.get('departments', []):  # Исправлено: берём из faculty
                for dept in faculty.get('departments', []):
                    dept_info = {
                        'id': dept.get('id'),
                        'name': dept.get('name'),
                        'head': dept.get('head'),
                        'teachers': dept.get('teachers', []),
                        'programs': []
                    }
                    
                    for prog in dept.get('educational_programs', []):
                        prog_info = {
                            'number': prog.get('number'),
                            'name': prog.get('name'),
                            'discipline': prog.get('discipline')
                        }
                        dept_info['programs'].append(prog_info)
                    
                    departments.append(dept_info)
    
    context = {'departments': departments}
    return render(request, 'departmentsInfo.html', context)


def universityStructure(request):
    """Задание 12: Структура университета с иерархией"""
    data = load_json_data()
    
    def get_initials(fullname):
        """Преобразование ФИО в формат 'Фамилия И.О.'"""
        parts = fullname.split()
        if len(parts) >= 3:
            return f"{parts[0]} {parts[1][0]}.{parts[2][0]}."
        return fullname
    
    context = {
        'university': data,
        'get_initials': get_initials,
    }
    return render(request, 'universityStructure.html', context)
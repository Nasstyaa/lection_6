class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = ()

    def __str__(self):
        current_courses = ''.join(self.courses_in_progress)
        completed_courses = ''.join(self.finished_courses)

        count_of_grades = 0
        for grade in self.grades:
            count_of_grades += len(self.grades[grade])
        sum_of_grades = sum(map(sum, self.grades.values()))
        self.average_grade = sum_of_grades / count_of_grades
        result = (
            f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade}\nКурсы в процессе изучения: {current_courses}\nЗавершенные курсы: {completed_courses}')

        return result

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Некорректно')
            return
        return self.average_grade < other.average_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade = ()
        self.courses_attached = []

    def __str__(self):
        count_of_grades = 0
        for grade in self.grades:
            count_of_grades += len(self.grades[grade])
        sum_of_grades = sum(map(sum, self.grades.values()))
        self.average_grade = sum_of_grades / count_of_grades
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade}'
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Некорректно')
            return
        return self.average_grade < other.average_grade


class Reviewerer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}')


# экземпляры классов

lecturer_1 = Lecturer('Иван', 'Петров')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Петр', 'Иванов')
lecturer_2.courses_attached += ['Java']

reviewer_1 = Reviewerer('Сергей', 'Васильев')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewerer('Анна', 'Федорова')
reviewer_2.courses_attached += ['Java']

student_1 = Student('Алексей', 'Рыбаков', 'м')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['C++']

student_2 = Student('Евгений', 'Павлов', 'м')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Pascal']

# вызов методов

student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 10)

student_1.rate_hw(lecturer_2, 'Java', 5)
student_1.rate_hw(lecturer_2, 'Java', 7)

student_2.rate_hw(lecturer_2, 'Java', 10)
student_2.rate_hw(lecturer_2, 'Java', 8)

student_2.rate_hw(lecturer_1, 'Python', 10)
student_2.rate_hw(lecturer_1, 'Python', 8)

reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 9)

reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 9)

reviewer_2.rate_hw(student_2, 'Java', 8)
reviewer_2.rate_hw(student_2, 'Java', 7)

reviewer_2.rate_hw(student_1, 'Java', 8)
reviewer_2.rate_hw(student_1, 'Java', 7)

print(f'Оценки студентам:\n\n{student_1}\n\n{student_2}')
print()

print(f'Оценки лекторам:\n\n{lecturer_1}\n\n{lecturer_2}\n')
print()

# сравнение студентов и лекторров по средней оценке
is_lt = (student_1 < student_2)
print(is_lt)

is_lt_2 = (lecturer_1 < lecturer_2)
print(is_lt_2)

students_list = [student_1, student_2]
lecturers_list = [lecturer_1, lecturer_2]


def rate_of_students(students_list, name_of_course):
    grade = 0
    count = 0
    for student in students_list:
        if student.courses_in_progress == [name_of_course]:
            grade += student.average_grade
            count += 1
    total_av_grade = grade / count
    return total_av_grade


def rate_of_lecturer(lecturer_list, name_of_course):
    grade = 0
    count = 0
    for lecturer in students_list:
        if lecturer.courses_in_progress == [name_of_course]:
            grade += lecturer.average_grade
            count += 1
    total_av_grade = grade / count
    return total_av_grade


print(f"Средняя оценка за домашние задания по всем студентам в рамках  курса Python: {rate_of_students(students_list, 'Python')}")
print()

print(f"Средняя оценка за домашние задания по всем студентам в рамках  курса Java: {rate_of_students(students_list, 'Java')}")
print()

print(f"средняя оценка за лекции всех лекторов в рамках курса Python: {rate_of_lecturer(lecturers_list, 'Python')}")
print()

print(f"средняя оценка за лекции всех лекторов в рамках курса Java: {rate_of_lecturer(lecturers_list, 'Java')}")
print()

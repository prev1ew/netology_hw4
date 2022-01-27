class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def get_average_grade(self, course=''):
        if self.grades:
            sum_of_items = 0
            quantity = 0
            for k, v in self.grades.items():
                if course and k.lower() != course.lower():
                    continue
                for item in v:
                    sum_of_items += item
                    quantity += 1
            return round(sum_of_items / quantity, 1)
        else:
            return 'Нет оценок'

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() < other.get_average_grade()
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за домашние задания: {self.get_average_grade()} \n' \
               f'Курсы в процессе изучения: {", ".join(self.finished_courses)} \n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}'

    def rate_lecturer(self, lector, course, grade):
        if isinstance(lector, Lecturer) \
                and (course in self.courses_in_progress or course in self.finished_courses) \
                and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 0


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self, course=''):
        if self.grades:
            sum_of_items = 0
            quantity = 0
            for k, v in self.grades.items():
                if course and k.lower() != course.lower():
                    continue
                for item in v:
                    sum_of_items += item
                    quantity += 1
            return round(sum_of_items / quantity, 1)
        else:
            return 0

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_grade() < other.get_average_grade()
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за лекции: {self.get_average_grade()}'


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def calculate_average_grade(list_of_people, course=''):
    # Так как 2 метода называются одинаково используется один метод для 2х классов
    sum_of_grades = 0
    if list_of_people:
        for item in list_of_people:
            if isinstance(item, Student) or isinstance(item, Lecturer):
                sum_of_grades += item.get_average_grade(course)
        return round(sum_of_grades / len(list_of_people), 1)
    else:
        return 0


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'test']
best_student.finished_courses += ['Python', 'test2']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

some_lecturer = Lecturer('Lecturer', 'TS')
some_lecturer.courses_attached.append('Python')

other_lecturer = Lecturer('Lecturer', 'Other')
other_lecturer.courses_attached.append('Python')

print(best_student)
print()
print(cool_mentor)
print()
print(some_lecturer)
print()

print(best_student.rate_lecturer(some_lecturer, 'Python', 5))
print(best_student.rate_lecturer(other_lecturer, 'Python', 4))

print()
print(some_lecturer)
print()
print(other_lecturer)
print(some_lecturer > other_lecturer)

new_student = Student('Ruoy', 'Eman', 'your_gender')
new_student.courses_in_progress += ['Python', 'test']
new_student.finished_courses += ['Python', 'test2']

cool_mentor.rate_hw(new_student, 'Python', 9)

print()
print(new_student)
print()
print(best_student)
print(new_student < best_student)

print(calculate_average_grade([new_student, best_student], 'Python'))
print(calculate_average_grade([cool_mentor, other_lecturer], 'Python'))


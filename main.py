class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average_score(self):
        summa_score = 0
        for course in self.grades.values():
            average_score = sum(course) / len(course)
        summa_score += average_score
        return summa_score

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__average_score()}\
        \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student!')
            return
        return self.__average_score() < other.__average_score()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Lecturer(Mentor):

    def __average_score(self):
        summa_score = 0
        for course in self.grades.values():
            average_score = sum(course) / len(course)
        summa_score += average_score
        return summa_score

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average_score()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer!')
            return
        return self.__average_score() < other.__average_score()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

cool_lecturer = Lecturer('Oleg', 'Buligin')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']
super_lecturer = Lecturer('Ivan', 'Ivanov')
super_lecturer.courses_attached += ['Git']
cool_reviewer = Reviewer('Pety', 'Petrov')
cool_lecturer.grades['Git'] = [8, 6, 7]
cool_lecturer.grades['Python'] = [10, 8, 10, 9, 8]
super_lecturer.grades['Git'] = [6, 7, 9, 5, 8]

best_student = Student('Ruoy', 'Eman', 'male')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']
super_student = Student('Koly', 'Kolyn', 'male')
super_student.courses_in_progress += ['Git']
best_student.grades['Git'] = [10, 6, 9, 8, 10]
best_student.grades['Python'] = [8, 8]
super_student.grades['Git'] = [8, 7, 9, 5, 7]

super_student.rate_lecture(super_lecturer, 'Git', 8)
super_student.rate_lecture(cool_lecturer, 'Git', 5)
super_student.rate_lecture(super_lecturer, 'Git', 9)
best_student.rate_lecture(cool_lecturer, 'Python', 10)
best_student.rate_lecture(cool_lecturer, 'Python', 7)
print(cool_lecturer.grades)
print(super_lecturer.grades)
print('_______________')
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(super_student, 'Git', 5)
cool_reviewer.rate_hw(super_student, 'Git', 8)
cool_reviewer.rate_hw(super_student, 'Git', 10)
print(best_student.grades)
print(super_student.grades)
print('______________')
print(best_student)
print(super_student)
print(cool_lecturer)
print(super_lecturer)
print(cool_reviewer)
print('______________')
print(best_student > super_student)
print(cool_lecturer > super_lecturer)

student_list = [best_student, super_student]
def middle_grade_student(student_list, course):
    middle_sum = 0
    for student in student_list:
        res = sum(student.grades[course]) / len(student.grades[course])
        middle_sum += res
    print(middle_sum)

middle_grade_student(student_list, 'Git')

lecturer_list = [cool_lecturer, super_lecturer]
def middle_grade_lecturer(lecturer_list, course):
    middle_sum = 0
    for lecturer in lecturer_list:
        res = sum(lecturer.grades[course]) / len(lecturer.grades[course])
        middle_sum += res
    print(middle_sum)

middle_grade_lecturer(lecturer_list, 'Git')

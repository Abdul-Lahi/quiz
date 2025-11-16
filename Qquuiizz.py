import json
import secrets
    
def register(user_register_type, name):
    id = secrets.token_urlsafe(3)
    email = input('Enter your email: ')
    password = input('Enter your password: ')
    user = {
        "id" : id,
        "name" : name,
        "type" : user_register_type,
        "email" : email,
        "password" : password
        }
    with open("quiz_users.txt", "r") as file:
        content = file.read()
        if len(content) == 0:
            users = []
        else:
            users = json.loads(content)
    for ex_user in users:
        if ex_user['id'] == user['id']:
            print('Id already exist')
            return False
        if ex_user['email'] == user['email'] :
            print('Email already exist')
            return False
    users.append(user)
    with open ("quiz_users.txt", "w") as file:
        json.dump(users, file, indent=4)
    print(f"{user['name']} sign up successful")

def set_quiz():
    quiz = []
    number_of_questions = int(input('Enter number of questions you want to set: '))
    for x in range(1, (number_of_questions + 1)):
        question = input(f'Enter question {x}: ')
        option_a = input(f'Enter option a: ')
        option_b = input(f'Enter option b: ')
        option_c = input(f'Enter option c: ')
        option_d = input(f'Enter option d: ')
        answer = input(f'Enter answer for question {x}: ')
        quiz.append({'question': question, '(A)': option_a, '(B)': option_b, '(C)': option_c, '(D)': option_d,  'answer': answer})
    with open ("quiz.txt", "w") as file:
        json.dump(quiz, file, indent=4)
    print(f'{number_of_questions} questions saved successfully')

def take_quiz(name):
    with open("quiz.txt") as file:
        quiz = json.load(file)
    if len(quiz) == 0:
        print("No quiz found. Please set a quiz first.")
        return
    
    score = 0
    results = []
    for item in quiz:
        user_input = input(f"{item['question'],'(A)',item['(A)'],'(B)',item['(B)'],'(C)',item['(C)'],'(D)',item['(D)']}: ").strip().lower()
        if user_input == item['answer'].strip().lower():
            print('Correct!')
            score += 1
        else:
            print(f'Incorrect! The correct answer was: {item["answer"]}')
    
    print(f'Your score is {score}/{len(quiz)}') 

    with open ("result.txt", "r") as file:
        stored_results = file.read()
        if len(stored_results) == 0:
            results = []
        else:
            results = json.loads(stored_results)
        result = {
            'name' : name,
            'score' : score
        }
        results.append(result)
    with open ("result.txt", "w") as file:
        json.dump(results, file)     
        
def login(name):
    username = name
    password = input('Enter password: ')
    with open ("quiz_users.txt") as file:
        data = json.load(file)
        for user in data:
            if (username == user['name']) and (password == user['password']): 
                print(f'Welcome {username}')
                return True
        print('Username or password is incorrect')
        return False

def teacher_task():
    while True:
        print('----OPTIONS----')
        print(
            '1. View all students\n'
            '2. Delete all students\n' 
            '3. Set quiz\n'
            '4. View students result\n'
            '5. Quit'
        )
        option = int(input('Input option (1-5): '))
        if option == 1:
            with open ("quiz_users.txt", "r") as file:
                content = file.read()
                if len(content.strip()) == 0:
                    print('No student available')
                else:
                    users = json.loads(content)
                    for u in users:
                        if u['type'] == 'student':
                            print(u)
        elif option == 2:
            with open ("quiz_users.txt", "r") as file:
                content = file.read()
                if len(content.strip()) == 0:
                    print('No student available')
                else:
                    users = json.loads(content)
                    for u in users:
                        if u['type'] == 'student':
                            users.remove(u)
                    with open("quiz_users.txt", "w") as file:
                        json.dump(users, file)
        elif option == 3:
            set_quiz()
        elif option == 4:
            with open ("result.txt") as file:
                results = json.load(file)
                print(results)
        elif option == 5:
            print('Goodbye!')
            break
        else:
            print('Enter valid option')

def student_task(name):
    print('----OPTIONS----')
    print(
        '1. Take quiz\n' 
        '2. View personal result\n'
        '3. Update name\n'
        '4. Exit'
    )
    while True:
        option = int(input('Input option (1-4): '))
        if option == 1:
            take_quiz(name)
        elif option == 2:
            with open ("result.txt") as file:
                    content = file.read()
                    stud = json.loads(content)
                    student_name = name
                    for s in stud:
                        if s['name'] == student_name:
                            print(f"{student_name}'s score is {str(s['score'])}")
                        else:
                            print(f"{student_name}'s score is not found.")
        elif option == 3:
            new_name = input("Enter your new name: ")
            with open("quiz_users.txt", "r") as file:
                users = json.load(file)
            for user in users:
                if user['name'] == name:
                    user['name'] = new_name
                    break
            with open("quiz_users.txt", "w") as file:
                json.dump(users, file)
            print("Name updated successfully!")
        elif option == 4:
            print('Goodbye!')
            break
        else:
            print('Enter valid option')
    
def main():
    name = input('Enter your name: ')
    startup = input('Enter register to register or login to login: ').lower()
    if startup == 'register':
        user_register_type = input('Do you want to register as a teacher or a student: ').lower()
        if user_register_type == 'teacher':
            registration = register(user_register_type, name)
            if registration is False:
                print('Registration failed')
                exit()
            teacher_task()    
        elif user_register_type == 'student':
            registration = register(user_register_type, name)
            if registration is False:
                print('Registration failed')
                exit()
            student_task(name)
        else:
            print('Invalid input!')
    elif startup == 'login':
        user_login_type = input('Do you want to login as a teacher or a student: ')
        if user_login_type == 'teacher':
            log_in = login(name)
            if log_in is False:
                
                exit()
            teacher_task()
        elif user_login_type == 'student':
            log_in = login(name)
            if log_in is False:
                print('Unable to login')
            student_task(name)
        else:
            print('Invalid input')
main()
# # # # privileges
# # # # examiners can view all students, can delete student from the system, can set quiz, can view student results.
# # # # student can take quiz, view personal result, can update name

# # # # registration (teachers/examiners)
# # # # students(candidates)
# # # # they have email, names, password, identification

# # # # procedure
# # # # register or login
# # # # register - as teacher or student

# # # # rules
# # # # no two emails are the same
# # # # id cannot be the same

# # # # quiz
# # # # quiz has questions

# # # # questions
# # # # question has options
# # # # question has a correct answer

# # # # result
# # # # result is total correct score over available score
# # # # belong to student

# # # # JSON

# # # users = {{...}, {....}, {...}}

# # # {
# # #     users : {{...}, {....}, {...}},
# # #     results : {{...}, {....}, {...}}
# # # }

# # # User = {
# # #     "id" : 12,
# # #   "name" : "John",
# # #   "type" : "teacher",
# # #   "email" : "....",
# # #   "password" : "..."
# # # }

# # # result = {
# # #     "id" : 12,
# # #     "score" : 50
# # # }

# # # quiz = {
    
# # # }

# # # questions = {
    
# # # }

import random

# Dataset for Academics (General Aptitude Questions)
import random

# Dataset for Academics (General Aptitude Questions)
academics_data = {
    'General Aptitude': [
        {"question": "What is the square root of 144?", "options": ["10", "11", "12", "13"], "answer": "12"},
        {"question": "If 5x = 25, what is the value of x?", "options": ["1", "5", "10", "25"], "answer": "5"},
        {"question": "What is the area of a triangle with base 10 and height 5?", "options": ["25", "30", "50", "55"], "answer": "25"},
        {"question": "What is the value of 3^4?", "options": ["64", "81", "91", "100"], "answer": "81"},
        {"question": "What is the formula for the area of a circle?", "options": ["πr²", "2πr", "πd", "πr³"], "answer": "πr²"},
        {"question": "What is the cube root of 27?", "options": ["1", "3", "9", "27"], "answer": "3"},
        {"question": "Which of the following is a prime number?", "options": ["8", "9", "7", "10"], "answer": "7"},
        {"question": "What is 10% of 250?", "options": ["25", "50", "100", "10"], "answer": "25"},
        {"question": "How many sides does a hexagon have?", "options": ["4", "6", "8", "10"], "answer": "6"},
        {"question": "What is the value of 2^5?", "options": ["32", "64", "128", "256"], "answer": "32"},
        {"question": "What is the square of 15?", "options": ["225", "200", "250", "150"], "answer": "225"},
        {"question": "If 3x + 2 = 11, what is the value of x?", "options": ["3", "4", "5", "6"], "answer": "3"},
        {"question": "What is 45% of 200?", "options": ["90", "100", "120", "130"], "answer": "90"},
        {"question": "What is the next number in the series 2, 4, 6, 8, ...?", "options": ["10", "9", "7", "11"], "answer": "10"},
        {"question": "Which of the following is a perfect square?", "options": ["14", "16", "18", "20"], "answer": "16"},
        {"question": "What is the perimeter of a rectangle with length 10 and width 5?", "options": ["30", "40", "50", "25"], "answer": "30"},
        {"question": "What is 15% of 80?", "options": ["10", "12", "14", "15"], "answer": "12"},
        {"question": "What is the volume of a cube with a side of 4 units?", "options": ["16", "64", "32", "8"], "answer": "64"},
        {"question": "Which of these is a rational number?", "options": ["√2", "π", "1/2", "e"], "answer": "1/2"},
        {"question": "What is the next prime number after 11?", "options": ["13", "17", "19", "23"], "answer": "13"}
    ]
}

# Dataset for Coding Questions
coding_data = {
    'Python': [
        {"question": "What is the output of the following code: print(2 * 3 + 5)?", "options": ["11", "13", "10", "15"], "answer": "11"},
        {"question": "Which of the following is used to define a function in Python?", "options": ["def", "function", "method", "define"], "answer": "def"},
        {"question": "What is the correct way to write a comment in Python?", "options": ["// comment", "# comment", "/* comment */", "<-- comment"], "answer": "# comment"},
        {"question": "Which function can be used to get the length of a string in Python?", "options": ["len()", "length()", "str()", "size()"], "answer": "len()"},
        {"question": "What does the range() function do in Python?", "options": ["Generates a sequence of numbers", "Returns a random number", "Converts an integer to a string", "Finds the length of a list"], "answer": "Generates a sequence of numbers"},
        {"question": "Which of the following data types is immutable in Python?", "options": ["List", "Dictionary", "Tuple", "Set"], "answer": "Tuple"},
        {"question": "Which operator is used for exponentiation in Python?", "options": ["^", "", "//", "/"], "answer": ""},
        {"question": "Which method can be used to convert a string to lowercase in Python?", "options": [".lower()", ".toLower()", ".down()", ".lcase()"], "answer": ".lower()"},
        {"question": "What is the correct syntax for a while loop in Python?", "options": ["while x > 10", "while (x > 10)", "loop while x > 10", "while x > 10:"], "answer": "while x > 10:"},
        {"question": "Which of the following functions is used to get the current working directory in Python?", "options": ["os.getcwd()", "getcwd()", "os.getDirectory()", "currentDir()"], "answer": "os.getcwd()"},
        {"question": "What is the output of the following code: print(5 == 5)?", "options": ["True", "False", "None", "Error"], "answer": "True"},
        {"question": "What is the correct way to handle exceptions in Python?", "options": ["try-except", "catch", "try-throw", "except-throw"], "answer": "try-except"},
        {"question": "Which of the following is the correct way to import a module in Python?", "options": ["import module", "import module_name", "module import", "import module_name as alias"], "answer": "import module_name as alias"},
        {"question": "Which of the following is used for creating a generator in Python?", "options": ["yield", "return", "break", "next"], "answer": "yield"},
        {"question": "Which function is used to open a file in Python?", "options": ["open()", "file.open()", "read()", "file()"], "answer": "open()"},
        {"question": "Which of the following is used to remove an element from a list in Python?", "options": [".remove()", ".delete()", ".erase()", ".pop()"], "answer": ".remove()"},
        {"question": "What is the correct syntax to create a dictionary in Python?", "options": ["dict = {}", "dict = []", "dict = ()", "dict = set()"], "answer": "dict = {}"},
        {"question": "What will the following code print: print([1, 2, 3] * 2)?", "options": ["[1, 2, 3, 1, 2, 3]", "[2, 4, 6]", "[1, 2, 3]", "[1, 2, 3]"], "answer": "[1, 2, 3, 1, 2, 3]"},
        {"question": "Which of the following is used to reverse a string in Python?", "options": ["str[::-1]", "reverse(str)", "str.reverse()", "str.reverse(0)"], "answer": "str[::-1]"},
        {"question": "What is the output of print('hello' + 2)?", "options": ["hello2", "error", "hello", "None"], "answer": "error"}
    ],
    
    'Java': [
        {"question": "Which of these is a valid method signature in Java?", "options": ["public static void main(String[] args)", "static void main(String[] args)", "public void main(String[] args)", "void main(String[] args)"], "answer": "public static void main(String[] args)"},
        {"question": "Which of the following is used to declare an array in Java?", "options": ["array[]", "int[]", "array(int)", "int[array]"], "answer": "int[]"},
        {"question": "In Java, which keyword is used to create an instance of a class?", "options": ["new", "create", "instance", "class"], "answer": "new"},
        {"question": "What is the default value of a boolean variable in Java?", "options": ["true", "false", "null", "undefined"], "answer": "false"},
        {"question": "Which access modifier allows access from anywhere in Java?", "options": ["private", "protected", "public", "default"], "answer": "public"},
        {"question": "Which of these data types are primitive in Java?", "options": ["String", "ArrayList", "int", "Object"], "answer": "int"},
        {"question": "What is the correct way to declare a constant in Java?", "options": ["const int x = 5", "final int x = 5", "constant int x = 5", "int final x = 5"], "answer": "final int x = 5"},
        {"question": "Which method is used to compare two strings in Java?", "options": ["compare()", "equals()", "compareTo()", "stringCompare()"], "answer": "equals()"},
        {"question": "Which of the following is used to exit a loop in Java?", "options": ["break", "exit", "stop", "quit"], "answer": "break"},
        {"question": "In Java, which keyword is used to inherit a class?", "options": ["extends", "implements", "super", "this"], "answer": "extends"},
        {"question": "What is the size of a float in Java?", "options": ["32-bit", "64-bit", "16-bit", "8-bit"], "answer": "32-bit"},
        {"question": "Which of the following can be used to handle exceptions in Java?", "options": ["try-catch", "catch-try", "throw-catch", "exception-catch"], "answer": "try-catch"},
        {"question": "Which method can be used to sort an array in Java?", "options": ["sort()", "Arrays.sort()", "Collections.sort()", "array.sort()"], "answer": "Arrays.sort()"},
        {"question": "Which method is used to get the length of an array in Java?", "options": ["size()", "length()", "getLength()", "count()"], "answer": "length()"},
        {"question": "What will be the output of System.out.println(10 / 3)?", "options": ["3.33", "3", "Error", "30"], "answer": "3"},
        {"question": "Which of these is not a valid loop in Java?", "options": ["for", "while", "foreach", "do-while"], "answer": "foreach"},
        {"question": "Which of the following is the root class of all Java classes?", "options": ["java.lang.Object", "java.util", "java.lang.Class", "java.io.Object"], "answer": "java.lang.Object"},
        {"question": "Which of the following is true about the 'final' keyword in Java?", "options": ["It is used to define constants.", "It is used to define methods.", "It is used to define variables.", "It cannot be used with classes."], "answer": "It is used to define constants."}
    ]
}

# Dataset for Special Academics (PCM Questions)
special_academics_data = {
    'Physics': [
        {"question": "What is Newton's first law of motion?", "options": ["An object will remain at rest unless acted upon by an external force.", "An object will remain at rest or in uniform motion unless acted upon by an external force.", "An object will always accelerate unless acted upon by an external force.", "An object will remain at rest unless it is in motion."], "answer": "An object will remain at rest or in uniform motion unless acted upon by an external force."},
        {"question": "What is the formula for kinetic energy?", "options": ["KE = 1/2 * m * v", "KE = m * v^2", "KE = 1/2 * m * v^2", "KE = m * v^3"], "answer": "KE = 1/2 * m * v^2"},
        {"question": "What is the unit of force?", "options": ["Joule", "Newton", "Pascal", "Watt"], "answer": "Newton"},
        {"question": "What is the speed of light?", "options": ["3 x 10^8 m/s", "3 x 10^6 m/s", "1 x 10^8 m/s", "3 x 10^9 m/s"], "answer": "3 x 10^8 m/s"},
        {"question": "What does Einstein's theory of relativity state?", "options": ["Time is constant.", "Energy equals mass times the speed of light squared.", "Light is faster than sound.", "The Earth is flat."], "answer": "Energy equals mass times the speed of light squared."},
        {"question": "What is the SI unit of acceleration?", "options": ["m/s", "m/s^2", "m", "s"], "answer": "m/s^2"},
        {"question": "What is the formula for gravitational potential energy?", "options": ["PE = m * g * h", "PE = 1/2 * m * v^2", "PE = m * g", "PE = m * h"], "answer": "PE = m * g * h"},
        {"question": "Which of these is a scalar quantity?", "options": ["Force", "Velocity", "Speed", "Acceleration"], "answer": "Speed"},
        {"question": "What is the formula for work done?", "options": ["Work = Force * Distance", "Work = Force * Velocity", "Work = Mass * Acceleration", "Work = Force * Time"], "answer": "Work = Force * Distance"},
        {"question": "Which of the following is a non-renewable energy source?", "options": ["Wind", "Solar", "Oil", "Geothermal"], "answer": "Oil"},
        {"question": "Which of the following is the primary source of energy for the Earth?", "options": ["Sun", "Earth", "Wind", "Moon"], "answer": "Sun"},
        {"question": "Which of these is a property of a sound wave?", "options": ["It can travel through a vacuum.", "It requires a medium to travel.", "It travels faster in a vacuum.", "It is invisible."], "answer": "It requires a medium to travel."},
        {"question": "Which scientist is known for developing the law of universal gravitation?", "options": ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Galileo Galilei"], "answer": "Isaac Newton"},
        {"question": "What is the phenomenon of light bending called?", "options": ["Reflection", "Refraction", "Diffraction", "Dispersion"], "answer": "Refraction"},
        {"question": "What is the value of the gravitational constant?", "options": ["6.674 x 10^-11 N m²/kg²", "9.8 m/s²", "1.6 x 10^-19 C", "3 x 10^8 m/s"], "answer": "6.674 x 10^-11 N m²/kg²"},
        {"question": "What is the main purpose of a transformer?", "options": ["Increase voltage", "Decrease voltage", "Increase current", "Change the direction of current"], "answer": "Increase voltage"},
        {"question": "What is the formula for the pressure in a fluid?", "options": ["P = F/A", "P = m * g", "P = m * v^2", "P = W/t"], "answer": "P = F/A"},
        {"question": "Which of these materials is an insulator?", "options": ["Copper", "Iron", "Wood", "Water"], "answer": "Wood"},
        {"question": "Which force keeps planets in orbit around the sun?", "options": ["Electromagnetic force", "Gravitational force", "Nuclear force", "Frictional force"], "answer": "Gravitational force"}
    ],
    
    'Chemistry': [
        {"question": "What is the atomic number of hydrogen?", "options": ["1", "2", "3", "4"], "answer": "1"},
        {"question": "Which of the following is a noble gas?", "options": ["Oxygen", "Helium", "Nitrogen", "Carbon"], "answer": "Helium"},
        {"question": "Which element has the chemical symbol Na?", "options": ["Sodium", "Nitrogen", "Neon", "Nickel"], "answer": "Sodium"},
        {"question": "What is the pH level of pure water?", "options": ["7", "5", "10", "0"], "answer": "7"},
        {"question": "What is the most abundant gas in the Earth's atmosphere?", "options": ["Oxygen", "Hydrogen", "Carbon dioxide", "Nitrogen"], "answer": "Nitrogen"},
        {"question": "What is the formula for methane?", "options": ["CH4", "C2H6", "C3H8", "C4H10"], "answer": "CH4"},
        {"question": "What is the primary component of natural gas?", "options": ["Methane", "Ethane", "Butane", "Propane"], "answer": "Methane"},
        {"question": "Which of these is an example of a chemical change?", "options": ["Ice melting", "Water boiling", "Burning paper", "Dissolving salt in water"], "answer": "Burning paper"},
        {"question": "What is the molar mass of water (H2O)?", "options": ["18 g/mol", "20 g/mol", "22 g/mol", "16 g/mol"], "answer": "18 g/mol"},
        {"question": "What is the chemical formula for sulfuric acid?", "options": ["H2SO4", "HCl", "NaOH", "HNO3"], "answer": "H2SO4"},
        {"question": "Which of the following is a compound?", "options": ["Oxygen", "Hydrogen", "Water", "Nitrogen"], "answer": "Water"},
        {"question": "What is the color of litmus paper in acidic solution?", "options": ["Red", "Blue", "Green", "Purple"], "answer": "Red"},
        {"question": "What is the process of separating components of a mixture using a solvent?", "options": ["Evaporation", "Distillation", "Filtration", "Chromatography"], "answer": "Chromatography"},
        {"question": "Which of the following is a nonmetal?", "options": ["Iron", "Copper", "Oxygen", "Aluminum"], "answer": "Oxygen"},
        {"question": "What is the name of the process by which plants make their own food?", "options": ["Photosynthesis", "Respiration", "Transpiration", "Germination"], "answer": "Photosynthesis"},
        {"question": "Which of the following is an example of an ionic bond?", "options": ["NaCl", "H2O", "CO2", "O2"], "answer": "NaCl"},
        {"question": "What is the unit of measuring the amount of a substance?", "options": ["Molar", "Gram", "Meter", "Liter"], "answer": "Molar"},
        {"question": "What is the chemical formula for carbon dioxide?", "options": ["CO", "CO2", "C2O", "C2O2"], "answer": "CO2"},
        {"question": "Which element has the highest atomic number?", "options": ["Uranium", "Plutonium", "Oganesson", "Radon"], "answer": "Oganesson"}
    ],
    
    'Mathematics': [
        {"question": "What is the derivative of x^2?", "options": ["2x", "x^2", "x", "x^3"], "answer": "2x"},
        {"question": "What is the integral of 1/x?", "options": ["ln(x)", "x^2", "x", "e^x"], "answer": "ln(x)"},
        {"question": "What is the value of sin(90°)?", "options": ["0", "1", "√2", "2"], "answer": "1"},
        {"question": "What is the Pythagorean theorem?", "options": ["a^2 + b^2 = c^2", "a^3 + b^3 = c^3", "a + b = c", "a^2 - b^2 = c^2"], "answer": "a^2 + b^2 = c^2"},
        {"question": "What is the square root of 64?", "options": ["6", "7", "8", "9"], "answer": "8"},
        {"question": "What is the area of a circle with radius 5?", "options": ["25π", "10π", "5π", "15π"], "answer": "25π"},
        {"question": "What is the formula for the sum of an arithmetic series?", "options": ["S = n/2 * (a + l)", "S = n * (a + l)", "S = n/2 * (a - l)", "S = n * a"], "answer": "S = n/2 * (a + l)"},
        {"question": "What is the solution to the equation x + 5 = 10?", "options": ["5", "10", "15", "0"], "answer": "5"},
        {"question": "What is the value of tan(45°)?", "options": ["1", "0", "√2", "∞"], "answer": "1"},
        {"question": "What is the volume of a sphere with radius 3?", "options": ["36π", "27π", "9π", "81π"], "answer": "36π"},
        {"question": "What is the value of 2!?", "options": ["1", "2", "4", "6"], "answer": "2"},
        {"question": "What is the area of a triangle with base 8 and height 6?", "options": ["24", "48", "14", "16"], "answer": "24"},
        {"question": "What is the value of log(100)?", "options": ["1", "2", "3", "10"], "answer": "2"},
        {"question": "What is the solution to the equation 3x = 9?", "options": ["3", "9", "1", "6"], "answer": "3"},
        {"question": "What is the value of √81?", "options": ["9", "8", "7", "10"], "answer": "9"},
        {"question": "What is the perimeter of a square with side length 5?", "options": ["20", "15", "25", "10"], "answer": "20"},
        {"question": "What is the value of cos(60°)?", "options": ["1", "0", "0.5", "√2"], "answer": "0.5"},
        {"question": "What is the slope of the line y = 2x + 5?", "options": ["2", "5", "1", "0"], "answer": "2"},
        {"question": "What is the solution to the equation 4x + 2 = 14?", "options": ["4", "3", "5", "2"], "answer": "3"}
    ]
}


# Function to handle question selection in MCQ format
def attempt_questions(topic, num_questions):
    questions = random.sample(academics_data.get(topic, []) + coding_data.get(topic, []) + special_academics_data.get(topic, []), num_questions)
    correct_answers = 0

    for question in questions:
        print(f"\nQuestion: {question['question']}")
        options = question['options']
        random.shuffle(options)  # Shuffle options to avoid predictable answers
        
        # Display options
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        # User selects an option
        user_answer_index = int(input("Select the correct option (1-4): ")) - 1
        user_answer = options[user_answer_index]
        
        # Check if the user's answer is correct
        if user_answer == question['answer']:
            correct_answers += 1

    accuracy = (correct_answers / num_questions) * 100
    return correct_answers, num_questions, accuracy

# Main Menu System
def main():
    while True:
        print("\n--- Main Menu ---")
        print("1. Academics (General Aptitude)")
        print("2. Coding (Python, Java)")
        print("3. Special Academics (PCM)")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            print("\n--- Academics (General Aptitude) ---")
            topic = 'General Aptitude'
            num_questions = int(input(f"How many questions would you like to attempt for {topic}? "))
            correct, total, accuracy = attempt_questions(topic, num_questions)
            
            print(f"\nResults for {topic}:")
            print(f"Total questions: {total}")
            print(f"Correct answers: {correct}")
            print(f"Accuracy: {accuracy:.2f}%")

        elif choice == '2':
            print("\n--- Coding (Python, Java) ---")
            print("1. Python")
            print("2. Java")
            coding_topic_choice = input("Select a topic (1-2): ")

            if coding_topic_choice == '1':
                topic = 'Python'
            elif coding_topic_choice == '2':
                topic = 'Java'
            else:
                print("Invalid choice, try again.")
                continue
            
            num_questions = int(input(f"How many questions would you like to attempt for {topic}? "))
            correct, total, accuracy = attempt_questions(topic, num_questions)
            
            print(f"\nResults for {topic}:")
            print(f"Total questions: {total}")
            print(f"Correct answers: {correct}")
            print(f"Accuracy: {accuracy:.2f}%")

        elif choice == '3':
            print("\n--- Special Academics (PCM) ---")
            print("1. Physics")
            print("2. Chemistry")
            print("3. Mathematics")
            topic_choice = input("Select a topic (1-3): ")

            if topic_choice == '1':
                topic = 'Physics'
            elif topic_choice == '2':
                topic = 'Chemistry'
            elif topic_choice == '3':
                topic = 'Mathematics'
            else:
                print("Invalid choice, try again.")
                continue

            num_questions = int(input(f"How many questions would you like to attempt for {topic}? "))
            correct, total, accuracy = attempt_questions(topic, num_questions)
            
            print(f"\nResults for {topic}:")
            print(f"Total questions: {total}")
            print(f"Correct answers: {correct}")
            print(f"Accuracy: {accuracy:.2f}%")

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

# Run the program
if _name_ == "_main_":
    main()
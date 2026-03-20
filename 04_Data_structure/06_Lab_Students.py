"""
Management students systems
=====================================================
System validates data, processes data and generates reports

Topics
- Strings
- Lists
- Exceptions

Stages:
1. Validate student data (email, name, surname)
2. Process data
3. Search and filter students
4. Generate reports and statistics
5. Error handling

"""

# ============================================================================
# Step 1: Validate data
# ============================================================================

def validate_email(email):
    """
    Check email is right.     
    Args:
        email (str): email to validate        
    Returns:
        bool: True if mail is correct but false        
    """
    # Raises:
    #     TypeError: if mail is not a string
    #     ValueError: if mail is empty
    # raises
    if not type(email) is str:
        raise TypeError
    if not len(email) > 0:
        raise ValueError
    
    # reqs
    # Requirements:

    # - it contains a symbol '@'
    if "@" not in email:
        return False      
    
    # - it contains at least  '.' after '@'
    email_parts = email.split("@") 
    if email_parts[1].count(".") <= 0:
        return False      

    # - it cannot start with spaces
    if email[0:1] == " ":
        return False      

    # - at least 5 chars
    if len(email) < 5:
        return False      

    # - before  '@' cannot be empty
    if email[0:1] == "@":
        return False   
    
    return True


def validate_name(name):
    """
    Check name is correct      
    Args:
        name (str): name to validate
    Returns:
        str: validated name and normalized (without spaces and capitalize)
        
    """
    # Raises:
    #     TypeError: Si nom no és una cadena
    #     ValueError: Si el nom no compleix els requisits
    if not type(name) is str:
        raise TypeError
    
    # Requisits:
    # - it cannot be empty
    if not len(name) > 0:
        raise ValueError

    # - at least between 2 and 50 chars(after trim)
    if not (len(name) >= 2 and len(name) <= 50):
        raise ValueError
    
    # - it cannot have numbers
    # - it cannot have special chars(@, #, $, etc.) except spaces and -
    format_name = name.strip()
    if not format_name.isalnum():
        if not (" " in format_name or "-" in format_name):
            raise ValueError
    
    # capitalize
    format_name = format_name.title()
    return format_name


def validate_student_code(code):
    """
    Check student code and normalize it.   
    Args:
        code (str): code to validate      
    Returns:
        str: normalized code with format "EST-XXXX"        
    """
    # Raises:
    #     TypeError: Si codi no és una cadena
    #     ValueError: Si el format és incorrecte
    # Format esperat: EST-XXXX (on XXXX són 4 dígits)
    # Exemples vàlids: "EST-1234", "est-0001", " EST-9999 "  
    if not type(code) is str:
        raise TypeError    
    
    # Requisits:
    # - it starts with "EST-" (case insensitive)
    # - Després del guió han d'haver exactament 4 dígits
    # - S'accepten espais al principi/final (s'eliminaran)
    format_code = code.strip()
    format_prefix = format_code[0:3].upper()
    format_code = format_prefix + format_code[3:]

    if not format_code[0:4] == "EST-":
        raise ValueError 
    
    code_parts = format_code.split("-") 
    if (not len(code_parts[1]) == 4 or not code_parts[1].isnumeric()):
        raise ValueError 
      
    return format_code


# ============================================================================
# Step 2: Process and storage
# ============================================================================

def create_student(code, name, surname, email):
    """
    Create a dictionary with student data after being validated
    Args:
        code (str): Student code
        name (str): Student name
        surname (str): Student surname
        email (str): Student email
    Returns:
        dict: Dictionary with all validated student data
    Raises:
        Exceptions thrown by validation function
    """
    # Validate all data
    code = validate_student_code(code)
    name = validate_name(name)
    surname = validate_name(surname)
    validate_email(email)
    
    # Create and return dictionary
    student = {}
    student["code"] = code
    student["name"] = name
    student["surname"] = surname
    student["email"] = email
    return student


def add_student(students, student):
    """
    Add an student to the end of the list, check it is not duplicated.    
    Duplicate student means if its code or mail already exists     
    Args:
        students (list): List of students
        student (dict): Student data to add
        
    Returns:
        bool: True if added, False if it already exists
        
    Raises:
        TypeError: If parameters are wrong
    """
    if (find_by_code(student["code"]) == None and find_by_email(student["email"]) == None):        
        students.append(student)
    else:
        raise TypeError

def show_students(students):
    """
    Print a text with multiple students (one by line).    
    Args:
        data_text (str): Text wth student data 
    """
    for student in students:
        print(student)
        

def process_students(data_text):
    """
    Process a text with multiple students (one by line).
    
    Format for each line: "CODE|NAME|SURNAME|EMAIL"
    Example: "EST-1234|Joan|García López|joan@example.com"
    
    - Empty lines are ignored
    - Lines with errors are registered but no stop the proces
    - Return processed students with the errors
    
    Args:
        data_text (str): Text wth student data
        
    Returns:
        tuple: (student_list, errors_list)
            student_list: dictionary list with valid students
            errors_list: tuple (line_number, error)
    """
    # split data by line
    
    data = data_text.split('\n')
    students_list = []
    errors_list = ()
    
    # for each line
    counter = 1
    for line in data:
        # print("student", line)

        # check line is not empty
        try:
            if len(line) == 0:            
                raise ValueError
        except ValueError:
            errors_list = errors_list + ((counter, "Line student empty"),)
            counter += 1
            continue

        # split metadata by |
        values = line.split("|")

        # validate code
        try:
            validate_student_code(values[0])
        except ValueError:
            errors_list = errors_list + ((counter, "Invalid student code"),)
            counter += 1
            continue
        
        # validate name
        try:
            values[1] = validate_name(values[1])
            values[2] = validate_name(values[2])
        except ValueError:
            errors_list = errors_list + ((counter, "Invalid name"),)
            counter += 1
            continue
        
        # validate email
        try:
            validate_email(values[3])
        except ValueError:
            errors_list = errors_list + ((counter, "Invalid email"),)
            counter += 1
            continue
            
        # in case ok, add to dictionary
        student = create_student(values[0], values[1], values[2], values[3])
        students_list.append(student)
        counter += 1

    # print(students_list)
    # print(errors_list)
    return students_list, errors_list


# ============================================================================
# Step 3: Find and filter
# ============================================================================

def find_by_code(students, code):
    """
    Find a student by its code (case insensitive).
    
    Args:
        students (list): list of students
        code (str): code to find
        
    Returns:
        dict or None: Found student or None
    """
    for student in students:
        if student["code"] == code:
            return student
    return None


def find_by_email(students, email):
    """
    Find a student by its email
    
    Args:
        students (list): list of students
        email (str): email to find
        
    Returns:
        dict or None: Found student or None
    """
    for student in students:
        if student["email"] == email:
            return student
    return None

def find_by_text(students, text):
    """
    Find a student by its name, surname or email
    
    Args:
        students (list): list of students
        text (str): text to find
        
    Returns:
        list: found student list 
    """
    found_students =[]
    for student in students:
        if text in student["name"] or text in student["surname"] or text in student["email"]:
            found_students.append(student)
    return found_students


def filtrar_per_domini_email(llista_estudiants, domini):
    """
    Filtra estudiants que tinguin un email d'un domini específic.
    Exemple: domini="example.com" retorna estudiants amb "@example.com"
    
    Args:
        llista_estudiants (list): Llista d'estudiants
        domini (str): Domini a filtrar (sense @)
        
    Returns:
        list: Llista d'estudiants filtrats
    """
    # TODO: Implementa el filtratge
    pass


# ============================================================================
# ETAPA 4: GENERACIÓ D'INFORMES
# ============================================================================

def generar_informe_basic(llista_estudiants):
    """
    Genera un informe de text amb la informació de tots els estudiants.
    
    Format:
    ========================================
    INFORME D'ESTUDIANTS
    ========================================
    Total d'estudiants: X
    
    CODI      | NOM COMPLET           | EMAIL
    -----------------------------------------------
    EST-1234  | Joan García López     | joan@example.com
    ...
    
    Returns:
        str: L'informe formatat
    """
    # TODO: Implementa la generació de l'informe
    pass


def generar_estadistiques(llista_estudiants):
    """
    Genera estadístiques sobre els estudiants.
    
    Estadístiques a calcular:
    - Nombre total d'estudiants
    - Longitud mitjana dels noms complets
    - Domini de correu més comú
    - Llista de tots els dominis únics
    
    Returns:
        dict: Diccionari amb les estadístiques
    """
    # TODO: Implementa el càlcul d'estadístiques
    pass





# ============================================================================
# ETAPA 5: PROGRAMA PRINCIPAL AMB MENÚ INTERACTIU
# ============================================================================

def show_menu():
    """Mostra el menú d'opcions"""
    menu = """
    ==========================================
    SISTEMA DE GESTIÓ D'ESTUDIANTS
    ==========================================
    1. Afegir estudiant manualment
    2. Processar lot d'estudiants
    3. Buscar estudiant per codi
    4. Buscar estudiants per text
    5. Filtrar per domini d'email
    6. Mostrar tots els estudiants
    7. Generar informe
    8. Mostrar estadístiques
    0. Sortir
    ==========================================
    """
    print(menu)


def main_program():
    """
    Programa principal amb menú interactiu.
    Gestiona totes les operacions del sistema.
    """
    students = []
    # students, errors = process_students(TEST_DATA)
    
    print("Benvingut al Sistema de Gestió d'Estudiants!")
    
    while True:
        show_menu()
        
        try:
            option = input("Choose an option: ").strip()
            
            if option == "0":
                print("\nClosing system. Exit!")
                break
                
            elif option == "1":
                code = input("Give me code: ").strip()
                name = input("Give me name: ").strip()
                surname = input("Give me surname: ").strip()
                email = input("Give me an email: ").strip()
                students.append(create_student(code, name, surname, email))
                
            elif option == "2":# process default data
                students, errors = process_students(TEST_DATA)
                
            elif option == "3":# find a student by code
                code = input("Give me a code: ").strip()
                print(find_by_code(students, code))
                
            elif option == "4":# find a student by text in name, surname or email
                code = input("Give me a text: ").strip()
                show_students(find_by_text(students, code))
                
            elif option == "5":
                # TODO: Implementa el filtratge per domini
                pass
                
            elif option == "6":# show all students
                show_students(students)

            elif option == "7":
                # TODO: Genera i mostra l'informe
                pass
                
            elif option == "8":
                # TODO: Mostra estadístiques
                pass
                
            else:
                print("\nOpcio no valida. Tria un numero del 0 al 8.")
                
        except KeyboardInterrupt:
            print("\n\nInterrupció detectada. Sortint...")
            break
        except Exception as e:
            print(f"\n❌ Error inesperat: {e}")
            print("El programa continuarà executant-se.")


# ============================================================================
# DADES DE PROVA
# ============================================================================

TEST_DATA = """EST-1001|Maria|Fernández Garcia|maria.fernandez@example.com
EST-1002|Pere|Martínez López|pere.martinez@escola.cat

EST-1003|Anna|Sánchez Ruiz|anna.sanchez@example.com
EST-1004|Josep|García Pérez|josep.garcia@escola.cat
EST-1005|Laura|Rodríguez Torres|laura.rodriguez@gmail.com"""


# ============================================================================
# TESTS BÀSICS (per comprovar les teves funcions)
# ============================================================================

def executar_tests():
    """Executa tests bàsics per comprovar les funcions"""
    print("Executant tests...")
    
    # Test 1: Validació d'email
    print("\n--- Test 1: Validació d'email ---")
    try:
        assert validate_email("user@example.com") == True
        assert validate_email(" user@example.com") == False
        assert validate_email("invalid.email") == False
        assert validate_email("@example.com") == False
        print("[OK] Tests d'email passats")
    except Exception as e:
        print(f"✗ Error en tests d'email: {e}")
    
    # Test 2: Validació de nom
    print("\n--- Test 2: Validació de nom ---")
    try:
        nom = validate_name("  joan  ")
        assert nom == "Joan"
        print("[OK] Tests de nom passats")
    except Exception as e:
        print(f"[ERROR] Error en tests de nom: {e}")
    
    # Test 3: Validació de codi
    print("\n--- Test 3: Validació de codi ---")
    try:
        codi = validate_student_code("  est-1234  ")
        assert codi == "EST-1234"
        print("[OK] Tests de codi passats")
    except Exception as e:
        print(f"[ERROR] Error en tests de codi: {e}")
    
    # Test 4: Processament de lot
    print("\n--- Test 4: Processament de lot ---")
    try:
        students, errors = process_students(TEST_DATA)
        assert len(students) > 0
        print(f"[OK] Processats {len(students)} estudiants, {len(errors)} errors")
    except Exception as e:
        print(f"[ERROR] Error en processament de lot: {e}")


# ============================================================================
# PUNT D'ENTRADA
# ============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("EXERCICI INTEGRADOR: GESTIÓ D'ESTUDIANTS")
    print("=" * 60)
    print("\nAquest exercici té 5 etapes a completar.")
    print("Llegeix atentament cada funció i implementa el codi necessari.")
    print("\nOpcions:")
    print("1. Executar tests (executar_tests())")
    print("2. Executar programa principal (programa_principal())")
    print("=" * 60)
    
    # Uncomment line to be executed:
    # executar_tests()
    main_program()

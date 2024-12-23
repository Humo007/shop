import pymysql

class MYSQL:
    def __init__(self):
        self.ConnectDatabase()
        self.CreateDatabase()
        self.CreateTBStaff()



    def ConnectDatabase(self):
        self.database = pymysql.connect(
            user = "root",
            password = "1234",
            host = "localhost"
        ) 
        self.cur = self.database.cursor()

    def CreateDatabase(self):
        self.cur.execute("Create DATABASE IF NOT EXISTS Restaurant_Staff")
        self.cur.execute("Use Restaurant_Staff")  

    def CreateTBStaff(self):
        self.cur.execute("Drop table if exists staff")
        self.cur.execute('''Create Table if not exists Staff(
                         id int,
                         first_name varchar(50),
                         last_name varchar(50),
                         phone_number varchar(50),
                         job_id varchar(50),
                         salary int 
                         ) ''')
    
    def InsertTBStaff(self):
        self.cur.execute('''INSERT INTO STAFF(id, first_name, last_name, phone_number, job_id, salary) 
                         VALUES
                         (1, "Steven", "King", "+998941234580", "AD_PRES", 24000),
                         (2, "Neena", "Kochnar", "+998941244667", "AD_VP", 17000),
                         (3, "Lex", "De Haan", "+998941244689", "AD_VP", 17000),
                         (4, "Aleksandr", "Hunold", "+998941244677", "IT_PROG", 11000),
                         (5, "Bruce", "Ernest", "+998941244664", "IT_PROG", 8000),
                         (6, "David", "Austin", "+998941244862", "IT_PROG", 6800),
                         (7, "Valli", "Pataballa", "+998941244969", "IT_PROG", 6800),
                         (8, "Diana", "Lorentz", "+998946254967", "IT_PROG", 6200),
                         (9, "Nancy", "Greenberg", "+998946255932", "FI_MGR", 12000),
                         (10, "Daniel", "Faviet", "+998946756983", "FI_ACCOUNT", 9000),
                         (11, "John", "Chen", "+998946756905", "FI_ACCOUNT", 8200),
                         (12, "Ismeal", "Sciarra", "+998946856983", "FI_ACCOUNT", 7700),
                         (13, "Den", "Raphaely", "+998946886970", "PU_MAN", 11000),
                         (14, "Aleksandr", "Kahoo", "+998946888480", "PU_CLERK", 3100)
                         ''')
        self.database.commit()
    
    def Select_NameSurname(self):
        self.cur.execute("select first_name, last_name  from staff ")
        res = self.cur.fetchall()
        print(res)
        # for i in res:
        #     print(i)


    def Select_NameSurnameSalary(self):
        self.cur.execute("SELECT first_name, last_name, salary from staff where job_id = 'IT_PROG'")
        result = self.cur.fetchall()
        for i in result:
            print(i)

      
    def Select_JobidSalary(self):
        self.cur.execute("SELECT job_id, salary from staff where salary between 5000 and 20000 ")
        result = self.cur.fetchall()
        # print(result)
        for i in result:
          print(i)

    def Select_ALL(self):
        self.cur.execute("SELECT * from staff where phone_number LIKE '%6983' ")
        result = self.cur.fetchall()
        # print(result)
        for i in result:
          print(i)

    def Select_ALLTOTALsalary(self):
        self.cur.execute("SELECT SUM(salary) FROM staff  ")
        result = self.cur.fetchone()
        print(f"Jami maoshlar yig'indisi {result} ga teng!")


    def Select_ALLMAXsalary(self):
        self.cur.execute("SELECT * from staff WHERE job_id = 'IT_PROG' ORDER BY salary DESC limit 1")
        result = self.cur.fetchall()
        # print(result)
        for i in result:
          print(i)

    def Select_allMiddlesalary(self):
        self.cur.execute("SELECT * from staff WHERE salary > (SELECT SUM(salary) / COUNT(salary) from staff)")
        result = self.cur.fetchall()
        # print(result)
        for i in result:
          print(i)

    def Select_allMiddlesalaryJobid(self):
        self.cur.execute("SELECT * from staff WHERE salary > (SELECT SUM(salary) / COUNT(salary) from staff where job_id = 'IT_PROG')")
        result = self.cur.fetchall()
        # print(result)
        for i in result:
          print(i)
    def CloseConnection(self):
        self.database.close()
        print("Database ulanish yopildi!")


sql = MYSQL()
sql.CreateTBStaff()
sql.InsertTBStaff()
while True:
    print("1. 1-shart Ism va familiyalarni ko'rish.")
    print("2. 2-shart Job_id si 'IT_PROG' bo'lgan ishchilarning ismi, familiyasi va maoshini ko'rish.")
    print("3. 3-shart Maoshi 5000dan katta va 20000dan kichik bo'lgan ishchilarning job_id si va maoshlarini ko'rish")
    print("4. 4-shart Telefon naqamlarining oxori '6983' bo'lgan ishchilarning hamma ma'lumaotlarini ko'rish ")
    print("5. 5-shart Hamma ishchilarning maoshlari yig'indisini ko'rish.")
    print("6. 6-shart Job_id si 'IT_PROG' va Maoshi eng ko'p bo'lgan ishchini to'liq ma'lumaotlarini ko'rish.")
    print("7. 7-shart Ishchilarning o'rtacha maoshidan ko'p maosh oladigan ishchilarning hamma ma'lumaotlarini ko'rish.")
    print("8. 8-shart Job_id si 'IT_PROG' bo'lgan ishichlarning o'rtacha maoshidan katta bo'lgan ishchilarning hamma ma'lumotlarini ko'rish.")
    print("9. Database ni yopish.")
    choice = input("Tanlang: ")
    if choice == '1':
        sql.Select_NameSurname()
    elif choice == '2':
        sql.Select_NameSurnameSalary()
    elif choice == '3':
        sql.Select_JobidSalary()
    elif choice == '4':
        sql.Select_ALL()
    elif choice == '5':
        sql.Select_ALLTOTALsalary()
    elif choice == '6':
        sql.Select_ALLMAXsalary
    elif choice == '7':
        sql.Select_allMiddlesalary()
    elif choice == '8':
        sql.Select_allMiddlesalaryJobid() 
    elif choice == '9':
        sql.CloseConnection()
    else:
        print("Noto'g'ri tanladingiz!")                                   



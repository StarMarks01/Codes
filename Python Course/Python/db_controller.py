import mysql.connector as db
class DbController:
    host = "localhost"
    user = "yagneshDB"
    password = "Yagnesh@123"
    
    nameVar = None
    classVar = None
    phoneVar = None
    emailVar = None
    rollVar = None
    badmintonVar = None
    swimmingVar = None
    runningVar = None
    readingVar = None
    genderVar = None
    findVar = None
    year = None
    country = None
    
    years = [x for x in range(1950, 2024)]
    
    countries =['Afghanisthan', 'Albania', 'America', 'Dune', 
        'India', 'Indonesia', 'Japan', 'Mexico', 'New Gearsy',
        'Notrh Korea', 'Pakistan', 'South Korea', 'United Kingdom', 'Wano']
    
    def createDatabase(self):
        self.mydb = db.connect(
            host = self.host,
            user = self.user,
            password = self.password
        )
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS yagneshnewdatabase")
        
    def createTable(self):
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS yagneshnewdatabase.schooldata (name VARCHAR(100), class VARCHAR(100), phone VARCHAR(13), email VARCHAR(100), roll VARCHAR(100), hobbie VARCHAR(100), gender VARCHAR(100), year VARCHAR(100), country VARCHAR(100))")

    def addStudent(self):
        name = self.nameVar.get()
        classs = self.classVar.get()
        phone = self.phoneVar.get()
        email = self.emailVar.get()
        rollCall = self.rollVar.get()
        hobbiesTuple = ((self.badmintonVar,'Badminton'),
                    (self.swimmingVar,'Swimming'),
                    (self.runningVar,'Running'),
                    (self.readingVar,'Reading'))
        hobbie = [x[1] for x in hobbiesTuple if x[0].get()==1]
        gender = self.genderVar.get()
        birth_year = self.year.get()
        country = self.country.get()
        sql = "INSERT INTO yagneshnewdatabase.schooldata (name, class, phone, email, roll, hobbie, gender, year, country) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        value = (name, classs, phone, email ,rollCall, ','.join(str(x) for x in hobbie), gender, birth_year, country)
        self.mycursor.execute(sql, value)
        self.mydb.commit()
        
    def findStudent(self):
        studentName = self.findVar.get()
        sql = "SELECT * FROM yagneshnewdatabase.schooldata WHERE name = '{}'".format(studentName)
        self.mycursor.execute(sql)
        students = self.mycursor.fetchall()
        if len(students) !=0:
            self.nameVar.set(students[0][0])
            self.classVar.set(students[0][1])
            self.phoneVar.set(students[0][2])
            self.emailVar.set(students[0][3])
            self.rollVar.set(students[0][4])
            hb = list(students[0][5].split(','))
            if('Badminton' in hb): # Test Name
                self.badmintonVar.set(1)
            if('Swimming' in hb):
                self.swimmingVar.set(1)
            if('Running' in hb):
                self.runningVar.set(1)
            if('Reading' in hb):
                self.readingVar.set(1)
            self.genderVar.set(int(students[0][6]))
            self.year.set(students[0][7])
            self.country.set(students[0][8])
        else:
            print('No student found')

    def updateStudent(self):
        name = self.nameVar.get()
        classs = self.classVar.get()
        phone = self.phoneVar.get()
        email = self.emailVar.get()
        rollCall = self.rollVar.get()
        hobbiesTuple = ((self.badmintonVar,'Badminton'),
                    (self.swimmingVar,'Swimming'),
                    (self.runningVar,'Running'),
                    (self.readingVar,'Reading'))
        hobbie = [x[1] for x in hobbiesTuple if x[0].get()==1]
        gender = self.genderVar.get()
        birth_year = self.year.get()
        country = self.country.get()
        sql = "UPDATE yagneshnewdatabase.schooldata SET name = '{}', class = '{}', phone = '{}', roll = '{}', hobbie= '{}', gender= '{}', year= '{}', country= '{}' WHERE email = '{}'".format(name, classs, phone ,rollCall, ','.join(str(x) for x in hobbie), gender, birth_year, country, email)
        self.mycursor.execute(sql)
        self.mydb.commit()

    def deleteStudent(self):
        email = self.emailVar.get()
        sql = "DELETE FROM yagneshnewdatabase.schooldata WHERE email = '{}'".format(email)
        self.mycursor.execute(sql)
        self.mydb.commit()
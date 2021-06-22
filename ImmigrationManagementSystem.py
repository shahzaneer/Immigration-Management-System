import time
import emoji
import smtplib


# lists which are necessary for account creation

names = []
passwords = []
emails = []
country_user = []
city_user = []


# list which are optional for user for selection in his account

list_selected_region = []
list_selected_country = []
list_selected_city = []
list_selected_educational_institute = []
list_selected_appartment = []


# payment module of a user

immigration_fee = []
semester_fee = []
appartment_fee = []
payment = []

# initializing useful variables as  null

nm = ""
pas = ""
emil = ""
nam = ""
cou = ""


def account_creation(name, password, email, country, city):
    # sbse pehle jb account banega tou yeh 5 arguments darja zail lists me mehfooz hojayengay!

    names.append(name)
    passwords.append(password)
    emails.append(email)
    country_user.append(country)
    city_user.append(city)
    # yeh cheezain user khud select krega tou yeh optional hain isliay inki jagah k ta'ayyan ki khatir yahan null append krwadia

    list_selected_region.append("")
    list_selected_country.append("")
    list_selected_city.append("")
    list_selected_educational_institute.append("")
    list_selected_appartment.append("")
    immigration_fee.append(0)
    semester_fee.append(0)
    appartment_fee.append(0)
    payment.append(0)
    time.sleep(1)


def login_account():
    print()
    print("|-----------------------------------------|")
    print("|------------Login to Account-------------|")
    print("|-----------------------------------------|")
    print()

    emilin = ""
    pasin = ""

    emil_first = True
    pas_first = True

    while emilin not in emails:
        if emil_first == True:
            emilin = input("Enter your Email ").lower()
            emil_first = False
        else:
            print("Account Not Found ! Try again :")
            emilin = input("Enter your Email ").lower()

    account_index = emails.index(emilin)

    while pasin != passwords[account_index]:
        if pas_first:
            pasin = input(" Enter your Password :")
            pas_first = False
        else:
            print("Invalid Password, Try again :")
            pasin = input(" Enter your Password :")

    return account_index


def region(account_index):
    print("")
    print("|----------------------------|")
    print("|-------Select Region -------|")
    print("|----------------------------|")
    print("")

    list_region = ["Asia", "Africa", "North America", "South America", "Europe", "Austrailia", "New Zealandia"]

    options = [0, 1, 2, 3, 4, 5, 6]
    while True:
        print("""
        Enter the corresponding number to select the Region:
            0. Asia 
            1. Africa 
            2. North America
            3. South America
            4. Europe
            5. Austrailia
            6. New Zealandia         
            """)
        try:
            region = int(input("choose Region :"))
            if region in options:
                list_selected_region[account_index] = list_region[region]
                print(f"you selected {list_selected_region[account_index]}")
                time.sleep(1)
                break
            else:
                print("Enter Valid Command (choose from OnScreen options)")

        except ValueError:
            print("Please Enter the corresponding Number to select Region ")


def country(account_index):
    print("")
    print("|------------------------------------|")
    print("|-------Select Country / State ------|")
    print("|------------------------------------|")
    print("")

    list_countries = ["China", "Japan", "Turkey", "South Korea", "Ghana", "Sudan", "Egypt", "Morocco", "USA", "Mexico",
                      "Canada", "Panama", "Brazil", "Argentina", "Chile", "Columbia", "Germany", "UK", "Italy", "Spain",
                      "Queensland", "Victoria", "New South Wales", "Tasmania", "New Plymouth", "Nelson", "Catenbury",
                      "Otago"]

    optionc = []
    for i in range(28):
        optionc.append(i)
        pass

    while True:
        if list_selected_region[account_index] == "Asia":
            print(""""
                0. China
                1. Japan
                2. Turkey
                3. South Korea
                """)
        elif list_selected_region[account_index] == "Africa":

            print(""""
                 4. Ghana
                 5. Sudan
                 6. Egypt
                 7. Morocco
                """)
        elif list_selected_region[account_index] == "North America":

            print(""""
                8.   USA
                9.   Mexico
                10.  Canada
                11.  Panama
                """)
        elif list_selected_region[account_index] == "South America":

            print(""""
                12. Brazil
                13. Argentina
                14. Chile
                15. Columbia
                  """)
        elif list_selected_region[account_index] == "Europe":
            print("""
                16. Germany
                17. UK
                18. Italy
                19. Spain
                 """)
        elif list_selected_region[account_index] == "Austrailia":
            print("""" 
                20. Queensland
                21. Victoria
                22. New South Wales
                23. Tasmania
                """)
        elif list_selected_region[account_index] == "New Zealandia":
            print(""""
                24. New Plymouth
                25. Nelson
                26. Catenbury
                27. Otago 
                """)
        try:
            country = int(input("Choose Country :"))

            if country in optionc:
                list_selected_country[account_index] = list_countries[country]
                print(f"You Selected {list_selected_country[account_index]}")
                time.sleep(1)
                break
            else:
                print("Enter Valid Command (choose from OnScreen options)")

        except ValueError:
            print("Please Enter the corresponding Number to select Country")


def city(account_index):
    optionli = []

    print()
    print("|--------------------------------|")
    print("|---------Select City------------|")
    print("|--------------------------------|")
    print()

    list_city = ['Beijing', 'Shanghai', 'Senzhen', "tokyo",
                 "Kyuoto", "Osaka", "Istanbul", "Ankara", "Anatolia", "Seoul", "Busan", "Incheon", "Acra", "Kumasi",
                 "Tema",
                 "Khartoum", "Kassala", "Port Sudan", "Cairo", "Alexandria", "Luxor", "Fes", "Meknes", "Marrakesh",
                 "Washington"
        , "New York", "California", "Mexico City", "Cancun", "Puebla", "Toronto", "Calbary", "Vancouver", "Panama City",
                 "Tocumen",
                 "Colon", "Brasilia", "Sao Paulo", "Goiania", "La Plata", "Mendoza", "Cordoba", "Santiago",
                 "Valparaiso", "Arica", "Santa Marta", "Bogota", "Cali",
                 "Berlin", "Munich", "Hamburg", "London", "Manchester", "Birmingham", "Rome", "Venice", "Florence",
                 "Madrid", "Barcelona",
                 "Seville", "Brisbane", "Townsville", "Melbourne", "Geelong", "Sydney", "New Castle", "Dunedin",
                 "Queenstown"
        , "Govett-Brewster", "Puke Ariki", "Motueka", "Mapua", "Christchurch", "Timaru", "Auckland", "Wellington"]

    for i in range(76):
        optionli.append(i)
        pass

    while True:

        if list_selected_country[account_index] == "China":
            immigration_fee[account_index] += 500
            print("""
            immigration fee = 500 US dollar

            0. Beijing
            1. Shanghai
            2. Senzhen
            """)
        elif list_selected_country[account_index] == "Japan":
            immigration_fee[account_index] += 700
            print("""
            immigration fee = 700 US dollar

            3. tokyo
            4. Kyuoto
            5. Osaka
            """)
        elif list_selected_country[account_index] == "Turkey":
            immigration_fee[account_index] += 1500
            print("""
            immigration fee = 1500 US dollar

            6. Istanbul
            7. Ankara
            8. Anatolia
            """)
        elif list_selected_country[account_index] == "South Korea":
            immigration_fee[account_index] += 1700
            print("""
            immigration fee = 1700 US dollar

            9.  Seoul
            10. Busan
            11. Incheon
            """)
        elif list_selected_country[account_index] == "Ghana":
            immigration_fee[account_index] += 300
            print("""
            immigration fee = 300 US dollar
            12. Acra
            13. Kumasi
            14. Tema
            """)
        elif list_selected_country[account_index] == "Sudan":
            immigration_fee[account_index] += 200
            print("""
            immigration fee = 200 US dollar

            15. Khartoum
            16. Kassala
            17. Port Sudan
            """)
        elif list_selected_country[account_index] == "Egypt":
            immigration_fee[account_index] += 500
            print("""
            immigration fee = 500 US dollar

            18. Cairo
            19. Alexandria
            20. Luxor
            """)
        elif list_selected_country[account_index] == "Morocco":
            immigration_fee[account_index] += 500
            print("""
            immigration fee = 500 US dollar

            21. Fes
            22. Meknes
            23. Marrakesh
            """)
        elif list_selected_country[account_index] == "USA":
            immigration_fee[account_index] += 2500
            print("""
            immigration fee = 2500 US dollar

            24. Washington
            25. New York
            26. California
            """)
        elif list_selected_country[account_index] == "Mexico":
            immigration_fee[account_index] += 1000
            print("""
            immigration fee = 1000 US dollar

            27. Mexico City
            28. Cancun
            29. Puebla
            """)
        elif list_selected_country[account_index] == "Canada":
            immigration_fee[account_index] += 1500
            print("""
            immigration fee = 1500 US dollar
            30. Toronto
            31. Calbary
            32. Vancouver
            """)
        elif list_selected_country[account_index] == "Panama":
            immigration_fee[account_index] += 1600
            print("""
            immigration fee = 1600 US dollar
            33. Panama City
            34. Tocumen
            35. Colon
            """)
        elif list_selected_country[account_index] == "Brazil":
            immigration_fee[account_index] += 1000
            print("""
            immigration fee = 1000 US dollar

            36. Brasilia
            37. Sao Paulo
            38. Goiania
            """)
        elif list_selected_country[account_index] == "Argentina":
            immigration_fee[account_index] += 1600
            print("""
            immigration fee = 1600 US dollar

            39. La Plata
            40. Mendoza
            41. Cordoba
            """)
        elif list_selected_country[account_index] == "Chile":
            immigration_fee[account_index] += 1700
            print("""
            immigration fee = 1700 US dollar

            42. Santiago
            43. Valparaiso
            44. Arica
            """)
        elif list_selected_country[account_index] == "Columbia":
            immigration_fee[account_index] += 1500
            print("""
            immigration fee = 1500 US dollar

            45. Santa Marta
            46. Bogota
            47. Cali
            """)
        elif list_selected_country[account_index] == "Germany":
            immigration_fee[account_index] += 1200
            print("""
            immigration fee = 1200 US dollar

            48. Berlin
            49. Munich
            50. Hamburg
            """)
        elif list_selected_country[account_index] == "UK":
            immigration_fee[account_index] += 2100
            print("""
            immigration fee = 2100 US dollar

            51. London
            52. Manchester
            53. Birmingham
            """)
        elif list_selected_country[account_index] == "Italy":
            immigration_fee[account_index] += 1000
            print("""
            immigration fee = 1000 US dollar

            54. Rome
            55. Venice
            56. Florence
            """)
        elif list_selected_country[account_index] == "Spain":
            immigration_fee[account_index] += 1100
            print("""
            immigration fee = 1100 US dollar

            57. Madrid
            58. Barcelona
            59. Seville
            """)
        elif list_selected_country[account_index] == "Queensland":
            immigration_fee[account_index] += 1700
            print("""
            immigration fee = 1700 US dollar

            60. Brisbane
            61. Townsville
            """)
        elif list_selected_country[account_index] == "Victoria":
            immigration_fee[account_index] += 1500
            print("""
            immigration fee = 1500 US dollar

            62. Melbourne
            63. Geelong
            """)
        elif list_selected_country[account_index] == "New South Wales":
            immigration_fee[account_index] += 1450
            print("""
            immigration fee = 1450 US dollar

            64. Sydney
            65. New Castle

            """)
        elif list_selected_country[account_index] == "Tasmania":
            immigration_fee[account_index] += 1200
            print("""
            immigration fee = 1200 US dollar

            66. Dunedin
            67. Queenstown
            """)
        elif list_selected_country[account_index] == "New Plymouth":
            immigration_fee[account_index] += 1800
            print("""
            immigration fee = 1800 US dollar

            68. Govett-Brewster
            69. Puke Ariki
            """)
        elif list_selected_country[account_index] == "Nelson":
            immigration_fee[account_index] += 1900
            print("""
            immigration fee = 1900 US dollar

            70. Motueka
            71. Mapua

            """)
        elif list_selected_country[account_index] == "Catenbury":
            immigration_fee[account_index] += 1250
            print("""
            immigration fee = 1250 US dollar

            72. Christchurch
            73. Timaru
            """)
        elif list_selected_country[account_index] == "Otago":
            immigration_fee[account_index] += 1700
            print("""
            immigration fee = 1700 US dollar

            74. Auckland
            75. Wellington
            """)

        try:
            city = int(input("Choose City :"))
            if city in optionli:
                list_selected_city[account_index] = list_city[city]
                print(f"you selected {list_selected_city[account_index]}")
                time.sleep(1)
                break
            else:
                print("Invalid Command !(choose from OnScreen options) ")

        except ValueError:
            print("Please Enter the corresponding Number to select City ")


def educational_institutes(account_index):
    optionl = []

    print("")
    print("|--------------------------------|")
    print("|--Select Educational institute--|")
    print("|--------------------------------|")
    print("")

    list_educationali_institutes = ['Tsinghua University', 'Peking University', 'Fudan University',
                                    'University of Tokyo', 'Kyoto University',
                                    'Osaka University', 'Koc University', 'sabaniu University', 'Istanbul University',
                                    'KAIST', 'National University of Seoul',
                                    'Korea University', 'The University of Ghana',
                                    'Kwame Nkrumah University of Science and Technology', 'University of Cape Coast',
                                    'National University Sudan', 'sudan University of Science and technology',
                                    'University of Khartoum', 'Cairo University', 'Al azhar University',
                                    'Misar University of Science and Technology', 'Al-Abhawayn University',
                                    'Mohammed VI university of health Sciences',
                                    'International Institute for higher education in morocco',
                                    'Harvard university', 'Stanford University',
                                    'Massachusett Institute of Technology (MIT)', 'Instituto Nacional Autonoma',
                                    'Universidad Politecno Nacional', 'Tecnologico de Monterrey (ITESM)',
                                    'University of Toronto', 'McGill University', "Queen's University ",
                                    'Universidad  Tecnologica de Panama', 'Universidad de panama',
                                    'Columbus University', 'Universidade de Brasilia', 'Universidade Estadual paulista',
                                    'Universidade de Sao Paulo (USP',
                                    'Instituto Technologico de Buenos Aires (TIBA)', 'Universidad Austral',
                                    'Universidad Palermo', 'University of Desarrollo', 'Austral university of Chile',
                                    'University of Atscama', 'Universidad Nacional de Colombia',
                                    'Universidad de Antioquia', 'Pontificia Universidad Javeriana',
                                    'Technische Nacional Munchen', 'Freie Universitat Berlin',
                                    'Ludwig-Maximillians-Universitat', 'University of Oxford',
                                    'University of Cambridge',
                                    'Imperial College London', 'Sapienza-universita di Roma', 'Universita di Bologna',
                                    'Politecnico di Milano', 'University of Barcelona',
                                    'Complutense University of Madrid', 'University of Navarra',
                                    'Austrailian National University', 'University of Queensland',
                                    'Monash University', 'University of Auckland', 'Victoria University of Wellington',
                                    'University of Catenbury']

    for i in range(66):
        optionl.append(i)
        pass

    while True:

        if list_selected_country[account_index] == "China":
            semester_fee[account_index] += 500

            print("""
            average fee per Semester = 500 US Dollars

            0. Tsinghua University
            1. Peking University
            2. Fudan University
            """)
        elif list_selected_country[account_index] == "Japan":
            semester_fee[account_index] += 300
            print("""
            average fee per Semester = 300 US Dollars

            3. University of Tokyo
            4. Kyoto University
            5. Osaka University
            """)
        elif list_selected_country[account_index] == "Turkey":
            semester_fee[account_index] += 1500
            print("""
            average fee per Semester = 1500 US dollars

              6. Koc University
              7. sabaniu University
              8. Istanbul University
            """)
        elif list_selected_country[account_index] == "South Korea":
            semester_fee[account_index] += 500
            print("""
            average fee per Semester = 500

            9.  KAIST
            10. National University of Seoul
            11. Korea University
            """)
        elif list_selected_country[account_index] == "Ghana":
            semester_fee[account_index] += 1200
            print("""
            average fee per Semester = 1200

            12. The University of Ghana
            13. Kwame Nkrumah University of Science and Technology
            14. University of Cape Coast
            """)
        elif list_selected_country[account_index] == "Sudan":
            semester_fee[account_index] += 400
            print("""
            average fee per Semester = 400 US Dollars 

            15. National University Sudan
            16. sudan University of Science and technology
            17. University of Khartoum
            """)
        elif list_selected_country[account_index] == "Egypt":
            semester_fee[account_index] += 600
            print("""
            average fee per Semester = 600 US Dollars

            18. Cairo University
            19. Al azhar University
            20. Misar University of Science and Technology
            """)
        elif list_selected_country[account_index] == "Morocco":
            semester_fee[account_index] += 600
            print("""
            average fee per Semester = 600 US Dollars

            21. Al-Abhawayn University
            22. Mohammed VI university of health Sciences
            23. International Institute for higher education in morocco
            """)
        elif list_selected_country[account_index] == "USA":
            semester_fee[account_index] += 1500
            print("""
            average fee per Semester = 1500 US Dollars

            24. Harvard university
            25. Stanford University
            26. Massachusett Institute of Technology (MIT)
            """)
        elif list_selected_country[account_index] == "Mexico":
            semester_fee[account_index] += 1000
            print("""
            average fee per Semester = 1000 US Dollars

            27. Instituto Nacional Autonoma
            28. Universidad Politecno Nacional
            29. Tecnologico de Monterrey (ITESM)
            """)
        elif list_selected_country[account_index] == "Canada":
            semester_fee[account_index] += 1500
            print("""
            average fee per Semester = 1500 US Dollars

            30. University of Toronto
            31. McGill University
            32. Queen's University 
            """)
        elif list_selected_country[account_index] == "Panama":
            semester_fee[account_index] += 500
            print("""
            average fee per Semester = 500 US Dollars

            33. Universidad  Tecnologica de Panama
            34. Universidad de panama
            35. Columbus University
            """)
        elif list_selected_country[account_index] == "Brazil":
            semester_fee[account_index] += 700
            print("""
            average fee per Semester = 700 US Dollars

            36. Universidade de Brasilia
            37. Universidade Estadual paulista
            38. Universidade de Sao Paulo (USP
            """)
        elif list_selected_country[account_index] == "Argentina":
            semester_fee[account_index] += 500
            print("""
            average fee per Semester = 500 US Dollars

            39. Instituto Technologico de Buenos Aires (TIBA)
            40. Universidad Austral
            41. Universidad Palermo
            """)
        elif list_selected_country[account_index] == "Chile":
            semester_fee[account_index] += 750
            print("""
            average fee per Semester = 750 US Dollars

            42. University of Desarrollo
            43. Austral university of Chile
            44. University of Atscama
            """)
        elif list_selected_country[account_index] == "Columbia":
            semester_fee[account_index] += 900
            print("""
            average fee per Semester = 900 US Dollars

            45. Universidad Nacional de Colombia
            46. Universidad de Antioquia
            47. Pontificia Universidad Javeriana
            """)
        elif list_selected_country[account_index] == "Germany":
            semester_fee[account_index] += 200
            print("""
            average fee per Semester = 200 US Dollars

            48. Technische Nacional Munchen
            49. Freie Universitat Berlin
            50. Ludwig-Maximillians-Universitat
            """)
        elif list_selected_country[account_index] == "UK":
            semester_fee[account_index] += 2500
            print("""
            average fee per Semester = 2500 US Dollars

            51. University of Oxford
            52. University of Cambridge
            53. Imperial College London
            """)
        elif list_selected_country[account_index] == "Italy":
            semester_fee[account_index] += 500
            print("""
            average fee per Semester = 500 US Dollars

            54. Sapienza-universita di Roma
            55. Universita di Bologna
            56. Politecnico di Milano
            """)
        elif list_selected_country[account_index] == "Spain":
            semester_fee[account_index] += 600
            print("""
            average fee per Semester = 600 US Dollars

            57. University of Barcelona
            58. Complutense University of Madrid
            59. University of Navarra
            """)
        elif list_selected_country[account_index] == "Queensland" or list_selected_country[
            account_index] == "Victoria" or list_selected_country[account_index] == "New South Wales" or \
                list_selected_country[account_index] == "Tasmania":
            semester_fee[account_index] += 1200
            print("""
            average fee per Semester = 1200 US Dollars

            60. Austrailian National University
            61. University of Queensland
            62. Monash University
            """)
        elif list_selected_country[account_index] == "New Plymouth" or list_selected_country[
            account_index] == "Nelson" or list_selected_country[account_index] == "Catenbury" or list_selected_country[
            account_index] == "Otago":
            semester_fee[account_index] += 1500
            print("""
            average fee per Semester = 1500 US Dollars

            63. University of Auckland
            64. Victoria University of Wellington
            65. University of Catenbury
            """)
        try:
            eduinstitute = int(input("Choose Educational Institute :"))

            if eduinstitute in optionl:
                list_selected_educational_institute[account_index] = list_educationali_institutes[eduinstitute]
                print(f"You Selected {list_selected_educational_institute[account_index]} !")
                time.sleep(1)
                break
            else:
                print("Invalid Command! (choose from OnScreen options) ")

        except ValueError:
            print("Please Enter the corresponding Number to select Education Institute")


def appartment(account_index):
    print()
    print("|----------------------------|")
    print("|---Select Appartment Type---|")
    print("|----------------------------|")
    print()

    while True:
        list_appartment = ["Single storey -- normal", "Double story -- classic", "triple storey--Luxury "]
        optiona = [0, 1, 2]

        print(""""
              0. Single storey -- Normal --  500$
              1. Double story -- Classic -- 1000$
              2. triple storey-- Luxury --  1500$
            """)

        try:
            appart = int(input("Enter command to select Appartment !"))

            if appart == 0:
                appartment_fee[account_index] += 500
            elif appart == 1:
                appartment_fee[account_index] += 1000
            elif appart == 2:
                appartment_fee[account_index] += 1500
            else:
                pass

            if appart in optiona:
                list_selected_appartment[account_index] = list_appartment[appart]
                print(f"you selected {list_selected_appartment[account_index]} type Appartment with fee {appartment_fee[account_index]} US Dollars")
                time.sleep(1)
                break
            else:
                print("Enter Valid Command please:  (choose from 0 ,1, 2 )")

        except ValueError:
            print("Please Enter the corresponding Number to select the Appartment type")


def report_generation(account_index):
    print()
    print("|-----------------------------------------|")
    print("|------------Report Generation------------|")
    print("|-----------------------------------------|")
    print()
    # taking the sum of payment module .
    payment[account_index] = semester_fee[account_index] + immigration_fee[account_index] + appartment_fee[
        account_index]

    print(f"""
    |---------------------RaviCom Immigration Services (Pvt.)--------------------------|

    |----------------------------Candidate's Profile-----------------------------------|

      Name                 : {names[account_index]}                                    
      Country              : {country_user[account_index]}                             
      City                 : {city_user[account_index]}                                
    |----------------------------------------------------------------------------------|

    |----------------------------Candidate's Details for Immigration-------------------|

      Region               : {list_selected_region[account_index]}                     
      Country/State        : {list_selected_country[account_index]}                    
      City                 : {list_selected_city[account_index]}                       
      Appartment Type      : {list_selected_appartment[account_index]}                 
      Education Institute  : {list_selected_educational_institute[account_index]}  

    | ---------------------------------------------------------------------------------|

    |----------------------------Expenses Info-----------------------------------------|

      Immigration Fee      : {immigration_fee[account_index]} US Dollars                    
      Average Semester Fee : {semester_fee[account_index]} US Dollars               
      Appartment fee       : {appartment_fee[account_index]} US Dollars                         

    |----------------------------------------------------------------------------------|

    |---------------------------Total Payment Estimation-------------------------------|

      Payment               : {payment[account_index]} US Dollars                                
    | ---------------------------------------------------------------------------------|
    """)
    time.sleep(5)


def update_info(account_index):
    print("")
    print("|--------------------------------|")
    print("|---------Update Info------------|")
    print("|--------------------------------|")
    print("")
    time.sleep(1)

    # # again setting the optional lists to empty strings so that we can update them again !

    list_selected_region[account_index] = ""
    list_selected_country[account_index] = ""
    list_selected_city[account_index] = ""
    list_selected_appartment[account_index] = ""
    list_selected_educational_institute[account_index] = ""

    immigration_fee[account_index] = 0
    semester_fee[account_index] = 0
    appartment_fee[account_index] = 0
    payment[account_index] = 0

    print("Enter 1 to select Region again :")
    time.sleep(1)


def delete_account(account_index):
    print("")
    print("|--------------------------------|")
    print("|--Deleting Acoount Permanently--|")
    print("|--------------------------------|")
    print("")

    # it will delete the information of each list at that index i.e account index

    names.pop(account_index)
    passwords.pop(account_index)
    emails.pop(account_index)
    country_user.pop(account_index)
    city_user.pop(account_index)
    list_selected_region.pop(account_index)
    list_selected_country.pop(account_index)
    list_selected_city.pop(account_index)
    list_selected_appartment.pop(account_index)
    list_selected_educational_institute.pop(account_index)
    immigration_fee.pop(account_index)
    semester_fee.pop(account_index)
    appartment_fee.pop(account_index)
    payment.pop(account_index)
    time.sleep(2)

    print("Your account have been deleted successfully!")


def email_my_details(account_index):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("shahism01@gmail.com", "vdacuytsomkulknh")
        msg = f"""

    |---------------------RaviCom Immigration Services (Pvt.)--------------------------|

    |----------------------------Candidate's Profile-----------------------------------|

      Name                 : {names[account_index]}                                    
      Country              : {country_user[account_index]}                             
      City                 : {city_user[account_index]}                                
    |----------------------------------------------------------------------------------|

    |----------------------------Candidate's Details for Immigration-------------------|

      Region               : {list_selected_region[account_index]}                     
      Country/State        : {list_selected_country[account_index]}                    
      City                 : {list_selected_city[account_index]}                       
      Appartment Type      : {list_selected_appartment[account_index]}                 
      Education Institute  : {list_selected_educational_institute[account_index]}  

    | ---------------------------------------------------------------------------------|

    |----------------------------Expenses Info-----------------------------------------|

      Immigration Fee      : {immigration_fee[account_index]} US Dollars                    
      Average Semester Fee : {semester_fee[account_index]} US Dollars               
      Appartment fee       : {appartment_fee[account_index]} US Dollars                         

    |----------------------------------------------------------------------------------|

    |---------------------------Total Payment Estimation-------------------------------|

      Payment               : {payment[account_index]} US Dollars                                
    | ---------------------------------------------------------------------------------|
    
    Thank you for using the IMS by Ravicom.
    """

        subject = "RaviCom Immigration Management System"
        body = "subject: {}\n\n{}".format(subject, msg)

        server.sendmail(f"shahism01@gmail.com", f"{emails[account_index]}", body)

        server.quit()
        print("your details have been emailed successfully!")

    except Exception as f:
        print("Please try again ! we found a connectivity issue !")

    finally:
        print("Regards, RaviCom Immigration (pvt.) ")


def main():
    print()
    print("|-----------------------------------------|")
    print("|------Immigration Management System------|")
    print("|-----------------------------------------|")
    print()

    print("Welcome to the Immigration Management System !")
    print("Please follow the onScreen commands to use the System ", emoji.emojize(":grinning_face_with_big_eyes:"))

    login = False
    while True:
        if login == False:
            print("""
                Enter the corresponding Number to select the option :
                1. Create Account
                2.  Login
                3. Exit

                """)
            try:
                command = int(input("Enter Command :"))
                if command == 1:
                    print()
                    print("|-----------------------------------------|")
                    print("|----------Account Creation---------------|")
                    print("|-----------------------------------------|")
                    print()
                    name = False
                    while True:
                        nm = input(" what's your good name? It should not include numbers or special characters !:").lower()
                        if len(nm) >= 3:
                            nam = nm.replace(" ", "x")
                            if nam.isalpha():
                                nm = nam.replace("x", " ")
                                name = True
                        if name:
                            break
                        else:
                            print("Please Enter Valid Name !")

                    email1 = False
                    while True:
                        emil = input(" Set your Valid Email Address :").lower()
                        if emil in emails: #to check that no accounts should have the same email adress
                            print("This email already exists in our database!")
                            continue
                        if "." in emil:
                            if "com" or "org" or "co" in emil:
                                if "@" in emil:
                                    if " " not in emil:
                                        email1 = True
                        if email1:
                            break
                        else:
                            print("Incorrect Email format!!")

                    pass1 = False
                    while True:
                        pas = input("  Set your Password : It should have 6 or more characters and alphanumeric :")
                        if len(pas) >= 6:
                            alpha_count = 0
                            numeric_count = 0
                            for i in pas:
                                if i.isalpha():
                                    alpha_count += 1
                                elif i.isnumeric():
                                    numeric_count += 1
                            if alpha_count >= 1 and numeric_count >= 1:
                                pass1 = True
                        if pass1:
                            break
                        else:
                            print("Please set a valid Password !")

                    countryy = False
                    while True:
                        coun = input(" Enter Your Country :").lower()
                        if len(coun) > 3:
                            if coun.isalpha():
                                countryy = True
                        if countryy:
                            break
                        else:
                            print("Invalid Country Name !")
                    cityy = False
                    while True:
                        cit = input(" Enter your City :").lower()
                        if len(cit) > 3:
                            if cit.isalpha():
                                cityy = True
                        if cityy:
                            break
                        else:
                            print("Invalid City Name !")
                    print("----------we are creating your account-----------")
                    account_creation(nm.title(), pas, emil, coun.title(), cit.title())

                    print("---Your Account has been created Successfully!----")


                elif command == 2:

                    if len(emails) == 0:
                        print("Please Create your account first !")
                        time.sleep(1)
                        continue

                    
                    account_index = login_account()

                    print("you have successfully logged in !")
                    time.sleep(2)
                    login = True



                elif command == 3:
                    print("")
                    print("|--------------------------------|")
                    print("|--------------Exit--------------|")
                    print("|--------------------------------|")
                    print("")
                    print("------Immigration Management System is exiting ------")
                    time.sleep(2)
                    print("----------Thank you for using IMS by RaviCom (pvt). ")
                    exit()

                else:
                    print("Invalid Command! please follow onScreen commands to use the System! ")

            except ValueError:
                print("Please Enter the corresponding Number to choose that option")

        elif login:
            print("""
                Enter the corresponding Number to select the option :
                1.  Select Region
                2.  Select Country/State
                3.  Select City
                4.  Select Appartment type
                5.  Select Educational Institute
                6.  Report Generation
                7.  Update Info
                8.  Account Deletion
                9.  Email details
                10.  Logout

                """)
            try:
                command_main = int(input("Enter :"))

                if command_main == 1:
                    if list_selected_region[account_index] != "":
                        print(" Enter 7 to update Region ")
                        time.sleep(1)
                        continue

                    region(account_index)

                elif command_main == 2:

                    if list_selected_region[account_index] == "":
                        print("Please Select Region first !")
                        time.sleep(1)
                        continue
                    else:
                        pass

                    if list_selected_country[account_index] != "":
                        print(f" you have selected country/state {list_selected_country[account_index]} if you want to update info Enter 7  ")
                        time.sleep(1)
                        continue

                    country(account_index)

                elif command_main == 3:
                    if list_selected_region[account_index] == "":
                        print("Please select region first !")
                        time.sleep(1)
                        continue
                    if list_selected_country[account_index] == "":
                        print("Please select country first !")
                        time.sleep(1)
                        continue

                    if list_selected_city[account_index] != "":
                        print(f" you have selected City {list_selected_city[account_index]} if you want to update info Enter 7  ")
                        time.sleep(1)
                        continue

                    city(account_index)

                elif command_main == 4:
                    if list_selected_region[account_index] == "":
                        print("Please select region first !")
                        time.sleep(1)
                        continue
                    if list_selected_country[account_index] == "":
                        print("Please select country first !")
                        time.sleep(1)
                        continue
                    if list_selected_city[account_index] == "":
                        print("please select the city first !")
                        time.sleep(1)
                        continue
                    if list_selected_appartment[account_index] != "":
                        print(f" you have selected appartment {list_selected_appartment[account_index]} if you want to update info Enter 7  ")
                        time.sleep(1)
                        continue

                    appartment(account_index)
                elif command_main == 5:

                    if list_selected_region[account_index] == "":
                        print("Please select region first !")
                        time.sleep(1)
                        continue
                    if list_selected_country[account_index] == "":
                        print("Please select country first !")
                        time.sleep(1)
                        continue
                    if list_selected_city[account_index] == "":
                        print("please select the city first !")
                        time.sleep(1)
                        continue
                    if list_selected_appartment[account_index] == "":
                        print("Please select the appartment first !")
                        time.sleep(1)
                        continue

                    if list_selected_educational_institute[account_index] != "":
                        print(f" you have selected University '{list_selected_educational_institute[account_index]}' if you want to update info Enter 7 ")
                        time.sleep(1)
                        continue

                    educational_institutes(account_index)
                elif command_main == 6:

                    if list_selected_region[account_index] == "":
                        print("Please select region first !")
                        time.sleep(1)
                        continue
                    if list_selected_country[account_index] == "":
                        print("Please select country first !")
                        time.sleep(1)
                        continue
                    if list_selected_city[account_index] == "":
                        print("please select the city first !")
                        time.sleep(1)
                        continue
                    if list_selected_appartment[account_index] == "":
                        print("Please select the appartment first !")
                        time.sleep(1)
                        continue
                    if list_selected_educational_institute[account_index] == "":
                        print("Please select the educational institute first !")
                        time.sleep(1)
                        continue

                    report_generation(account_index)

                elif command_main == 7:

                    update_info(account_index)

                elif command_main == 8:
                    delete_account(account_index)
                    login = False
                elif command_main==9:
                    if list_selected_region[account_index] == "":
                        print("Please select region first !")
                        time.sleep(1)
                        continue
                    if list_selected_country[account_index] == "":
                        print("Please select country first !")
                        time.sleep(1)
                        continue
                    if list_selected_city[account_index] == "":
                        print("please select the city first !")
                        time.sleep(1)
                        continue
                    if list_selected_appartment[account_index] == "":
                        print("Please select the appartment first !")
                        time.sleep(1)
                        continue
                    if list_selected_educational_institute[account_index] == "":
                        print("Please select the educational institute first !")
                        time.sleep(1)
                        continue


                    print()
                    print("|-----------------------------------------|")
                    print("|-----------Sending Email-----------------|")
                    print("|-----------------------------------------|")
                    print("We are sending email it may take a moment :-)")
                    print()
                    email_my_details(account_index)

                elif command_main == 10:
                    print()
                    print("|-----------------------------------------|")
                    print("|-----------Logging out-------------------|")
                    print("|-----------------------------------------|")
                    print()
                    time.sleep(2)
                    print("You have successfully logged out !")
                    login = False

                else:
                    print("Invalid Command! ")
            except ValueError:
                print("Please Enter the corresponding Number to select ")


main()






import os

class Main:
    
    def parser(self):
        #_id,index,dataEMD,nome/primeiro,nome/último,idade,género,morada,modalidade,clube,email,federado,resultado
        
        script_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_directory, '..', 'Data', 'emd.csv')
        full_path = os.path.abspath(file_path)
        
        athletes = []

        try:
            # encoding para não desformatar
            with open(full_path, 'r', encoding='utf-8') as data:
                data.readline()
                for line in data:
                    #strip para limpar a string se nao o parse do ultimo elemento nao regista "true" mas sim "true\n"
                    split = line.strip().split(',')
                    athlete = {
                        "id":split[0],
                        "index":split[1],
                        "dataEMD":split[2],
                        "nome":split[3],
                        "idade":split[5],
                        "genero":split[6],
                        "morada":split[7],
                        "modalidade":split[8],
                        "clube":split[9],
                        "email":split[10],
                        "federado":split[11],
                        "resultado":split[12]
                    }
                    athletes.append(athlete)
        except FileNotFoundError:
            print(f"File not found: {full_path}")
            
        return athletes
    
    
    def menuPrint(self):
        print("")
        print("1. Sorted List with all sports")
        print("2. Percentage of apt and inapt athletes")
        print("3. Athletes per age rating")
        print("0. Exit")
        user_choice = input("Choose an option: ")
        return user_choice


    def sortSport(self, athletes):
        sports = []
        for athlete in athletes:
            if athlete["modalidade"] in sports:
                pass
            else:
                sports.append(athlete["modalidade"])
                
        sports.sort()
        return sports
    
    def aptAthletes(self, athletes):
        apt = []
        total = []
        for athlete in athletes:
            if (athlete["resultado"] == "true"):
                apt.append(athlete)
                total.append(athlete)
            else:
                total.append(athlete)
        percentage = (len(apt) / len(total)) * 100;
        return percentage
                

    def ageDistribution(self, athletes):
        total = []
        range1 = []
        range2 = []
        range3 = []
        range4 = []
        range5 = []
        distList = []
        
        for athlete in athletes:
            total.append(athlete)
            idade = athlete["idade"]
            idade = int(idade)
            if 20 <= idade <= 24:
                range1.append(athlete)
            elif 25 <= idade <= 29:
                range2.append(athlete)
            elif 30 <= idade <= 34:
                range3.append(athlete)
            elif 35 <= idade <= 39:
                range4.append(athlete)
                
        dist1 = len(range1) / len(total)
        distList.append(round(dist1, 2))
        dist2 = len(range2) / len(total)
        distList.append(round(dist2, 2))
        dist3 = len(range3) / len(total)
        distList.append(round(dist3, 2))
        dist4 = len(range4) / len(total)
        distList.append(round(dist4, 2))
        return distList

            
        
                    
    def main_loop(self, athletes):
        while True:
            user_choice = self.menuPrint()
            
            if user_choice == '1':
                # Lista ordenada alfabeticamente das modalidades desportivas;
                sports = self.sortSport(athletes)
                print("The sports are: " + sports)
                pass
            elif user_choice == '2':
                # Percentagens de atletas aptos e inaptos para a prática desportiva;
                percentage = self.aptAthletes(athletes)
                print()
                print("The percentage of apt athletes is " + str(percentage) + "%")
                pass
            elif user_choice == '3':
                # Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...
                dist = self.ageDistribution(athletes)
                print()
                print("The percentage of athletes between 20 and 24 years is " + str(dist[0]) + "%")
                print("The percentage of athletes between 25 and 29 years is " + str(dist[1]) + "%")
                print("The percentage of athletes between 30 and 34 years is " + str(dist[2]) + "%")
                print("The percentage of athletes between 35 and 39 years is " + str(dist[3]) + "%")
                pass
            elif user_choice == '0':
                break
            else:
                print(" ")
                print("Invalid option:", user_choice)

    def __init__(self):
        athletes = self.parser()
        self.main_loop(athletes)



main_instance = Main()
            
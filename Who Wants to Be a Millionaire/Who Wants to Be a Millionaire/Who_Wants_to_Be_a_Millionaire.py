import random
import time
import os
print("\t<<MİLYONÇU>>\n")
time.sleep(2)
os.system('cls')
question = [["Irlandiyanin paytaxtı hansıdır?"],
          ['Nağaranın başqa sözlə adı?'],
          ['Ömründə bir dəfə olsa da çiçək açan bitkilərə nə ad verilir?'],
          ['Hansı ölkə piramidaları ilə məşhurdur?'],
          ['Ən az sahəsi olan materik?'],
          ['Hansi daxili planetlərə daxil deyil?'],
          ['Azərbaycan gəmiləri hansı çay vasitəsilə dünya okeanına çıxır?'],
          ['Dünyada sahəsinə görə ən böyük ölkə hansıdır?'],
          ['Bunlardan hansı Venesuelanın prezidenti olub?'],
          ['Türkiyənin milli pul vahidi hansıdır?'],
          ['Əhalinin 60%-i şəhərdə yaşayır,əvvəlki paytaxtı Alma-Ata olub?'],
          ['Tibbin hansı bölməsi ürək-damar xəstəlikləri ilə məşğul olur?'],
          ['Norveçin paytaxtı hansıdır?'],
          ['Beynəlxalq Sistemdə zaman vahidi kimi qəbul edilmişdir:']]
money = ['500'],['1.000'],['2.000'],['3.000'],['5.000'],['7.500'],['15.000'],['30.000'],['60.000'],['125.000'],['250.000']
answer = [[["Dublin"],["Galway"],["Liverpool"],["Cork"]],
        [['Dumbul'],['Künəlgə'],['Tar'],['Saz']],
        [['Çiçəkli Bitkilər'],['Kök'],['Gövdə'],['Tumurcuq']],
        [['Misir'],['Şirvanşahlar'],['Səfəvilər'],['Mesopotamiya']],
        [['Avstraliya'],['Şimali Amerika'],['Cənubi Amerika'],['Antarktida']],
        [['Yupiter'],['Mars'],['Merkuri'],['Venera']],
        [['Volqa'],['Araz'],['Ural'],['Kür']],
        [['Rusiya'],['Çin'],['Türkiyə'],['Almanya']],
        [['Çaves'],['Pablo'],['Berluskoni'],['Putin']],
        [['Lirə'],['Manat'],['Dollar'],['Euro']],
        [['Qazaxıstan'],['Özbəkistan'],['Qırğızıstan'],['Azərbaycan']],
        [['Kardiologiya'],['Nevrologiya'],['Onkologiya'],['Urologiya']],
        [['Oslo'],['Helsinki'],['Bakı'],['Stokholm']],
        [['Saniyə'],['Dəqiqə'],['Saat'],['Metr']]]
counter = 0
counter_1 = 0
answer_output = [] 
helper = []
helper_window = ["joker,","50/50,","auditoriya"]
while True:
    if counter_1 == 12:
        time.sleep(1)
        os.system('cls')
        print('\n-------------------------\n||--ARTIQ MILIONERSIZ--||\n-------------------------')
        time.sleep(10)
        break
    elif counter_1 > 0 and help_ != "joker" and help_ != "50/50" and help_ != "auditoriya":
        help_ = ""
        print("\n<--Büdcə",*money[counter_1 - 1],"AZN-->\n")
        checkpoint = input('davam ucun <-İstənilən düyməni basın-> yoxsa <-dayanmaq-> :')
        if checkpoint == 'dayanmaq':
            print('Qazadığınız pul',*money[counter_1 - 1])
            time.sleep(5)
            os.system('cls')
            break
        time.sleep(1)
        os.system('cls')
    while True:
        i = random.choice(answer[counter_1])
        if i not in answer_output:
            answer_output.append(i)
            counter+=1
        elif counter == 4:
            counter = 0
            break
    print(*question[counter_1])
    print("-----------------\nA)",*answer_output[0],
          "\nB)",*answer_output[1],
          "\nC)",*answer_output[2],
          "\nD)",*answer_output[3],
          "\n-----------------")
    answer_output = []
    print("Mövcut Köməkçilər <--",*helper_window,"-->")
    help_ = input("istəmirsinizsə <<-İstənilən düyməni basın->> basın : ")
 
    if help_ not in helper and help_ == "joker":
        counter_1+=1
        helper.append(help_)
        time.sleep(1)
        os.system('cls')
        helper_window.remove("joker,")
        continue
    elif help_ == "":
        pass
    elif help_ not in helper and help_ == "50/50": 
        helper.append(help_)
        time.sleep(1)
        os.system('cls')
        helper_window.remove("50/50,")
        answer_50 = [*answer[counter_1][0]]
        while True:
            i = random.choice(answer[counter_1])
            if i != answer[counter_1][0]:
                answer_50.append(i)
                break
        print(*question[counter_1])
        print("-----------------\nA)",answer_50[0],
          "\nB)",*answer_50[1])
    elif help_ not in helper and help_ == "auditoriya":
        helper.append(help_)
        helper_window.remove("auditoriya")
        while True:
            audi = random.randint(0,100)
            audi_1 = random.randint(0,100)
            audi_2 = random.randint(0,100)
            audi_3 = random.randint(0,100)
            if audi + audi_1 + audi_2 + audi_3 == 100:
                audi_full = [audi,audi_1,audi_2,audi_3]
                audi_full.sort()
                print("-----------------\n|",*answer[counter_1][1],audi_full[0],"%")
                print("|",*answer[counter_1][3],audi_full[1],"%")
                print("|",*answer[counter_1][2],audi_full[2],"%")
                print("|",*answer[counter_1][0],audi_full[3],"%\n-----------------")
                break
    help_ = ""
    while True:
        player_answer = input("\n||--Cavabınız : ")
        correct = input("\nƏminsinizsə <-Bəli-> Əmin deyilsinizsə <-Xeyir-> yazin : ")
        if correct != "Bəli":
            if correct != "Xeyir":
                print("\n----------------------------------------------\n| Sadəcə Bəli Və yaxud Xeyir yaza bilərsiniz |\n----------------------------------------------\n")
        elif correct == "Xeyir":
            continue
        elif player_answer != str(*answer[counter_1][0]):
            print("Cavab Yanlışdır. Doğru Cavab - ",*answer[counter_1][0]," -")
            if counter_1 == 1 or counter_1 == 0:
                time.sleep(1)
                os.system('cls')
                print("\n<<---0 AZN QAZANDINIZ--->>\n")
                time.sleep(15)
                break
            elif 1 < counter_1 < 7:
                time.sleep(1)
                os.system('cls')
                print("\n<<---1000 AZN QAZANDINIZ--->>\n")
                time.sleep(15)
            elif 7 < counter_1 < 12:
                time.sleep(1)
                os.system('cls')
                print("\n<<---15000 AZN QAZANDINIZ--->>\n")
                time.sleep(15)
                break
            break
        elif correct == "Bəli" and player_answer == str(*answer[counter_1][0]):
            print("\n<<----Seçdiyiniz Cavab Doğrudur---->>\n")
            time.sleep(2)
            os.system('cls')
            counter_1+=1
            break
    if player_answer != str(*answer[counter_1 - 1][0]):
        break
    else:
        pass


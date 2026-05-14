import os
import time
import sys

class BazaForsunok:
    def __init__(self):
        self.dani = {
            "0445110064": ["Bosch", "CRI 1", "0.052", "0.050", "15.5 Ом", "50Нм + 90°", "Mercedes 2.2 CDI"],
            "0445110123": ["Bosch", "CRI 2.1", "0.048", "0.050", "16.0 Ом", "50Нм + 90°", "Mercedes Sprinter"],
            "0445110183": ["Bosch", "CRI 2.1", "0.055", "0.052", "15.8 Ом", "55Нм + 90°", "Opel/Fiat 1.3 CDTI"],
            "0445110239": ["Bosch", "CRI 2.1", "0.050", "0.048", "16.2 Ом", "50Нм + 90°", "Hyundai/Kia 1.5 CRDi"],
            "0445110293": ["Bosch", "CRI 2.1", "0.053", "0.050", "15.5 Ом", "50Нм + 90°", "VW/Audi 2.0 TDI"],
            "0445110305": ["Bosch", "CRI 2.1", "0.050", "0.045", "16.0 Ом", "45Нм + 90°", "Renault 1.5 dCi"],
            "0445110311": ["Bosch", "CRI 2.1", "0.052", "0.050", "15.9 Ом", "50Нм + 90°", "BMW 3.0d (E90)"],
            "0445110359": ["Bosch", "CRI 2.1", "0.048", "0.050", "16.1 Ом", "55Нм + 90°", "Iveco Daily 2.3"],
            "0445110418": ["Bosch", "CRI 2.4", "0.054", "0.052", "15.7 Ом", "50Нм + 90°", "Jeep 2.8 CRD"],
            "0445110511": ["Bosch", "CRI 2.1", "0.050", "0.050", "16.0 Ом", "50Нм + 90°", "Газель (Cummins)"],
            "0445110719": ["Bosch", "CRI 2.1", "0.052", "0.050", "15.8 Ом", "50Нм + 90°", "Peugeot 1.6 HDi"],
            "0445110002": ["Bosch", "CRI 1", "0.050", "0.050", "15.5 Ом", "50Нм + 90°", "BMW 530d (E39)"],
            "0445110243": ["Bosch", "CRI 2.1", "0.051", "0.049", "16.0 Ом", "50Нм + 90°", "Volvo V70 2.4D"],
            "0445110110": ["Bosch", "CRI 1", "0.050", "0.050", "15.6 Ом", "50Нм + 90°", "Alfa Romeo 1.9 JTD"],
            "0445110190": ["Bosch", "CRI 2.1", "0.052", "0.050", "16.0 Ом", "50Нм + 90°", "Mercedes E-Class"],
            "0445110141": ["Bosch", "CRI 1", "0.050", "0.050", "15.5 Ом", "50Нм + 90°", "BMW X5 3.0d"],
            "0445120002": ["Bosch", "CRIN 1", "0.150", "0.250", "0.30 Ом", "70Нм + 90°", "MAN TGA"],
            "0445120007": ["Bosch", "CRIN 1", "0.160", "0.260", "0.32 Ом", "70Нм + 90°", "Iveco Cursor"],
            "0445120121": ["Bosch", "CRIN 2", "0.155", "0.250", "0.35 Ом", "75Нм + 90°", "Cummins ISBe"],
            "0445120153": ["Bosch", "CRIN 2", "0.150", "0.245", "0.33 Ом", "70Нм + 90°", "Камаз / МАЗ"],
            "0445120224": ["Bosch", "CRIN 2", "0.165", "0.280", "0.34 Ом", "80Нм + 90°", "WEICHAI WP10"],
            "0445120212": ["Bosch", "CRIN 2", "0.150", "0.250", "0.31 Ом", "70Нм + 90°", "DAF CF85"],
            "0445120059": ["Bosch", "CRIN 1", "0.160", "0.260", "0.32 Ом", "70Нм + 90°", "MAN F2000"],
            "0445120123": ["Bosch", "CRIN 2", "0.150", "0.250", "0.34 Ом", "75Нм + 90°", "Cummins QSB"],
            "0445115007": ["Bosch", "Piezo", "0.035", "0.040", "180 кОм", "Нерозбірна", "Audi A6 3.0 TDI"],
            "0445116017": ["Bosch", "Piezo", "0.032", "0.038", "185 кОм", "Нерозбірна", "BMW X5 (E70)"],
            "0445115067": ["Bosch", "Piezo", "0.035", "0.040", "180 кОм", "Нерозбірна", "Mercedes OM642"],
            "28231014": ["Delphi", "C2i", "N/A", "0.038", "0.20 Ом", "45 Нм", "Renault Kangoo 1.5"],
            "28231973": ["Delphi", "C2i", "N/A", "0.040", "0.22 Ом", "50 Нм", "Ford Mondeo 2.0 TDCi"],
            "28342997": ["Delphi", "C3i", "N/A", "0.035", "0.21 Ом", "45 Нм", "Mercedes OM651"],
            "EJBR02101Z": ["Delphi", "C2i", "N/A", "0.038", "0.20 Ом", "45 Нм", "Hyundai Terracan"],
            "EJBR03301D": ["Delphi", "C2i", "N/A", "0.040", "0.23 Ом", "50 Нм", "Kia Bongo 2.9"],
            "EJBR05102D": ["Delphi", "C2i", "N/A", "0.038", "0.19 Ом", "45 Нм", "Renault Logan 1.5 dCi"],
            "EJBR01801A": ["Delphi", "C2i", "N/A", "0.038", "0.20 Ом", "45 Нм", "Renault Clio 1.5 dCi"],
            "EJBR04401D": ["Delphi", "C2i", "N/A", "0.039", "0.21 Ом", "50 Нм", "SsangYong Kyron"],
            "EMBR00101D": ["Delphi", "Piezo", "0.025", "0.030", "200 кОм", "55 Нм", "VW Amarok 2.0 TDI"],
            "095000-5471": ["Denso", "G2", "0.045", "0.055", "0.40 Ом", "65 Нм", "Toyota LC 3.0"],
            "095000-5801": ["Denso", "G2", "0.050", "0.060", "0.38 Ом", "60 Нм", "Nissan Navara 2.5"],
            "095000-5600": ["Denso", "G2", "0.048", "0.058", "0.42 Ом", "65 Нм", "Mitsubishi L200"],
            "095000-6222": ["Denso", "G2", "0.052", "0.062", "0.40 Ом", "65 Нм", "Mazda BT-50"],
            "5WS40539": ["Siemens", "VDO", "0.028", "0.035", "195 кОм", "Нерозбірна", "Ford/Peugeot 2.0 HDi"],
            "A2C59511603": ["VDO", "Piezo", "0.030", "0.036", "200 кОм", "Нерозбірна", "VW Passat 1.6 TDI"],
            "0445110068": ["Bosch", "CRI 1", "0.052", "0.050", "15.5 Ом", "50Нм + 90°", "Mercedes 2.7 CDI"],
            "0445110070": ["Bosch", "CRI 1", "0.052", "0.050", "15.7 Ом", "50Нм + 90°", "Jeep 2.7 CRD"],
            "0445120024": ["Bosch", "CRIN 1", "0.155", "0.250", "0.32 Ом", "70Нм + 90°", "Iveco Tector"],
            "0445110311": ["Bosch", "CRI 2.1", "0.050", "0.050", "16.0 Ом", "50Нм + 90°", "BMW E60 525d"],
            "0445110646": ["Bosch", "CRI 2.1", "0.053", "0.050", "16.1 Ом", "50Нм + 90°", "Sorento 2.2 CRDi"],
            "0445120134": ["Bosch", "CRIN 2", "0.150", "0.250", "0.34 Ом", "75Нм + 90°", "Cummins ISLe"],
            "28236381": ["Delphi", "C3i", "N/A", "0.036", "0.21 Ом", "45 Нм", "Mercedes Sprinter 651"],
            "095000-0570": ["Denso", "G2", "0.045", "0.055", "0.40 Ом", "60 Нм", "John Deere"],
            "0445110253": ["Bosch", "CRI 2.1", "0.050", "0.050", "16.0 Ом", "50Нм + 90°", "Chevrolet Lacetti 2.0"],
        }

    def znayty(self, tekst):
        zbigy = []
        for nomer in self.dani.keys():
            if tekst in nomer:
                zbigy.append(nomer)
        return zbigy

    def otrimaty_info(self, nomer):
        return self.dani.get(nomer)

class ProgramnyiInterfeys:
    @staticmethod
    def ochystyty():
        os.system('cls' if os.name == 'nt' else 'clear')

    def liniya(self):
        print("-" * 70)

    def pokazu_menu(self):
        self.ochystyty()
        self.liniya()
        print("                 ПРОГРАМА ДЛЯ ПОШУКУ ФОРСУНОК")
        self.liniya()
        print("1. Пошук за номером")
        print("2. Переглянути всю базу")
        print("3. Вихід")
        print("")

    def pokazaty_kartu(self, nomer, info):
        print(f"\nІНФОРМАЦІЯ ПРО ФОРСУНКУ: {nomer}")
        self.liniya()
        print(f"Бренд:          {info[0]}")
        print(f"Тип:            {info[1]}")
        print(f"Зазор AH:       {info[2]} мм")
        print(f"Зазор RNH:      {info[3]} мм")
        print(f"Опір котушки:   {info[4]}")
        print(f"Момент затяжки: {info[5]}")
        print(f"Застосування:   {info[6]}")
        self.liniya()

    def poshuk_forsunok(self, baza):
        self.ochystyty()
        self.liniya()
        print("                         ПОШУК")
        self.liniya()
        zapyt = input("\n Введіть частину номера: ").strip()
        
        if not zapyt:
            return

        rezultaty = baza.znayty(zapyt)

        if len(rezultaty) == 0:
            print("\n Нічого не знайдено.")
        elif len(rezultaty) == 1:
            self.pokazaty_kartu(rezultaty[0], baza.otrimaty_info(rezultaty[0]))
        else:
            print(f"\n Знайдено варіантів: {len(rezultaty)}")
            for i in range(len(rezultaty)):
                item = rezultaty[i]
                inf = baza.otrimaty_info(item)
                print(f"{i+1}. {item} | {inf[0]} | {inf[6]}")
            
            try:
                vybir = int(input("\n Оберіть порядковий номер: "))
                if 1 <= vybir <= len(rezultaty):
                    nomer_f = rezultaty[vybir-1]
                    self.pokazaty_kartu(nomer_f, baza.otrimaty_info(nomer_f))
                else:
                    print(" Помилка вибору.")
            except:
                print(" Потрібно вводити число.")
        
        input("\n Натисніть Enter...")

    def vsya_baza(self, baza):
        self.ochystyty()
        self.liniya()
        print(f"{'Номер':<15} | {'Бренд':<10} | {'Автомобіль':<25}")
        self.liniya()
        for k, v in baza.dani.items():
            print(f"{k:<15} | {v[0]:<10} | {v[6]:<25}")
        input("\n Натисніть Enter...")

def main():
    baza = BazaForsunok()
    ui = ProgramnyiInterfeys()
    
    while True:
        ui.pokazu_menu()
        punkt = input(" Оберіть пункт: ")
        
        if punkt == "1":
            ui.poshuk_forsunok(baza)
        elif punkt == "2":
            ui.vsya_baza(baza)
        elif punkt == "3":
            print(" Вихід з програми...")
            time.sleep(0.3)
            break

if __name__ == "__main__":
    main()
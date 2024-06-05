from paskaita_18.darbuotojai import Stazuotojas, Vadybininkas, Inzinierius
if __name__ == "__main__":
    vadybininkas = Vadybininkas(base_salary=3000, bonus=1500)
    print(f"Vaidmuo: {vadybininkas.get_role()}")
    print(f"Darbo užmokestis: {vadybininkas.calculate_pay():.2f}")

    inzinierius = Inzinierius(hourly_rate=25, hours_worked=160)
    print(f"Vaidmuo: {inzinierius.get_role()}")
    print(f"Darbo užmokestis: {inzinierius.calculate_pay():.2f}")

    stazuotojas = Stazuotojas(stipend=1000)
    print(f"Vaidmuo: {stazuotojas.get_role()}")
    print(f"Darbo užmokestis: {stazuotojas.calculate_pay():.2f}")

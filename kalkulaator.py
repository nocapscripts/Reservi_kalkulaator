from datetime import date
from colorama import Fore, Style

def calc():
    today = date.today()

    years = today.year  # Kraba hetkene aastaarv automaatselt

    month = int(input(Fore.YELLOW + "Sisesta kuu (1-12): " + Style.RESET_ALL))

    day = int(input(Fore.YELLOW + "Sisesta päev (1-31): " + Style.RESET_ALL))

    start_date = date(years, month, day)

    end_date = date(years, 12, 13)  # ebakindel ajalõpp

    days_until_end = (end_date - today).days
    total_days = (end_date - start_date).days  # kogu ajateenistuse kestus päevades

    # Arvutame protsent arvu
    days_elapsed = (today - start_date).days
    percentage_completed = (days_elapsed / total_days) * 100 if total_days > 0 else 0

    print(Fore.GREEN + f"Praegune aasta: {Fore.CYAN}{years}{Style.RESET_ALL}")
    print(Fore.GREEN + f"Ajateenistuse alguse aeg: {Fore.CYAN}{start_date}{Style.RESET_ALL}.")
    print(Fore.GREEN + f"Ajateenistuse lõpuni on jäänud: {Fore.CYAN}{days_until_end} päeva{Style.RESET_ALL}.")
    print(Fore.GREEN + f"Ajateenistusest on läbitud: {Fore.CYAN}{days_elapsed} päeva{Style.RESET_ALL}.")
    print(Fore.GREEN + f"Ajateenistusest on läbitud {Fore.CYAN}{percentage_completed:.2f}%{Style.RESET_ALL}.")

def main():
    while True:
        try:
            print(Fore.CYAN + """
            Tere tulemast EKV reservi kalkulaatorisse!
            
            Valikud:
            1. Kalkulaator
            2. Välju
            """ + Style.RESET_ALL)
            select = int(input(Fore.YELLOW + "Valik: " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "Viga! Te ei sisestanud õiget valikut." + Style.RESET_ALL)
            continue
        
        if select == 1:
            calc()
        elif select == 2:
            print(Fore.MAGENTA + "Väljumine..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Viga! Palun sisestage õige valik." + Style.RESET_ALL)

if __name__ == "__main__":
    main()

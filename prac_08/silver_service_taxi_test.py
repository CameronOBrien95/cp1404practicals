from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Hummer", 200, 6)
    taxi.drive(18)
    print(taxi.get_fare())
    print(taxi)

main()
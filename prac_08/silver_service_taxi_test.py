from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    my_taxi = SilverServiceTaxi("Tesla", 100, 2)
    my_taxi.drive(18)
    print(my_taxi)
    print("${:.2f}".format(my_taxi.get_fare()))


main()

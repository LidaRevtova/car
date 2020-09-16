class Carbase:

    def __init__(self, car_type, brand, passenger_seats_count, photo_le_name, body_whl, carring, extra):
        self.car_type = car_type
        self.brand = brand
        self.passenger_seats_count = passenger_seats_count
        self.photo_le_name = photo_le_name
        self.body_whl = body_whl
        self.carring = carring
        self.extra = extra

    def get_photo_le_ext(self):
        num_of_t = self.photo_le_name.find('.')
        return self.photo_le_name[num_of_t:]

class Car:

    def __init__(self):
        pass

class Truck:
    def __init__(self):
        pass


class Specmachine:
    def __init__(self):
        pass

def get_car_list(filename):
    car_list = []
    with open(filename, encoding='utf-8') as f:
        for i in f:
            line = i.split(';')
            line.append(car_list)
    return car_list

def main():
    pass

if __name__ == '__main__':
    main()
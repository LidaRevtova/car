class Carbase:
    """базовый класс"""

    def __init__(self, car_type=None, brand=None, photo_le_name=None):
        """метод инициализации"""
        self.car_type = car_type
        self.brand = brand
        self.photo_le_name = photo_le_name

    def get_photo_le_ext(self):
        """метод для получ расширения"""
        num_of_t = self.photo_le_name.find('.')
        if num_of_t != -1:
            return self.photo_le_name[num_of_t:]
        return None

class Car(Carbase):
    """класс машин"""

    def __init__(self, car_type, brand, passenger_seats_count, photo_le_name, body_whl=None, carrying=None):
        """метод инициализации"""
        super().__init__(car_type, brand, photo_le_name)
        self.passenger_seats_count = int(passenger_seats_count) or None
        self.carrying = float(carrying) or None

class Truck(Carbase):
    """класс грузовика"""

    def __init__(self, car_type, brand, passenger_seats_count, photo_le_name, body_whl, carrying):
        """метод инициализации"""
        super().__init__(car_type, brand, photo_le_name)
        self.body_whl = body_whl or None
        self.carrying = float(carrying)
        if self.body_whl is not None:
            self.body_whl = body_whl.split('x')
            self.body_width = float(self.body_whl[0])
            self.body_height = float(self.body_whl[1])
            self.body_length = float(self.body_whl[-1])
        else:
            self.body_height, self.body_length, self.body_width = 0.0, 0.0, 0.0

    def get_body_volume(self):
        """метод для получ размера"""
        return self.body_length * self.body_width * self.body_height


class Specmachine(Carbase):
    """класс спец машин"""
    def __init__(self, car_type, brand, passenger_seats_count, photo_le_name, body_whl=None, carrying=None, extra=None):
        """метод инициализации"""
        super().__init__(car_type, brand, photo_le_name)
        self.extra = extra
        self.carrying = float(carrying) or None


def get_car_list(filename):
    """"""
    car_list = []
    with open(filename, encoding='utf-8') as f:
        for i in f:
            line = i.split(';')
            if line[0] == 'car':
                car_list.append(Car(*line[:-1]))
            elif line[0] == 'truck':
                car_list.append(Truck(*line[:-1]))
            elif line[0] == 'spec_machine':
                car_list.append(Specmachine(*line[:-1]))
            else:
                pass

    return car_list

def main():
    get_car_list('solution.txt')

if __name__ == '__main__':
    main()


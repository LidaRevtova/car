class Carbase:

    def __init__(self, car_type, brand, photo_le_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_le_name = photo_le_name
        self.carrying = float(carrying)

    def get_photo_le_ext(self):
        num_of_t = self.photo_le_name.find('.')
        return self.photo_le_name[num_of_t:]

class Car:

    def __init__(self, car_type, brand, passenger_seats_count, photo_le_name, carrying):
        self.passenger_seats_count = int(passenger_seats_count)
        super.__init__(car_type, brand, photo_le_name, carrying)



class Truck:
    def __init__(self, car_type, brand, photo_le_name, carrying, body_whl):
        super.__init__(car_type, brand, photo_le_name, carrying)
        self.body_whl = body_whl.split('x')
        self.body_width = float(self.body_whl[0])
        self.body_height = float(self.body_whl[1])
        self.body_length = float(self.body_whl[2])

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class Specmachine:
    def __init__(self, car_type, brand, photo_le_name, carrying, extra):
        super.__init__(car_type, brand, photo_le_name, carrying)
        self.extra = extra



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
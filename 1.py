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
    def __init__(self, car_type, brand, photo_le_name, carrying, body_width, body_height, body_length):
        super.__init__(car_type, brand, photo_le_name, carrying)
        self.body_width = float(body_width)
        self.body_height = float(body_height)
        self.body_length = float(body_length)


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
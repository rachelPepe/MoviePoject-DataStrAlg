# movie class

class Movie:
    def __init__(self, ID, title, year, price, city, state, status):
        self.ID = ID
        self.title = title
        self.year = year
        self.price = price
        self.city = city
        self.state = state
        self.status = status

    def __str__(self):
        return (f'{self.ID}: {self.title} / {self.year} / ${self.price} -- status: {self.status}\n'
                f'   Playing in: {self.city}, {self.state}')


# value = storage.get('my_key')
# storage.delete('my_key')

class StorageHelper():

    def __init__(self, **kwargs):
        self.storage = kwargs.pop('storage')

    def load_colors(self):
        # self.storage.put('my_key', 'my_value')
        self.storage.put('blue', value = (0.36, 0.41, 0.57, 1))
        self.storage.put('light_blue', value = (0.55, 0.51, 0.62, 1))
        self.storage.put('pink', value = (0.9, 0.8, 0.8, 1))
        self.storage.put('light_pink', value = (0.89, 0.8, 0.75, 1))

    def color(self, color_name: str):
        return self.storage.get(color_name)['value']

class LoggingDict(dict):
    def __setitem__(self,key,value):
        print(f'Setting {key}:{value}')
        super().__setitem__(key, value)

    def __getitem__(self, item):
        print(f'Getting {item}')
        return super().__getitem__(item)
    
    def __delitem__(self, key):
        print(f"Deleting {key}")
        super().__delitem__(key)
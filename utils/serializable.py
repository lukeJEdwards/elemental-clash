__all__ = ['Serializable']

class Serializable:
    def __init__(self, **kwargs:dict):
        super().__init__(**kwargs)
    
    def encode(self, obj:any):
        if isinstance(obj, tuple): return {'__tuple__':True, 'obj':obj}
        elif isinstance(obj, list): return [self.encode(item) for item in obj]
        elif isinstance(obj, dict): return {key: self.encode(value) for key, value in obj.items()}
        else: return obj
        
    def serialize(self):
        tuple_perserved_dict = {}
        for key, obj in self.__dict__.items():
            if key[0] == '_': continue
            else: tuple_perserved_dict[key] = self.encode(obj)
        return tuple_perserved_dict
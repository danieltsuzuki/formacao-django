class Pet:
    def __init__(self, dono, nome, nascimento, especie, cor):
        self.__dono = dono
        self.__nome = nome
        self.__nascimento = nascimento
        self.__especie = especie
        self.__cor = cor
    
    @property
    def dono(self):
        return self.__dono
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def nascimento(self):
        return self.__nascimento
    
    @property
    def especie(self):
        return self.__especie
    
    @property
    def cor(self):
        return self.__cor
    
    @dono.setter
    def dono(self, dono):
        self.__dono = dono
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento
    
    @especie.setter
    def especie(self, especie):
        self.__especie = especie
    
    @cor.setter
    def cor(self, cor):
        self.__cor = cor
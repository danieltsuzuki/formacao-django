class Vaga:
    def __init__(self, titulo, descricao, salario, local, quantidade, contato, tipo_contratacao, tecnologias):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__salario = salario
        self.__local = local
        self.__quantidade = quantidade
        self.__contato = contato
        self.__tipo_contratacao = tipo_contratacao
        self.__tecnlogias = tecnologias
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def salario(self):
        return self.__salario
    
    @property
    def local(self):
        return self.__local
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @property
    def contato(self):
        return self.__contato
    
    @property
    def tipo_contratacao(self):
        return self.__tipo_contratacao
    
    @property
    def tecnologias(self):
        return self.__tecnlogias
    
    @titulo.setter
    def titulo(self, valor):
        self.__titulo = valor
    
    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor
    
    @salario.setter
    def salario(self, valor):
        self.__salario = valor
    
    @local.setter
    def local(self, valor):
        self.__local = valor
    
    @quantidade.setter
    def quantidade(self, valor):
        self.__quantidade = valor
    
    @contato.setter
    def contato(self, valor):
        self.__contato = valor
    
    @tipo_contratacao.setter
    def tipo_contratacao(self, valor):
        self.__tipo_contratacao = valor
    
    @tecnologias.setter
    def tecnologias(self, valor):
        self.__tecnlogias = valor

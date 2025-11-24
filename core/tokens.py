class Token:
    """Representa um token encontrado no código fonte"""
    
    def __init__(self, tipo: str, valor: str):
        self.tipo = tipo
        self.valor = valor
    
    def to_dict(self):
        """Converte o token para dicionário"""
        return {
            'Tipo': self.tipo,
            'Valor': self.valor
        }
    
    def __repr__(self):
        return f"Token(tipo='{self.tipo}', valor='{self.valor}')"


class TabelaSimbolos:
    """Gerencia a tabela de símbolos do analisador"""
    
    def __init__(self):
        self.simbolos = {}
        self.contador = 0
    
    def adicionar_simbolo(self, simbolo: str):
        """Adiciona um símbolo à tabela se não existir"""
        if simbolo not in self.simbolos:
            self.contador += 1
            self.simbolos[simbolo] = self.contador
    
    def obter_todos(self):
        """Retorna todos os símbolos em formato de lista"""
        return [
            {'Ordem': ordem, 'Símbolo': simbolo}
            for simbolo, ordem in self.simbolos.items()
        ]
    
    def __len__(self):
        return len(self.simbolos)
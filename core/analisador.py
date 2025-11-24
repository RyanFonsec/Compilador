import re
from .tokens import Token, TabelaSimbolos
from .config import PALAVRAS_CHAVE_C, PADROES_TOKEN


class AnalisadorLexico:
    """Analisador léxico para linguagem C"""
    
    def __init__(self):
        self.padroes_compilados = [
            (tipo, re.compile(pattern)) 
            for tipo, pattern in PADROES_TOKEN
        ]
    
    def analisar(self, codigo: str):
        """
        Analisa o código fonte e retorna tokens e tabela de símbolos
        
        Args:
            codigo (str): Código fonte em C para análise
            
        Returns:
            tuple: (lista_de_tokens, tabela_de_simbolos)
        """
        tokens = []
        tabela_simbolos = TabelaSimbolos()
        posicao = 0
        
        while posicao < len(codigo):
            token = self._proximo_token(codigo, posicao)
            
            if token:
                # Processa token válido
                if token.tipo != 'ESPACO':
                    tokens.append(token)
                    
                    # Adiciona identificadores à tabela de símbolos
                    if token.tipo == 'IDENTIFICADOR':
                        tabela_simbolos.adicionar_simbolo(token.valor)
                
                posicao += len(token.valor)
            else:
                # Token inválido
                token_erro = Token('ERRO', codigo[posicao])
                tokens.append(token_erro)
                posicao += 1
        
        return tokens, tabela_simbolos
    
    def _proximo_token(self, codigo: str, posicao: int):
        """
        Encontra o próximo token a partir da posição atual
        
        Args:
            codigo (str): Código fonte
            posicao (int): Posição atual no código
            
        Returns:
            Token or None: Próximo token encontrado ou None se inválido
        """
        for tipo, regex in self.padroes_compilados:
            match = regex.match(codigo, posicao)
            if match:
                valor = match.group(0)
                token = Token(tipo, valor)
                
                # Classificação especial para palavras-chave
                if tipo == 'IDENTIFICADOR' and valor in PALAVRAS_CHAVE_C:
                    token.tipo = 'PALAVRA_CHAVE'
                
                return token
        return None
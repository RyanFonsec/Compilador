# Configurações e constantes do analisador
PALAVRAS_CHAVE_C = {
    'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
    'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
    'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
    'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while'
}

PADROES_TOKEN = [
    ('COMENTARIO', r'//.*|/\*[\s\S]*?\*/'),
    ('PREPROCESSADOR', r'#\s*\w+'),  
    ('STRING', r'L?\"([^\\\"]|\\.)*\"'), 
    ('CHAR', r"L?\'([^\\\']|\\.)*\'"),
    
    
    ('NUMERO_HEX', r'\b0x[0-9a-fA-F]+[uUlL]*\b'),
    ('NUMERO_FLOAT', r'\b\d*\.\d+([eE][-+]?\d+)?[fFlL]?\b|\b\d+[eE][-+]?\d+[fFlL]?\b'),
    ('NUMERO_INT', r'\b\d+[uUlL]*\b'),
    
    
    ('OPERADOR', r'>>=|<<=|\.\.\.|->|\+\+|--|&&|\|\||<=|>=|==|!=|\+=|-=|\*=|/=|%=|&=|\^=|\|=|[+\-*/%=!<>&|^~?]'),
    
    ('DELIMITADOR', r'[(){}\[\],;.:]'), 
    ('IDENTIFICADOR', r'[a-zA-Z_]\w*'),
    ('ESPACO', r'\s+')
]

EXEMPLO_CODIGO_C = """#include <stdio.h>

int main() {
    int numero = 42;
    float pi = 3.14;
    char letra = 'A';
    
    // Comentário de linha
    printf("Hello, World!\\n");
    
    /* Comentário 
       de bloco */
    
    for(int i = 0; i < 10; i++) {
        numero += i;
    }
    
    return 0;
}"""
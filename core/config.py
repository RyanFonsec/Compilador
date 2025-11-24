# Configurações e constantes do analisador
PALAVRAS_CHAVE_C = {
    'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
    'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
    'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
    'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while'
}

PADROES_TOKEN = [
    ('COMENTARIO', r'//.*|/\*[\s\S]*?\*/'),
    ('STRING', r'\"([^\\\"]|\\.)*\"'),
    ('CHAR', r"\'([^\\\']|\\.)*\'"),
    ('NUMERO', r'\b\d+\.\d*\b|\b\d+\b|\b0x[0-9a-fA-F]+\b'),
    ('OPERADOR', r'[+\-*/%=!<>&|^~]{1,3}'),
    ('DELIMITADOR', r'[(){}\[\],;.:]'),
    ('IDENTIFICADOR', r'[a-zA-Z_]\w*'),
    ('PREPROCESSADOR', r'#\s*\w+'),
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
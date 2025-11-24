import re
import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Analisador Léxico C", layout="wide")

st.title("🔍 Analisador Léxico - Linguagem C")
st.markdown("---")

# Palavras-chave da linguagem C
C_KEYWORDS = {
    'auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do',
    'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if',
    'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static',
    'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while'
}

# Padrões de tokens
token_patterns = [
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

def analisar_codigo(codigo):
    tokens = []
    tabela_simbolos = {}
    posicao = 0
    contador_simbolo = 0
    
    while posicao < len(codigo):
        match = None
        for token_type, pattern in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(codigo, posicao)
            if match:
                valor = match.group(0)
                
                # Ignora espaços
                if token_type == 'ESPACO':
                    posicao = match.end()
                    break
                
                # Classifica palavras-chave
                if token_type == 'IDENTIFICADOR' and valor in C_KEYWORDS:
                    token_type = 'PALAVRA_CHAVE'
                
                # Adiciona token
                tokens.append((token_type, valor))
                
                # Adiciona à tabela de símbolos
                if token_type == 'IDENTIFICADOR' and valor not in tabela_simbolos:
                    contador_simbolo += 1
                    tabela_simbolos[valor] = contador_simbolo
                
                posicao = match.end()
                break
        
        if not match:
            # Caractere não reconhecido - avança 1 posição
            st.warning(f"Caractere não reconhecido: '{codigo[posicao]}' na posição {posicao}")
            tokens.append(('ERRO', codigo[posicao]))
            posicao += 1
    
    return tokens, tabela_simbolos

# Interface principal
st.subheader("📝 Entrada do Código")

# Exemplo de código C
codigo_exemplo = """#include <stdio.h>

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

# Opções de entrada
opcao = st.radio("Escolha a forma de entrada:", 
                ["📝 Usar Código Exemplo", "📤 Fazer Upload de Arquivo", "✏️ Digitar Código"])

codigo_fonte = ""

if opcao == "📝 Usar Código Exemplo":
    codigo_fonte = codigo_exemplo
    st.code(codigo_fonte, language='c')

elif opcao == "📤 Fazer Upload de Arquivo":
    arquivo = st.file_uploader("Selecione um arquivo .c", type=['c', 'h'])
    if arquivo is not None:
        codigo_fonte = arquivo.read().decode('utf-8')
        st.success(f"Arquivo '{arquivo.name}' carregado com sucesso!")
        st.code(codigo_fonte, language='c')

else:  # Digitar código
    codigo_fonte = st.text_area("Digite seu código C:", value=codigo_exemplo, height=300)

# Botão de análise
if st.button("🚀 Analisar Código", type="primary") and codigo_fonte:
    with st.spinner("Analisando código C..."):
        tokens, tabela_simbolos = analisar_codigo(codigo_fonte)
    
    # Exibir resultados
    st.subheader("📋 Resultados da Análise Léxica")
    
    # Tokens encontrados
    st.write("### Lista de Tokens")
    if tokens:
        df_tokens = pd.DataFrame(tokens, columns=['Tipo', 'Valor'])
        st.dataframe(df_tokens, use_container_width=True)
        
        # Estatísticas
        col1, col2, col3 = st.columns(3)
        total_tokens = len(tokens)
        palavras_chave = len([t for t in tokens if t[0] == 'PALAVRA_CHAVE'])
        identificadores = len([t for t in tokens if t[0] == 'IDENTIFICADOR'])
        
        col1.metric("Total de Tokens", total_tokens)
        col2.metric("Palavras-chave", palavras_chave)
        col3.metric("Identificadores", identificadores)
    else:
        st.warning("Nenhum token encontrado!")
    
    # Tabela de símbolos
    st.write("### Tabela de Símbolos")
    if tabela_simbolos:
        df_simbolos = pd.DataFrame([
            {'Ordem': ordem, 'Símbolo': simbolo}
            for simbolo, ordem in tabela_simbolos.items()
        ])
        st.dataframe(df_simbolos, use_container_width=True)
        st.metric("Símbolos Únicos", len(tabela_simbolos))
    else:
        st.warning("Nenhum símbolo na tabela!")
    
    # Verificação de erros
    st.write("### Verificação de Erros")
    erros_token = len([t for t in tokens if t[0] == 'ERRO'])
    
    col1, col2 = st.columns(2)
    with col1:
        if erros_token == 0:
            st.success("✅ SEM ERROS NA IDENTIFICAÇÃO DE TOKENS")
        else:
            st.error(f"❌ ERROS NA IDENTIFICAÇÃO DE TOKENS: {erros_token} erro(s)")
    
    with col2:
        if len(tabela_simbolos) > 0:
            st.success("✅ SEM ERROS NA IDENTIFICAÇÃO DE SÍMBOLOS")
        else:
            st.warning("⚠️ Nenhum símbolo identificado")

# Explicação do código
st.markdown("---")
st.subheader("🔍 Explicação do Código")

with st.expander("📖 Como o Analisador Léxico Funciona"):
    st.markdown("""
    ### Funcionamento do Analisador Léxico:
    
    **1. Definição dos Padrões (Regex):**
    - Usamos expressões regulares para identificar cada tipo de token
    - Exemplo: `r'[a-zA-Z_]\\w*'` para identificadores
    
    **2. Processamento:**
    - O código é percorrido caractere por caractere
    - Para cada posição, testamos todos os padrões regex
    - Quando encontramos um match, classificamos o token
    
    **3. Tabela de Símbolos:**
    - Armazena apenas identificadores únicos
    - Mantém a ordem de primeira ocorrência
    - Ignora palavras-chave e outros tokens
    
    **4. Tratamento de Erros:**
    - Caracteres não reconhecidos são marcados como ERRO
    - O processamento continua após erros
    """)

st.info("💡 **Dica:** Use o código exemplo para testar ou faça upload de seu próprio arquivo .c")
import streamlit as st
import pandas as pd
from core.config import EXEMPLO_CODIGO_C


class ComponentesInterface:
    """Componentes reutilizáveis da interface"""
    
    @staticmethod
    def exibir_cabecalho():
        """Exibe o cabeçalho da aplicação"""
        st.title("🔍 Analisador Léxico - Linguagem C")
        st.markdown("---")
    
    @staticmethod
    def exibir_entrada_codigo():
        """
        Exibe interface para entrada do código
        
        Returns:
            str: Código fonte inserido pelo usuário
        """
        st.subheader("📝 Entrada do Código")
        
        opcao = st.radio(
            "Escolha a forma de entrada:",
            ["📝 Usar Código Exemplo", "📤 Fazer Upload de Arquivo", "✏️ Digitar Código"]
        )
        
        if opcao == "📝 Usar Código Exemplo":
            st.code(EXEMPLO_CODIGO_C, language='c')
            return EXEMPLO_CODIGO_C
        
        elif opcao == "📤 Fazer Upload de Arquivo":
            return ComponentesInterface._carregar_arquivo()
        
        else:  # Digitar código
            return ComponentesInterface._obter_codigo_digitado()
    
    @staticmethod
    def _carregar_arquivo():
        """Carrega código fonte de arquivo .c"""
        arquivo = st.file_uploader("Selecione um arquivo .c", type=['c', 'h'])
        if arquivo is not None:
            codigo = arquivo.read().decode('utf-8')
            st.success(f"Arquivo '{arquivo.name}' carregado com sucesso!")
            st.code(codigo, language='c')
            return codigo
        return ""
    
    @staticmethod
    def _obter_codigo_digitado():
        """Obtém código fonte digitado pelo usuário"""
        return st.text_area("Digite seu código C:", value=EXEMPLO_CODIGO_C, height=300)
    
    @staticmethod
    def exibir_tokens(tokens):
        """Exibe a lista de tokens encontrados"""
        st.write("### Lista de Tokens")
        
        if not tokens:
            st.warning("Nenhum token encontrado!")
            return
        
        # Converter tokens para DataFrame
        dados_tokens = [token.to_dict() for token in tokens]
        df_tokens = pd.DataFrame(dados_tokens)
        st.dataframe(df_tokens, use_container_width=True)
        
        ComponentesInterface._exibir_estatisticas_tokens(tokens)
    
    @staticmethod
    def _exibir_estatisticas_tokens(tokens):
        """Exibe estatísticas sobre os tokens"""
        col1, col2, col3, col4 = st.columns(4)
        
        total_tokens = len(tokens)
        palavras_chave = len([t for t in tokens if t.tipo == 'PALAVRA_CHAVE'])
        identificadores = len([t for t in tokens if t.tipo == 'IDENTIFICADOR'])
        operadores = len([t for t in tokens if t.tipo == 'OPERADOR'])
        
        col1.metric("Total de Tokens", total_tokens)
        col2.metric("Palavras-chave", palavras_chave)
        col3.metric("Identificadores", identificadores)
        col4.metric("Operadores", operadores)
    
    @staticmethod
    def exibir_tabela_simbolos(tabela_simbolos):
        """Exibe a tabela de símbolos"""
        st.write("### Tabela de Símbolos")
        
        simbolos = tabela_simbolos.obter_todos()
        if not simbolos:
            st.warning("Nenhum símbolo na tabela!")
            return
        
        df_simbolos = pd.DataFrame(simbolos)
        st.dataframe(df_simbolos, use_container_width=True)
        st.metric("Símbolos Únicos", len(simbolos))
    
    @staticmethod
    def exibir_verificacao_erros(tokens, tabela_simbolos):
        """Exibe verificação de erros"""
        st.write("### Verificação de Erros")
        
        erros_token = len([t for t in tokens if t.tipo == 'ERRO'])
        
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
    

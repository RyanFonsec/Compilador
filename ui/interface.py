import streamlit as st
from .componentes import ComponentesInterface
from core.analisador import AnalisadorLexico


class InterfaceUsuario:
    """Gerencia a interface principal do usuário"""
    
    def __init__(self):
        self.analisador = AnalisadorLexico()
        self._configurar_pagina()
    
    def _configurar_pagina(self):
        """Configura a página do Streamlit"""
        st.set_page_config(
            page_title="Analisador Léxico - Linguagem C",
            page_icon="🔍",
            layout="wide"
        )
    
    def executar(self):
        """Executa a aplicação principal"""
        try:
            # Exibir cabeçalho
            ComponentesInterface.exibir_cabecalho()
            
            # Obter código fonte
            codigo_fonte = ComponentesInterface.exibir_entrada_codigo()
            
            # Executar análise se houver código
            if codigo_fonte and st.button("🚀 Analisar Código", type="primary"):
                self._executar_analise(codigo_fonte)
                     
        except Exception as e:
            st.error(f"❌ Erro na aplicação: {str(e)}")
            st.info("🔄 Recarregue a página e tente novamente")
    
    def _executar_analise(self, codigo_fonte):
        """Executa a análise léxica e exibe resultados"""
        with st.spinner("🔍 Analisando código C..."):
            tokens, tabela_simbolos = self.analisador.analisar(codigo_fonte)
        
        self._exibir_resultados(tokens, tabela_simbolos)
    
    def _exibir_resultados(self, tokens, tabela_simbolos):
        """Exibe os resultados da análise"""
        st.subheader("📋 Resultados da Análise Léxica")
        
        ComponentesInterface.exibir_tokens(tokens)
        ComponentesInterface.exibir_tabela_simbolos(tabela_simbolos)
        ComponentesInterface.exibir_verificacao_erros(tokens, tabela_simbolos)
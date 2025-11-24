# Funções utilitárias (pode ser expandido conforme necessidade)

def validar_codigo(codigo: str) -> bool:
    """
    Valida se o código não está vazio
    
    Args:
        codigo (str): Código fonte a ser validado
        
    Returns:
        bool: True se válido, False caso contrário
    """
    return bool(codigo and codigo.strip())

def formatar_erro(mensagem: str) -> str:
    """
    Formata mensagens de erro
    
    Args:
        mensagem (str): Mensagem de erro
        
    Returns:
        str: Mensagem formatada
    """
    return f"❌ {mensagem}"
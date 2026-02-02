

# Simulador de Renda: Transicao Carreira TI
# Regras: Bolsa Familia, Trilhas do Futuro e Estagio

def calcular_renda():
    bolsa_familia = 600.00 # Base
    ajuda_trilhas = 440.00 # Auxilio presencial Senai
    
    print("--- SIMULADOR DE RENDA HIGH LEVEL ---")
    salario_estagio = float(input("Digite o valor do estagio (ou 0): "))
    
    # Regra de Protecao: Mantem 50% se ganhar acima de 218
    if salario_estagio > 218.00:
        bolsa_familia = 300.00
        status = "Regra de Protecao Ativa (50%)"
    else:
        status = "Bolsa Familia Integral"
        
    total = bolsa_familia + ajuda_trilhas + salario_estagio
    
    print(f"\nStatus: {status}")
    print(f"Renda Total Estimada: R$ {total:.2f}")

if __name__ == "__main__":
    calcular_renda()


def calcular_simulador_social():
    print("\n" + "="*40)
    print("--- SIMULADOR DE RENDA E DIREITOS v2.0 ---")
    print("="*40)

    # 1. Entradas
    salario_estagio = float(input("\nDigite o valor do estágio (R$): "))
    num_pessoas = int(input("Quantas pessoas moram na residência? "))
    idade = int(input("Qual a sua idade? "))
    pcd = input("Possui alguma deficiência? (s/n): ").lower() == 's'
    
    # 2. Lógica BPC/LOAS (Regra de 1/4 do salário mínimo)
    salario_minimo = 1518.00
    renda_per_capita = salario_estagio / num_pessoas
    
    eligivel_bpc = (idade >= 65 or pcd) and (renda_per_capita <= (salario_minimo / 4))

    # 3. Lógica de Isenção (Bolsa Família/CadÚnico)
    tem_bolsa = input("Recebe Bolsa Família? (s/n): ").lower() == 's'
    isencao = "ELEGÍVEL" if tem_bolsa else "NÃO ELEGÍVEL"

    # 4. Cálculo de ROI (Investimento)
    print("\n--- Módulo de Investimento Imobiliário ---")
    custo_obra = float(input("Custo total da obra: "))
    aluguel = float(input("Aluguel mensal previsto: "))
    roi = ((aluguel * 12) / custo_obra) * 100 if custo_obra > 0 else 0

    # Resultados
    print("\n" + "="*40)
    print(f"Renda Per Capita:     R$ {renda_per_capita:.2f}")
    print(f"Direito ao BPC:       {'SIM' if eligivel_bpc else 'NÃO'}")
    print(f"Isenção Concursos:    {isencao}")
    print(f"Retorno Anual (ROI):  {roi:.2f}%")
    print("="*40)

if __name__ == "__main__":
    try:
        calcular_simulador_social()
    except ValueError:
        print("\nErro: Insira apenas números nos campos financeiros.")

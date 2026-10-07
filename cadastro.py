while True:
   
    print("Bem-vindo ao nosso sistema de cadastro! Por favor, preencha as informações abaixo:")
    nome = input("Qual é o seu nome? ")
    print("Olá, " + nome + "! Prazer em te conhecer!")
    idade = input("Qual é a sua idade? ")
    nomecompleto = input("Qual é o seu nome completo? ")
    logradouro = input("Qual o seu endereço? ")
    email = input("Qual o seu email? ")
    celular = input("Qual o seu número de celular? ")

    
    while True:
        cpf = input("Qual o seu CPF? (Apenas números): ").strip()   
        if not cpf.isdigit():
            print("Erro: Digite apenas números! Não use letras, pontos, hífens ou símbolos.")
            print("-" * 55)
            continue 
        if len(cpf) != 11:
            print(f"Erro: O CPF precisa ter exatamente 11 dígitos. Você digitou {len(cpf)}.")
            print("-" * 55)
            continue     
        cpf_final = cpf
        break  

    
    print("\n" + "="*20 + " CONFIRMAÇÃO DE DADOS " + "="*20)
    print(f"Nome Completo: {nomecompleto}")
    print(f"Idade:         {idade}")
    print(f"Endereço:      {logradouro}")
    print(f"E-mail:        {email}")
    print(f"Celular:       {celular}")
    print(f"CPF:           {cpf_final}")
    print("=" * 62)

    confirmação = input("Os dados estão corretos? (S para sim / N para não): ").strip().upper()
    
    if confirmação == "S":
        
        with open("usuarios_cadastrados.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Nome: {nomecompleto} | Idade: {idade} | CPF: {cpf_final} | Celular: {celular} | Email: {email} | Endereço: {logradouro}\n")
        print("Cadastro realizado com sucesso!")
        break  # Encerra o programa
    else:
        
        print("\nRepetindo o questionário... Vamos corrigir os dados.")
        print("=" * 62)

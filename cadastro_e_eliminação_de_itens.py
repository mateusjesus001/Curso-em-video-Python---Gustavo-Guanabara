def cadastro():
  # Inicializa um dicionário vazio
 cadastro_de_insumos_de_produção = {}

# Pede ao usuário para inserir chaves e valores até que eles desejem parar
 while True:
    insumosdeprodução = input("Digite um insumo de produção (ou digite 'parar' para encerrar): ")
    
    # Verifica se o usuário deseja parar
    if insumosdeprodução.lower() == 'parar':
        break
    
    quantidade = input(f"Digite a quantidade de '{insumosdeprodução}': ")
    
    # Adiciona a chave e o valor ao dicionário
    cadastro_de_insumos_de_produção[insumosdeprodução] = quantidade
 print('-='*35)


# Inicializa um dicionário vazio
 cadastro_de_insumos_de_embalagem = {}

# Pede ao usuário para inserir chaves e valores até que eles desejem parar
 while True:
    insumosdeembalagem = input("Digite um insumo de embalagem (ou digite 'parar' para encerrar): ")
    
    # Verifica se o usuário deseja parar
    if insumosdeembalagem.lower() == 'parar':
        break
    
    quantidade = input(f"Digite a quantidade de '{insumosdeembalagem}': ")
    
    # Adiciona a chave e o valor ao dicionário
    cadastro_de_insumos_de_embalagem[insumosdeembalagem] = quantidade

 cadastrogeral = cadastro_de_insumos_de_produção.copy()
 cadastrogeral.update(cadastro_de_insumos_de_embalagem)
 parar = 0
 while parar == 0:
   item = input('digite o item a ser eliminado: ').strip()
   resposta = 0
   if item in cadastrogeral:
    resposta = input('deseja excluir o item selecionado ? Sim/Não  ').upper()
    if resposta == 'SIM':
     del cadastrogeral[item]
     print('o item foi excluído com sucesso')
     
     exclusões = input('deseja continuar ? Sim/Não ').upper()
     if exclusões == 'SIM':
       parar = 0
     else: 
      if item in cadastrogeral:
       deletartodos = input('Existem mais insumos de mesmo nome no cadastro, deseja exclui-los ? Sim/Não  ').upper()
       if deletartodos == 'SIM':
        item_lista = [item]
        for i in item_lista:
         while i in cadastrogeral:
          del cadastrogeral[item]
       else:
         break
      print('Todos os itens idênticos foram deletados com sucesso !')
      break
    else:
     encerrar = input('deseja encerrar ? Sim/Não  ').upper()
     if encerrar == 'SIM':
      break
     else:
      resposta = input('deseja excluir o item selecionado ? Sim/Não  ').upper()
     if resposta == 'SIM':
      del cadastrogeral[item]
      print('o item foi excluído com sucesso')
      exclusões = input('deseja continuar ? Sim/Não ').lower()
      if exclusões == 'sim':
       item = input('digite o item a ser eliminado: ').strip()
       if item in cadastrogeral:
        resposta = input('deseja excluir o item selecionado ? Sim/Não  ').upper()
        if resposta == 'SIM':
         del cadastrogeral[item]
         print('o item foi excluído com sucesso')
        else:
         if item in cadastrogeral:
          deletartodos = input('Existem mais insumos de mesmo nome no cadastro, deseja exclui-los ? Sim/Não  ').upper()
          if deletartodos == 'SIM':
           item_lista = [item]
           for i in item_lista:
            while i in cadastrogeral:
             del cadastrogeral[item]
             print('Todos os itens idênticos foram deletados com sucesso !')
             break
         
          else:
           break
       

      else:
       if item in cadastrogeral:
        deletartodos = input('Existem mais insumos de mesmo nome no cadastro, deseja exclui-los ? Sim/Não  ').upper()
        if deletartodos == 'SIM':
         item_lista = [item]
         for i in item_lista:
          while i in cadastrogeral:
           del cadastrogeral[item]
           print('Todos os itens idênticos foram deletados com sucesso !')
           break
        else:
          break
       else:
         break
        
      break
       
     else:
      break
      

   else:
    print('o item selecionado não está no cadastro')
    tentativas = input('quer tentar denovo ? Sim/Não  ').upper()
    if tentativas == 'SIM':
      parar = 0
    else:
      parar = 1
 print(cadastrogeral)
cadastro()
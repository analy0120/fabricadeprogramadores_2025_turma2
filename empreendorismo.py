estoque = { "batom": [200, 10.00],
            "rimel": [100, 9.50],
            "blush": [260, 13.00],
            "iluminador": [500, 4.99],
            "sombra": [190, 15.60],
            "corretivo": [360, 18.90],
            "po": [400, 15.00],
            "curvex": [344, 20.00],
            "demaquilante": [230, 13.40],
            "base": [170, 22.50],
            "primer": [700, 11.90],
            "contorno": [234, 10.88],
            "gloss": [344, 4.90],
            "pincel": [700, 16.90],
            "hidratante": [190, 12.70],
            "fixador": [333, 18.90],
            "delineador": [456, 12.34],
            "paleta": [567, 23.99],
            "caneta": [133, 10.34],
            "mascara": [1550, 7.99], }
produto = input("digite o produto selecionado: ")
quantidade = int(input("digite a quantidade: "))
venda = [ [produto, quantidade] ]
total = 0 
if produto in estoque:
    print("vendas:\n")
    for operaçao in venda:
        produto, quantidade = operaçao # EMPREENDEDORISMO
        preço = estoque[produto][1]
        custo = preço * quantidade
        print("%12s: %3d x %6.2f = %6.2f" %
        (produto, quantidade,preço,custo))    
        estoque[produto][0] -= quantidade
        total+=custo
    else:
        print("nao temos este produto no estoque!")
    print("custo total: %21.2f\n" % total)
    primt("estoque:\n")
    for chave, dados in estoque.items ():
        print("descriçao: ", chave)
        print("quantidade: ", dados[0])
        print("preços: %6.2f\n" % dados[1])

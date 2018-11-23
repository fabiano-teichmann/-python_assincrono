import asyncio


async def tamanho_lista():
    print("Iniciando a função para contar tamanho de uma lista")

    await asyncio.wait([criando_lista()])
    
    # troca de contexto
    print('terminando')



async def criando_lista():
 	print('Iniciando a criação da lista')
 	l = []
 	for i in range(0, 100):
 		l.append(i)
 	return l

loop = asyncio.get_event_loop()
loop.run_until_complete(tamanho_lista())
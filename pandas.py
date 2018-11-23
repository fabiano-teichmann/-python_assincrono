import asyncio
from time import time


async  def empacotar_bala():
	print("Empacotando balas...")

	# parada para verificar se tem cliente no balcão
	await atender_balcao()

	# troca de contexto
	print("Explicitamente voltando a empacotar balas")


async def atender_balcao():
	print("Verifico se tem cliente")
	loop = asyncio.get_event_loop()
	loop.run_in_executor(None, count_100)
	print("Voltando a empacotar as balas")

def count_100():
	print('Contando 2 segundos')

	for i in range(0, 100):
		print(i)
ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(empacotar_bala())]

wait_tasks = asyncio.wait(tasks)

ioloop.run_until_complete(wait_tasks)
	


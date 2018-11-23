import asyncio


async  def empacotar_bala():
	print("Empacotando balas...")

	# parada para verificar se tem cliente no balcão
	await asyncio.sleep(2)

	# troca de contexto
	print("Explicitamente voltando a empacotar balas")


async def atender_balcao():
	print("Explicitamente verificando se tem cliente no balcão...")
	await asyncio.sleep(4)
	print("Voltando a empacotar as balas")


ioloop = asyncio.get_event_loop()  # Event Loop
while True:
	tasks = [ioloop.create_task(empacotar_bala()),
			 ioloop.create_task(atender_balcao())]

	wait_tasks = asyncio.wait(tasks)

	ioloop.run_until_complete(wait_tasks)
	


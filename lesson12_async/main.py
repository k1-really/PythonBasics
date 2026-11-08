#Async - делается в одном процессе. Более эффективно распределяется время за счет того, что выполняем другую задачу, а не простаиваем
#Многопоточка - создаются несколько потоков, в которых параллельно выполняются действия
import asyncio
import time


async def fetch_data(seconds):
    print("Начинаем запрос")
    await asyncio.sleep(2)
    print("Запрос прошел успешно!")

    return 42

async def main():
    print(fetch_data)
    start = time.time()
    print(await fetch_data(2))
    print(await fetch_data(4))
    end = time.time()
    print(f"Время выполнения: {end - start}")

asyncio.run(main())
import asyncio

async def add(a, b):
    print(f"Calculating {a} + {b}")
    await asyncio.sleep(1)  
    result = a + b
    print(f"Result of addition: {result}")
    return result

async def subtract(a, b):
    print(f"Calculating {a} - {b}")
    await asyncio.sleep(1)
    result = a - b
    print(f"Result of subtraction: {result}")
    return result

async def multiply(a, b):
    print(f"Calculating {a} * {b}")
    await asyncio.sleep(1) 
    result = a * b
    print(f"Result of multiplication: {result}")
    return result

async def divide(a, b):
    print(f"Calculating {a} / {b}")
    await asyncio.sleep(1) 
    if b == 0:
        print("Error: Division by zero")
        return None
    result = a / b
    print(f"Result of division: {result}")
    return result

async def main():
    a, b = 10, 5
    results = await asyncio.gather(
        add(a, b),
        subtract(a, b),
        multiply(a, b),
        divide(a, b)
    )
    print("\nAll results:", results)

if __name__ == "__main__":
    asyncio.run(main())

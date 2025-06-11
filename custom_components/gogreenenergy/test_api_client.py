# test_api_client.py
import asyncio
from .api_client import GoGreenEnergyApiClient

async def main():
    client = GoGreenEnergyApiClient()
    data = await client.fetch_price_data()
    print(data)

if __name__ == "__main__":
    asyncio.run(main())
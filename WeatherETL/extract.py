import pandas as pd
import json
import aiohttp
import asyncio

sitename = "https://www.met.no/en" 
baseUrl = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
latitude = 60.10
longitude = 9.58
url = f'{baseUrl}?lat={latitude}&lon={longitude}'

class UserAgent:
    def __init__(self, sitename):
        if not sitename or sitename.lower() in ['generic', 'default']:
            raise ValueError("Invalid sitename. You will receive a 403 Forbidden response.")
        self.sitename = sitename
        self.headers = {
            'User-Agent': f'{self.sitename}',
        }

    async def make_request(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as response:
                if response.status == 200:
                    json_data = await response.json()
                    data = pd.DataFrame(json_data)
                    print(data)

                    data.to_excel('output.xlsx', index=False)
                    print("Data saved to output.xlsx")
                else:
                    print(f"Failed to retrieve data. HTTP Status: {response.status}")

async def fetch_weather_data():
    user_agent = UserAgent(sitename)
    await user_agent.make_request(url)

if __name__ == "__main__":
    asyncio.run(fetch_weather_data())

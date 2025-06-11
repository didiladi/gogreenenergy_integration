class GoGreenEnergySensor:
    def __init__(self, api_client):
        self.api_client = api_client
        self._state = None

    @property
    def state(self):
        return self._state

    async def async_update(self):
        data = await self.api_client.fetch_price_data()
        self._state = data.get('price')  # Assuming the API returns a 'price' key

    async def async_setup(self):
        await self.async_update()
import aiohttp
from .const import DEFAULT_VAT

class GoGreenEnergyApiClient:
    URL = "https://www.gogreenenergy.at/.rest/calculator/v1/products?includeHistory=true&products=GSFLEX,GGFLEX"

    async def fetch_price_data(self, product_key="GSFLEX", options=("plus",), vat=DEFAULT_VAT):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.URL) as resp:
                data = await resp.json()
        product = next((p for p in data if p["key"] == product_key), None)
        if not product:
            return {}
        history = product.get("history", [])
        if not history:
            return {}
        latest = history[-1]
        base_price = latest["energyPrice"]
        total_price = base_price
        for opt in options:
            opt_data = product.get("options", {}).get(opt)
            if opt_data:
                total_price += opt_data.get("energyPrice", 0)
        # Apply VAT
        total_price_gross = total_price * (1 + vat)
        total_price_cents = round(total_price_gross * 100, 2)
        return {
            "period": f'{latest["fromDate"]} - {latest["untilDate"]}',
            "price": total_price_cents,
            "product": product["name"],
            "options": options
        }
from datetime import timedelta
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, CoordinatorEntity
from .api_client import GoGreenEnergyApiClient

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    api_client = GoGreenEnergyApiClient()

    async def async_update_data():
        return await api_client.fetch_price_data(product_key="GSFLEX", options=("plus",))

    coordinator = DataUpdateCoordinator(
        hass,
        name="GoGreenEnergy Price",
        update_method=async_update_data,
        update_interval=timedelta(hours=1),  # Update every hour
    )

    await coordinator.async_config_entry_first_refresh()
    sensor = GoGreenEnergySensor(coordinator)
    async_add_entities([sensor])

class GoGreenEnergySensor(CoordinatorEntity, Entity):
    def __init__(self, coordinator):
        super().__init__(coordinator)
        self._attr_name = "GoGreenEnergy Price"
        self._attr_unit_of_measurement = "Cent/kWh"

    @property
    def state(self):
        return self.coordinator.data.get("price")

    @property
    def extra_state_attributes(self):
        data = self.coordinator.data
        return {
            "period": data.get("period"),
            "product": data.get("product"),
            "options": ", ".join(data.get("options", []))
        }



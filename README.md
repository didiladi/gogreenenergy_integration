# GoGreenEnergy Home Assistant Integration

This custom integration provides a sensor for GoGreenEnergy electricity and gas prices in Home Assistant.

## Features

- Fetches current and historical prices for GoGreenEnergy products (electricity/gas)
- Supports options like "plus" and VAT calculation
- Updates price data once per hour (configurable)

## Installation

1. Copy the `gogreenenergy` folder to your Home Assistant `custom_components` directory.
2. Restart Home Assistant.

## Configuration

Add to your `configuration.yaml`:

```yaml
sensor:
  - platform: gogreenenergy
```

By default, the integration fetches the "strom flex plus" (GSFLEX + plus) electricity price.  
You can modify the code to support other products or options if needed.

## Dependencies

- `aiohttp` (installed automatically)
- `beautifulsoup4` (installed automatically, but not currently used)

## Notes

- The sensor updates once per hour to avoid unnecessary API calls.
- Prices are shown in Cent/kWh, including VAT.

## Credits

Created by [@didiladi](https://github.com/didiladi)
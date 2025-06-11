# GoGreenEnergy Home Assistant Integration

This repository contains a Home Assistant integration for fetching price data from GoGreenEnergy.

## Installation

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/yourusername/gogreenenergy_integration.git
   ```

2. Navigate to the `gogreenenergy_integration` directory:
   ```
   cd gogreenenergy_integration
   ```

3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

4. Copy the `custom_components` directory to your Home Assistant configuration directory:
   ```
   cp -r custom_components/gogreenenergy /config/custom_components/
   ```

## Configuration

To configure the GoGreenEnergy integration, add the following to your `configuration.yaml` file:

```yaml
sensor:
  - platform: gogreenenergy
    api_key: YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your actual API key from GoGreenEnergy.

## Usage

Once the integration is set up, you can restart Home Assistant. The GoGreenEnergy sensor will be available in your Home Assistant dashboard, providing real-time price data.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. 

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
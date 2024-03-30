# Google Analytics 360 Dataset Project

Welcome to the Google Analytics 360 Dataset Project! This repository is designed for anyone interested in working with realistic Google Analytics data. Whether you're a data scientist, a student, or a marketing analyst, this dataset offers a comprehensive glimpse into the type of data Google Analytics 360 can provide.

## Project Structure

- `analytics_data.json` - A JSON file containing a sample output of Google Analytics data, closely resembling real-world data.
- `user.py` - A customizable Python script for interacting with the data in `analytics_data.json`.

## Dataset Example

The `analytics_data.json` file provides a structured example of what Google Analytics data might look like, including visit IDs, user information, device details, geolocation, traffic sources, page hits, and more. Here is a brief overview:

```json
{
  "visitId": "1234567890",
  "visitStartTime": "2024-03-29T10:15:30.000Z",
  "date": "2024-03-29",
  "fullVisitorId": "7890123456789012345",
  "userId": "user_abc@email.com",
  "clientId": "1234.5678",
  "channelGrouping": "Paid Search",
  "socialEngagementType": "Socially Engaged",
  "device": {
    "browser": "Chrome",
    "browserVersion": "89.0.4389.9",
    "browserSize": "1920x1080",
    "operatingSystem": "Windows",
    "isMobile": false,
    "mobileDeviceInfo": {
      "mobileDeviceBranding": "Apple",
      "mobileDeviceModel": "iPhone 12 Pro",
      "mobileInputSelector": "touchscreen"
    }
  },
  "geoNetwork": {
    "continent": "Europe",
    "country": "France",
    "region": "Île-de-France",
    "city": "Paris",
    "networkDomain": "example.com"
  },
  "trafficSource": {
    "source": "google",
    "medium": "cpc",
    "campaign": "spring_sale",
    "keyword": "buy shoes online",
    "adContent": "50% Off Shoes",
    "isTrueDirect": false
  },
  "page": {
    "pagePath": "/products/shoes",
    "hostname": "www.example.com",
    "pageTitle": "Buy Shoes Online - Example.com"
  },
  "hits": [
    {
      "type": "PAGE",
      "time": "2024-03-29T10:15:35.000Z",
      "isEntrance": true,
      "isExit": false
    },
    {
      "type": "EVENT",
      "time": "2024-03-29T10:16:12.000Z",
      "eventCategory": "ecommerce",
      "eventAction": "add_to_cart",
      "eventLabel": "product_xyz"
    },
    {
      "type": "TRANSACTION",
      "time": "2024-03-29T10:18:25.000Z",
      "transactionId": "T12345",
      "transactionRevenue": 59.99,
      "transactionShipping": 5.99,
      "transactionTax": 4.2,
      "currencyCode": "EUR",
      "productInfo": {
        "productSKU": "SHOE_001",
        "productName": "Running Shoes",
        "productCategory": "Apparel/Shoes",
        "productPrice": 49.99,
        "productQuantity": 1
      }
    }
  ],
  "customDimensions": {
    "dimension1": "premium_user",
    "dimension2": "new_user"
  },
  "customMetrics": {
    "metric1": 25,
    "metric2": 75.25
  }
}
```

## Contributing

We welcome contributions to improve the dataset or the sample scripts! Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

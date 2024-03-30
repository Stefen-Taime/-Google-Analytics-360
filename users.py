import pandas as pd
from faker import Faker
from faker.providers import person, internet, date_time, address, user_agent
from datetime import datetime, timedelta
import random

departements_fr = pd.read_csv('fr.csv')

fake = Faker('fr_FR')
fake.add_provider(person)
fake.add_provider(internet)
fake.add_provider(date_time)
fake.add_provider(address)
fake.add_provider(user_agent)

def generate_data():
    departement = departements_fr.sample(1).iloc[0]

    visit_id = fake.uuid4()
    visit_start_time = fake.date_time_between(start_date='-1y', end_date='now')
    date = visit_start_time.date()
    full_visitor_id = fake.uuid4()
    user_id = fake.email()
    client_id = fake.uuid4()
    channel_grouping = fake.random_element(elements=('Paid Search', 'Organic Search', 'Direct', 'Referral', 'Social'))
    social_engagement_type = fake.random_element(elements=('Socially Engaged', 'Not Socially Engaged'))
    browser = fake.chrome()
    browser_version = f"Chrome {fake.random_int(min=50, max=99)}.{fake.random_int(min=0, max=3)}.{fake.random_int(min=1000, max=9999)}.{fake.random_int(min=50, max=99)}"
    browser_size = '1920x1080'
    operating_system = fake.random_element(elements=('Windows', 'macOS', 'Linux'))
    is_mobile = fake.boolean(chance_of_getting_true=30)
    mobile_device_info = {
        'mobileDeviceBranding': 'Apple',
        'mobileDeviceModel': 'iPhone 12 Pro',
        'mobileInputSelector': 'touchscreen'
    } if is_mobile else {}
    continent = 'Europe'
    country = 'France'
    region = departement['geoRegion']
    city = departement['geoCity']
    network_domain = 'example.com'
    source = fake.random_element(elements=('google', 'bing', 'yahoo', 'duckduckgo'))
    medium = fake.random_element(elements=('cpc', 'cpm', 'organic', 'referral'))
    campaign = fake.word() if medium in ('cpc', 'cpm') else None
    keyword = ' '.join(fake.words(nb=3)) if medium == 'cpc' else None
    ad_content = '50% Off' if medium == 'cpc' else None
    is_true_direct = True if medium == 'direct' else False
    page_path = '/products/' + fake.word()
    hostname = 'www.example.com'
    page_title = 'Buy ' + fake.word().capitalize() + ' Online - Example.com'
    hits = []
    for hit_type in ('PAGE', 'EVENT', 'TRANSACTION'):
        hit = {
            'type': hit_type,
            'time': fake.date_time_between(start_date=visit_start_time, end_date=visit_start_time + timedelta(hours=1)).isoformat() + 'Z',
            'isEntrance': True if hit_type == 'PAGE' else False,
            'isExit': False if hit_type == 'PAGE' else True
        }
        if hit_type == 'EVENT':
            hit['eventCategory'] = 'ecommerce'
            hit['eventAction'] = 'add_to_cart'
            hit['eventLabel'] = 'product_xyz'
        elif hit_type == 'TRANSACTION':
            hit['transactionId'] = 'T' + fake.uuid4().split('-')[-1]
            hit['transactionRevenue'] = str(fake.pydecimal(left_digits=2, right_digits=2, positive=True))
            hit['transactionShipping'] = str(fake.pydecimal(left_digits=1, right_digits=2, positive=True))
            hit['transactionTax'] = str(fake.pydecimal(left_digits=1, right_digits=2, positive=True))
            hit['productInfo'] = {
                'productSKU': 'SHOE_' + fake.uuid4().split('-')[-1][:4],
                'productName': 'Running Shoes',
                'productCategory': 'Apparel/Shoes',
                'productPrice': str(fake.pydecimal(left_digits=2, right_digits=2, positive=True)),  
                'productQuantity': fake.random_int(min=1, max=5)
            }
            hit['currencyCode'] = 'EUR'
        hits.append(hit)
    custom_dimensions = {
        'dimension1': 'premium_user' if fake.boolean(chance_of_getting_true=30) else 'regular_user',
        'dimension2': 'new_user' if fake.boolean(chance_of_getting_true=20) else 'returning_user'
    }
    custom_metrics = {
    'metric1': fake.random_int(min=0, max=100),
    'metric2': str(fake.pydecimal(left_digits=2, right_digits=2, positive=True))
}


    return {
        'visitId': visit_id,
        'visitStartTime': visit_start_time.isoformat() + 'Z',
        'date': date.isoformat(),
        'fullVisitorId': full_visitor_id,
        'userId': user_id,
        'clientId': client_id,
        'channelGrouping': channel_grouping,
        'socialEngagementType': social_engagement_type,
        'device': {
            'browser': browser,
            'browserVersion': browser_version,
            'browserSize': browser_size,
            'operatingSystem': operating_system,
            'isMobile': is_mobile,
            'mobileDeviceInfo': mobile_device_info
        },
        'geoNetwork': {
            'continent': continent,
            'country': country,
            'region': region,
            'city': city,
            'networkDomain': network_domain
        },
        'trafficSource': {
            'source': source,
            'medium': medium,
            'campaign': campaign,
            'keyword': keyword,
            'adContent': ad_content,
            'isTrueDirect': is_true_direct
        },
        'page': {
            'pagePath': page_path,
            'hostname': hostname,
            'pageTitle': page_title
        },
        'hits': hits,
        'customDimensions': custom_dimensions,
        'customMetrics': custom_metrics
    }

data = [generate_data() for _ in range(1000)]

import json
with open('analytics_data.json', 'w') as f:
    json.dump(data, f, indent=2)
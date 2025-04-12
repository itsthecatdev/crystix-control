import os
import yaml
from pathlib import Path
from collections import defaultdict

def load_fixtures(base_path='crystix/fixture'):
    fixtures = defaultdict(dict)
    base = Path(base_path)

    if not base.exists():
        print(f"[!] Directory not found: {base.resolve()}")
        return fixtures

    for manufacturer_dir in base.iterdir():
        #print(f"Scanning manufacturer: {manufacturer_dir}")  # DEBUG
        if manufacturer_dir.is_dir():
            manufacturer = manufacturer_dir.name
            for fixture_file in manufacturer_dir.glob('*.yaml'):
                #print(f"  Found fixture: {fixture_file}")  # DEBUG
                fixture_name = fixture_file.stem
                with open(fixture_file, 'r') as f:
                    data = yaml.safe_load(f)
                    fixtures[manufacturer][fixture_name] = data
    return fixtures
def get_channels(fixture_data):
    return fixture_data.get('channels', {})

def get_channel_count(fixture_data):
    return fixture_data.get('channels', {}).get('count', 0)

def get_channel_highlight(fixture_data):
    return fixture_data.get('channels', {}).get('hightlight', [])

def get_channel_config(fixture_data):
    return fixture_data.get('channel_config', {})

def get_channel_details(fixture_data, channel_number):
    config = get_channel_config(fixture_data)
    return config.get(channel_number, {})
def get_loaded_fixtures(fixtures):
    if not fixtures:
        print("[!] No fixtures loaded. Check the directory structure.")
        return
    
    max_manufacturer_len = max(len(manufacturer) for manufacturer in fixtures)
    max_fixture_len = max(len(fixture_id) for manufacturer in fixtures.values() for fixture_id in manufacturer)
    
    # Add extra space between the columns
    manufacturer_width = max_manufacturer_len + 5
    fixture_width = max_fixture_len + 5

    print(f"{'Manufacturer':<{manufacturer_width}} | {'Fixture ID':<{fixture_width}}")
    print('-' * (manufacturer_width + fixture_width + 3))

    for manufacturer, fixture_dict in fixtures.items():
        for fixture_id in fixture_dict:
            print(f"{manufacturer:<{manufacturer_width}} | {fixture_id:<{fixture_width}}")

import requests


def get_place_info(api_key, latitude, longitude):
    # Send a request to the Places API
    response = requests.get(
        'https://maps.googleapis.com/maps/api/place/nearbysearch/json',
        params={
            'location': f'{latitude},{longitude}',
            # 'radius': 50,  # Adjust this value as needed
            'key': api_key,
            'rankby': 'distance',
            'keyword': 'Posto Marechal  25 Kw',
            'language': 'pt-BR'
        }
    )

    # If the request was successful, extract the data
    if response.status_code == 200:
        data = response.json()

        # If a result was found, extract the address, name, and photo reference
        if data['results']:
            # save json results to file
            with open('results.json', 'w') as f:
                f.write(response.text)

            result = data['results'][0]
            address = result.get('vicinity')
            name = result.get('name')
            photo_ref = result['photos'][0]['photo_reference'] if 'photos' in result else None

            # Get the city and state from the address
            # This assumes the address is in the format "Street, City, State"
            parts = address.split(',')
            city = parts[1].strip() if len(parts) > 1 else None
            state = parts[2].strip() if len(parts) > 2 else None

            # Get the photo from the photo reference
            if photo_ref:
                photo_response = requests.get(
                    'https://maps.googleapis.com/maps/api/place/photo',
                    params={
                        'maxwidth': 400,  # Adjust this value as needed
                        'photoreference': photo_ref,
                        'key': api_key,
                    }
                )
                if photo_response.status_code == 200:
                    with open('photo.jpg', 'wb') as f:
                        f.write(photo_response.content)

            return address, city, state, name

    return None, None, None, None


# Replace with your API key, latitude, and longitude
api_key = 'AIzaSyD9e3nrisuqL81nqUYa7BEVMeIMqCX1HQo'
latitude = '-26.897434'
longitude = '-49.231515'
address, city, state, name = get_place_info(api_key, latitude, longitude)

print(f'Address: {address} City: {city} State: {state} Name: {name}')

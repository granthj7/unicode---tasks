import requests
from django.http import JsonResponse
import json
from django.shortcuts import render
def pokemon_types(request):
    try:
        api_url = "https://pokeapi.co/api/v2/type/"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            types = []

            for type_data in data['results']:
                type_name = type_data['name']
                type_url = type_data['url']

                type_response = requests.get(type_url)
                if type_response.status_code == 200:
                    type_info = type_response.json()
                    pokemon_names = [pokemon['pokemon']['name'] for pokemon in type_info['pokemon']]
                    types.append({'type': type_name, 'pokemon_names': pokemon_names})
                else:
                    types.append({'type': type_name, 'pokemon_names': []})

            response_data = {'pokemon_types': types}
            return JsonResponse(response_data, json_dumps_params={'indent': 1})

        else:
            return JsonResponse({'error': 'Unable to fetch Pokémon types'}, status=500)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
def select_pokemon_type(request):
    alltypes = gettypes()
    print(alltypes)
    if request.method == 'POST':
        selected_type = request.POST.get('pokemon_type')
        api_url = f"https://pokeapi.co/api/v2/type/{selected_type}"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            pokemon_names = [pokemon['pokemon']['name'] for pokemon in data['pokemon']]
        else:
            pokemon_names = []
        return render(request, 'results.html', {'pokemon_names': pokemon_names, 'selected_type': selected_type})
    return render(request, 'types.html')

def gettypes():
    try:
        api_url = "https://pokeapi.co/api/v2/type/"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            types = [type_data['name'] for type_data in data['results']]
            return types
        else:
            return []

    except Exception as e:
        print(f"Error: {e}")
        return []














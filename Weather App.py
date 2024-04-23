#Simple Weather App
#Made By Geoff Ribu


#importing request package to allow for API calls
import requests
#importing GUI creator
import PySimpleGUI as sg

api_key = 'd4d303a1d63c7aaa12e0ba41456a764d'

sg.theme('DarkTeal7')

def DrawMenu ():
    layout = [  [sg.Text('Enter City Name:')],
                [sg.InputText()],
                [sg.Button('Show me the weather!')],
                [sg.Text()],
                [sg.Button('Cancel')]
    ]

    return sg.Window('JJ\'s Weather App', layout, element_justification='c')

def DrawWeather (city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temperature_c = round(data['main']['temp'] - 273.15, 2)

        reaction = ReactToTemp(temperature_c)

        layout = [  [sg.Text(f'Temperature: {temperature_c}(C)')],
                    [sg.Text(reaction)],
                    [sg.Text(f'Humidity: {data['main']['humidity']}%')],
                    [sg.Text()],
                    [sg.Button('Return to menu')]
        ]

        return sg.Window(f'Weather in {city}', layout, element_justification='c')
    else:
        layout = [  [sg.Text(f'{city} is invalid...')],
                    [sg.Text()],
                    [sg.Button('Return to menu')]
        ]
        return sg.Window(f'Error', layout, element_justification='c')

def ReactToTemp (temp):
    if 20 < temp < 22:
        return 'PERFECT!!!!!!!'
    elif temp <= 20:
        return 'TOO COLD BRRRRRR...'
    else:
        return '*burning noises*'

window = DrawMenu()
city = 'Auckland'
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

    if event == 'Show me the weather!':
        window.close()
        window = DrawWeather(values[0])
        
        
    
    if event == 'Return to menu':
        window.close()
        window = DrawMenu()
        









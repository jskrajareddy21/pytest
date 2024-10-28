import requests

def len_joke():
    joke = get_joke()
    return len(joke)

def get_joke():
    # url = 'https://api.api-ninjas.com/v1/jokes'
    #
    # response = requests.get(url)
    #
    # print(response.status_code)
    # if response.status_code == 200:
    #     joke = response.json()['value']['joke']
    # else:
    #     joke = 'No joke'
    YOUR_API_KEY = ''
    #limit = 3
    api_url = 'https://api.api-ninjas.com/v1/jokes'
    response = requests.get(api_url, headers={'X-Api-Key': YOUR_API_KEY})
    if response.status_code == requests.codes.ok:
        joke = response.content
    else:
        print("Error:", response.status_code, response.text)
        joke = 'no joke'
    return joke

if __name__ == '__main__':
    print(get_joke())
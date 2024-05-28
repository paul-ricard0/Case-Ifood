import requests
import pandas as pd
import dotenv
import os

dotenv.load_dotenv()
GITHUB_USER = 'marciocl'
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = { "Authorization": f"token {GITHUB_TOKEN}"}

def clean_company(company:str) -> str:
    """
    Remove o caractere '@' do início do nome da empresa, se presente.
    """
    if company and company.startswith('@'):
        return company[1:]
    return company

def transform_date(date_str:str) -> str:
    """
    Transforma uma string de data no formato 'AAAA-MM-DDTHH:MM:SSZ' para o formato 'DD/MM/AAAA'.
    """
    return pd.to_datetime(date_str).strftime('%d/%m/%Y')

def get_follower_details(followers:list) -> list:
    """
    Obtém detalhes dos seguidores a partir de uma lista de URLs e retorna uma lista de dicionários com os dados.

    Args:
        followers (list): Uma lista de dicionários contendo informações dos seguidores, incluindo URLs.

    Returns:
        list: Uma lista de dicionários contendo detalhes dos seguidores.
    """
    user_data = []
    for follower in followers:
        user_url = follower['url']
        response = requests.get(user_url, headers=HEADERS)
        if response.status_code == 200:
            user_info = response.json()
            
            print(f"Request follower: {user_info.get('name')}")
            user_data.append({
                'name': user_info.get('name'),
                'company': clean_company(user_info.get('company')),
                'blog': user_info.get('blog'),
                'email': user_info.get('email'),
                'bio': user_info.get('bio'),
                'public_repos': user_info.get('public_repos'),
                'followers': user_info.get('followers'),
                'following': user_info.get('following'),
                'created_at': transform_date(user_info.get('created_at'))
            })
        else:
            print("Erro request em follower")
    return user_data

if __name__ == '__main__':   
    # Request 1
    followers_url = f"https://api.github.com/users/{GITHUB_USER}/followers"
    response = requests.get(followers_url, headers=HEADERS)

    if response.status_code == 200:
        print(f"Request feito com sucesso em {GITHUB_USER}")
        # Request 2
        followers = response.json()
        user_data = get_follower_details(followers)
        
        
        df = pd.DataFrame(user_data).astype({'name': str,
                                            'company': str,
                                            'blog': str,
                                            'email': str,
                                            'bio': str,
                                            'public_repos': int,
                                            'followers': int,
                                            'following': int,
                                            'created_at': str}) 
        
        print("Salvando dados em .csv")
        
        file_path = r"data\dados.csv"
        df.to_csv(file_path, index=False)

        print("Pipe finalizado com SUCESSO!!")
    else:
        print(f"Erro ao acessar a API: {response.status_code}")
        
    
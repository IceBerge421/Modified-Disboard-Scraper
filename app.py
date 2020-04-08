import pandas as pd
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}
tag = "debate"

servers = []
for page in range(1, 16):
    url = f"https://disboard.org/servers/tag/{tag}/{page}?sort=-member_count"
    request = Request(url, headers=headers)
    content = urlopen(request)
    soup = BeautifulSoup(content, 'html.parser')
    for server_info in soup.find_all(class_='server-info'):
        server_name = server_info.find(class_="server-name")
        server_name_link = server_name.find('a')
        server_online = server_info.find(class_="server-online")

        parent = server_info.parent.parent
        tags = []
        for tag_ in parent.find_all(class_="tag"):
            tag_name = tag_.find(class_="name")
            tags.append(tag_name.contents[0].strip())
        try:  # Dirty hack. Too lazy to use hasattr.
            members_online_count = server_online.contents[0].strip()
        except AttributeError as err_info:
            members_online_count = "N/A"
        server = [
            server_name_link.contents[0].strip(),
            members_online_count
        ]
        server.extend(tags)
        servers.append(server)

df = pd.DataFrame(
    servers,
    columns=[
        'Server Name',
        'Members Online',
        'Tag 1',
        'Tag 2',
        'Tag 3',
        'Tag 4',
        'Tag 5'
    ]
)
print("Creating output file...")
df.to_csv('servers.csv', index=False, encoding='utf-8')

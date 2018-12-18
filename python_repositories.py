"""This module represents an application collecting information of the most starred GitHub python projects
and saving it in the form of diagram"""

# import
import requests
import pygal

# create api request and save response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print('Status code:', r.status_code)  # status_code stores indication of request successful execution (code - 200)

# save api response
response_dict = r.json()  # api returns its response in the json format (dictionary)
print('Total repositories:', response_dict['total_count'])

# analysis of information about repositories
repositories_dicts = response_dict['items']
names, plot_dicts = [], []
for repository_dict in repositories_dicts:
    names.append(repository_dict['name'])
    description = repository_dict['description']
    if not description:
        description = 'No description provided.'
    plot_dict = {'value': repository_dict['stargazers_count'], 'label': description,
                 'xlink': repository_dict['html_url']}
    plot_dicts.append(plot_dict)

# create configuration object for visualization
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 18
my_config.label_font_size = 12
my_config.major_label_font_size = 14
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

# create visualization
chart = pygal.Bar(my_config, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_most_starred_github_repositories.svg')

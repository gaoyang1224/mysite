import yaml

with open("python36.yaml", encoding= 'utf-8') as f:
    data = yaml.load(f,Loader=yaml.SafeLoader)

print(data)
print(data['db']['port'])
print(data['user'][0]['password'])
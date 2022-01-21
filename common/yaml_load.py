import yaml
#封装读yaml文件

def load(path):
    file = open(path,'r',encoding='utf-8')
    data = yaml.load(file,Loader=yaml.FullLoader)
    return data

if __name__ == '__main__':
    print(load('../test_data/tunnel_Large_screen.yaml'))
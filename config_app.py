import json

def func1(config_file):
    file = open(config_file)
    data = json.load(file)

    config_text = open("config_nvdsanalytics.txt","w")

    for key, value in data.items():
        config_text.write('[{key}]\n'.format(key=key))
    
        config_text = open("config_nvdsanalytics.txt", "a")

        for key,value in value.items():
            config_text.write(
                '{key}={value}\n'.format(key=key,value=value))
            
        config_text.write("\n")

    config_text.close()
    config_text.close()

    
func1('config.json')


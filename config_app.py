import json

def func1(config_file):
    file = open(config_file)
    data = json.load(file)

    config_text = open("config_nvdsanalytics.txt","w")
    config_text.close()
    config_text = open("config_nvdsanalytics.txt", "a")

    for key, value in data.items():
        
        config_text.write('[{key}]\n'.format(key=key))

        for key,value in value.items():
            if type(value) is list:
                list_value = []
                for element in value:
                    list_value.append(str(element))
                    list_type_value = ";".join(list_value)
                config_text.write(
                    '{key}={list_type_value}\n'.format(key=key,list_type_value=list_type_value))
            else:
                config_text.write(
                '{key}={value}\n'.format(key=key,value=value))
            
        config_text.write("\n")

    config_text.close()

    
func1('config.json')


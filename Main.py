import json

inputs = ['decoys.json', 'prompts.json']
original = ['Drawful2Decoy.jet','Drawful2Prompt.jet']
outputs = ['Drawful2DecoyES.jet', 'Drawful2PromptES.jet']


def read_json(input_json, encoding='utf-8'):
    with open(input_json, "r", encoding=encoding) as read_file:
        return json.load(read_file)


def format_new_file(i):

    if i == 1:
        aux = {
            "content": [

            ],
            "episodeid":1239
        }
    else:
        aux = {
            "content": []
        }

    print("Formatting new input: {0}".format(inputs[i]))

    developer = read_json(inputs[i])
    for value in developer['{0}'.format(inputs[i][:-5])]:

        if i == 1:
            value['text'] = value['questionText']
            aux['content'].append(
                {"x":value['adultContent'],"id":value['id'],"text":value['text']}
            )
        else:
            aux['content'].append({"id":value['id'],"x": value['adultContent'],"text":value['text']})

    #print(aux)

    return aux


def add_missing(formatted, index):

    aux = formatted
    og = read_json(original[index], encoding='utf-8-sig')

    for o in og['content']:
        found = False

        for f in formatted['content']:
            if o['id'] == f['id']:
                found = True
                break

        if not found:
            aux['content'].append(o)

    return formatted


def export(data, index, encoding='utf-8'):
    print(data['content'][1])
    with open(outputs[index], 'w', encoding=encoding) as fp:
        json.dump(data, fp, ensure_ascii=False)


for i in range(0, len(inputs)):
    formatted = format_new_file(i)
    export(add_missing(formatted, i),i)




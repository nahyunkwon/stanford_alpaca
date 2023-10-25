import pandas as pd
import json

def create_seed_task_jsonl(csv_file='seed_tasks_access.csv', output_filename='seed_tasks_access.jsonl'):
    """
    create seed task jsonl file out of human-generated seed task csv file
    """

    tasks = pd.read_csv(csv_file)

    lines = []

    # task_format = {
    #     "id": "",
    #     "name": "",
    #     "instruction": "",
    #     "instances": [
    #         {
    #         "input": "",
    #         "output": ""
    #         }
    #     ],
    #     "is_classification": False
    # }

    for i in range(len(tasks)):
        print(i)
        task_format = {}
        task_format['id'] = "seed_task_" + str(tasks.iloc[i]['id'])
        task_format['name'] = tasks.iloc[i]['name']
        task_format['instruction'] = tasks.iloc[i]['instruction']
        
        instance = {}
        instance['input'] = tasks.iloc[i]['input']
        instance['output'] = tasks.iloc[i]['output']
        task_format['instances'] = [instance]

        if tasks.iloc[i]['is_classification']:
            is_classification = bool(True)
        else:
            is_classification = bool(False)
        task_format['is_classification'] = is_classification

        lines.append(task_format)

    print(lines)

    with open(output_filename, 'w') as file:
        for line in lines:
            json.dump(line, file)
            file.write("\n")



def main():
    create_seed_task_jsonl()



if __name__ == "__main__":
    main()
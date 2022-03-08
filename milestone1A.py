from datetime import datetime
import time
import yaml


def yaml_loader():
    with open("Milestone1/Milestone1A.yaml") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data


def log_task(flow_name, task_name, msg):
    log(f'{flow_name}.{task_name} {msg}')


def dispatch_flow(flow_name, activities):
    for task_name in activities.keys():
        task = activities.get(task_name)

        if task.get('Type') == 'Task':
            dispatch_sequential_tasks(flow_name, task_name, task)
        if task.get('Type') == 'Flow':
            log_flow(f'{flow_name}.{task_name}', task)





def dispatch_concurrent_tasks(flow):
    pass


def log(msg):
    print(f'{datetime.now()};{msg}')
    msg = f'{datetime.now()};{msg}\n'
    with open('res.txt', 'a') as f:
        f.write(msg)


def log_flow(flow_name, flow):
    log(f'{flow_name} Entry')
    flow_type = flow.get('Type')

    if flow_type is None:
        return

    if flow_type.lower() == 'flow':
        dispatch_flow(flow_name, flow.get('Activities'))

    log(f'{flow_name} Exit')


def main():
    pipeline = yaml_loader()

    for key in pipeline.keys():
        log_flow(key, pipeline[key])


main()
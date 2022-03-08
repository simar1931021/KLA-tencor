from datetime import datetime
import main


def yaml_lader():
    return {
        'M1A_Workflow': {
            'Type': 'Flow',
            'Execution': 'Sequential',
            'Activities': {
                'TaskA': {
                    'Type': 'Task',
                    'Function': 'TimeFunction',
                    'Inputs': {'FunctionInput': 'TaskA_Input', 'ExecutionTime': '1'}
                },
                'TaskB': {
                    'Type': 'Task',
                    'Function': 'TimeFunction',
                    'Inputs': {'FunctionInput': 'TaskB_Input', 'ExecutionTime': '2'}
                },
                'FlowA': {
                    'Type': 'Flow',
                    'Execution': 'Sequential',
                    'Activities': {
                        'TaskC': {
                            'Type': 'Task',
                            'Function': 'TimeFunction',
                            'Inputs': {'FunctionInput': 'TaskC_Input', 'ExecutionTime': '3'}
                        },
                        'TaskD': {
                            'Type': 'Task',
                            'Function': 'TimeFunction',
                            'Inputs': {'FunctionInput': 'TaskD_Input', 'ExecutionTime': '4'}
                        }
                    }
                }
            }
        }
    }


def log_task(flow_name, task_name, msg):
    log(f'{flow_name}.{task_name} Executing {msg}')


def dispatch_flow(flow_name, activities):
    for task_name in activities.keys():
        task = activities.get(task_name)

        if task.get('Type') == 'Task':
            dispatch_sequential_tasks(flow_name, task_name, task)
        if task.get('Type') == 'Flow':
            log_flow(task_name, task)


def dispatch_sequential_tasks(flow_name, task_name, task):
    log_task(flow_name, task_name, 'Entry')
    function_name = task.get('Function')
    function_args = ", ".join(list(task.get('Inputs').values()))
    log_task(flow_name, task_name, f'{function_name}({function_args})')
    log_task(flow_name, task_name, 'Exit')


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
    pipeline = yaml_lader()

    for key in pipeline.keys():
        log_flow(key, pipeline[key])


main()

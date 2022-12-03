
def check_operation(id, details):
    global ordering
    authorized = False
    # print(f"[debug] checking policies for event {id}, details: {details}")
    print(f"[info] checking policies for event {id},"\
          f" {details['source']}->{details['deliver_to']}: {details['operation']}")
    src = details['source']
    dst = details['deliver_to']
    operation = details['operation']
    
    if src == 'drone_status' and dst == 'mobile_connection' \
        and operation == 'info':
        authorized = True  
    if src == 'mobile_connection' and dst == 'drone_status' \
        and operation == 'drone_start':
        authorized = True   
    if src == 'drone_status' and dst == 'control_center' \
        and operation == 'task_add':
        authorized = True   
    if src == 'control_center' and dst == 'drone_status' \
        and operation == 'task_response':
        authorized = True   
              
    if src == 'control_center' and dst == 'mobile_connection' \
        and operation == 'task_info':
        authorized = True   
    if src == 'drone_status' and dst == 'mobile_connection' \
        and operation == 'job_error':
        authorized = True  
    if src == 'drone_status' and dst == 'control_center' \
        and operation == 'job_error':
        authorized = True 
    if src == 'mobile_connection' and dst == 'drone_status' \
        and operation == 'status_request':
        authorized = True   
    if src == 'drone_status' and dst == 'mobile_connection' \
        and operation == 'status_response':
        authorized = True   
    if src == 'mobile_connection' and dst == 'drone_status' \
        and operation == 'drone_to_home':
        authorized = True 
    if src == 'drone_status' and dst == 'control_center' \
        and operation == 'task_completed':
        authorized = True 

    if src == 'drone_status' and dst == 'sprayer_control' \
        and operation == 'on_sprayer':
        authorized = True 
    if src == 'sprayer_control' and dst == 'flying_control' \
        and operation == 'sprayer_condition':
        authorized = True 
    if src == 'drone_status' and dst == 'situation_control' \
        and operation == 'check_earth':
        authorized = True 
    if src == 'drone_status' and dst == 'control_center' \
        and operation == 'task_completed':
        authorized = True 

    return authorized
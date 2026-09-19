import csv 
def report_generator(unsafe_logs,report_file_path):
    if not unsafe_logs:
        print('system is secure.')
        return
    else:
        headers=unsafe_logs[0].keys()
        with open(report_file_path,'w',newline='',encoding='utf-8') as f:
            writer=csv.DictWriter(f,fieldnames=headers)
            writer.writeheader()
            writer.writerows(unsafe_logs)
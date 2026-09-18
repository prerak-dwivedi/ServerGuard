def log_parser(file):
    with open(file, 'r', encoding='utf-8') as f:
        clean_logs=[]
        corrupt_logs=[]
        for line in f:
            ip,path,status=0,0,0
            i=line.split('"')
            i.pop(-1)
            if i:
                if len(i[0].split()) > 3:
                    ip=(i[0].split())[0]
                    if len(i[1].split()) >=3: 
                        path=(' '.join(i[1].split()[1:-1]))
                        if len(i[2].split()) == 2:
                            status=(i[2].split()[0])
                            data={'ip address':ip,'path':path,'status':status}
                            clean_logs.append(data)
            if not(ip and path and status):
                corrupt_logs.append(line)
    return(clean_logs,corrupt_logs)
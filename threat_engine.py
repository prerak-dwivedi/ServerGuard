def threat_detector(clean_logs,suspicious_keywords):
    unsafe_logs=[]
    for log in clean_logs:
        path=log['path']
        for keyword in suspicious_keywords:
            if keyword.lower() in path.lower():
                unsafe_logs.append(log)
                break
    return (unsafe_logs)
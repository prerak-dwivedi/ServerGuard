def error_log(corrupt_log_file,corrupt_log_variable):
    with open(corrupt_log_file,'a') as f:
        for i in corrupt_log_variable:
            f.write(i+'\n')
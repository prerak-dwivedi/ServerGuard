import csv
import config
from parser import log_parser
from error_logger import error_log
from threat_engine import threat_detector
from reporter import report_generator
(clean_data,corrupt_data)=log_parser(config.log_file_path)
error_log(config.failed_log_file_path,corrupt_data)
flagged_logs=threat_detector(clean_data,config.suspicious_keywords)
report_generator(flagged_logs,config.report_file_path)
print("execution complete!")
print(f"clean logs parsed: {len(clean_data)}")
print(f"corrupt logs separated: {len(corrupt_data)}")
print(f"threats detected: {len(flagged_logs)}")
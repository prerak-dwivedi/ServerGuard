# Project: ServerGuard - Log Analysis Engine



## Problem Statement

System administrators and security teams struggle to manually review massive web server log files to identify malicious activities such as SQL injections, Cross-Site Scripting (XSS), or brute-force login attempts. Manual analysis is slow, error-prone, and leaves servers vulnerable to delayed threat detection.

## 

## Scope of the Project

This project is modular, procedural Python application designed to automate first-line security auditing. The system takes standard web server logs, cleanly extracts data like IP addresses and HTTP requests, and evaluates them against predefined threat signatures. The scope includes handling of corrupted data without crashing and outputting a final structured CSV report of flagged abnormalities.

## 

## Target Users

Cybersecurity analysts monitoring network traffic for intrusion attempts.

System administrators checking server health and identifying malicious IPs.

IT students or researchers needing a lightweight tool to analyze dummy server data.

## 

## High-Level Features

**Automated Log Ingestion:** Reads and parses server log files line by line for performance and reduced memory usage.

**Threat Detection:**logic to flag specific attack types, including SQL injection (SQLi), XSS, and brute force anomalies.

**Fault Tolerant Error Handling:** Safely catches skips and logs the corrupted or malformed text lines without stopping the main app.

**Automated Reporting:**a structured CSV alert file summarizing the identified threats is generated.


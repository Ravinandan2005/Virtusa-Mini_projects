# OpsBot - Security Alert Log Filter

## Overview

OpsBot is a Python automation tool designed for IT Operations teams to automate the detection and filtering of security-critical log entries. Instead of manually reviewing thousands of daily log entries, OpsBot automatically identifies and isolates critical issues such as failed login attempts, errors, and system-critical events.

## Business Context

IT Operations teams managing production servers generate massive volumes of log data daily (typically 5,000+ lines). Manual review to identify security threats like failed login attempts is time-consuming, taking approximately 2 hours per day. OpsBot addresses this by automating the filtering process, enabling teams to focus on actual security incidents rather than noise.

## Problem Statement

The tool solves the following challenges:
- Filter noise (informational messages) from server logs
- Identify security-relevant events (CRITICAL, ERROR, FAILED LOGIN)
- Generate consolidated security alert reports with frequency counts
- Confirm successful alert file creation and size

## Features

1. **Automated Log Parsing** - Reads raw log files line by line
2. **Multi-Pattern Detection** - Identifies three security keywords:
   - CRITICAL: System-level critical failures
   - ERROR: Operational errors
   - FAILED LOGIN: Authentication failures indicating potential attacks
3. **Frequency Tracking** - Maintains count dictionary for each alert type
4. **Report Generation** - Outputs filtered alerts to timestamped security_alert_[date].txt files
5. **Verification** - Displays file size confirmation for generated reports

## Installation

No external dependencies required. The script uses only Python standard library modules:
- `os` - File operations and size verification
- `datetime` - Timestamp generation

## Usage

```bash
python opsbot.py
```

The script reads from the configured log file (default: ensora.log) in the same directory and produces output in the output/ folder.

## Input/Output

**Input:** ensora.log (or any configured log file)
- Format: Pipe-delimited or space-separated log entries
- Expected structure: [timestamp] | [level] | [message]
- Can contain any log format as long as keywords are present

**Output:** output/security_alert_[date].txt
- Contains all lines matching CRITICAL, ERROR, or FAILED LOGIN keywords
- One alert per line
- Timestamp-named for daily tracking

**Console Output:** Security Alert Summary
- Count of each alert type detected
- Output file path and size in bytes

## Testing

Sample test results with 138-line log file:
- ERROR count: 30
- CRITICAL count: 11
- FAILED LOGIN count: 7
- Output file: 3,948 bytes containing 48 security alert lines

## Requirements Met

1. File Parsing - Reads log file line by line with strip()
2. Pattern Matching - Uses 'in' operator for keyword detection
3. Data Structuring - Dictionary-based frequency counting
4. Report Generation - Writes filtered logs to timestamped file
5. Automation - Uses os module for file size confirmation

## Log Data Source

The sample log file (ensora.log) is sourced from Ensora AI, a production web application created and hosted at https://ensora-ai.vercel.app/. The logs reflect real server operations including API requests, authentication events, and system-level events. This provides authentic test data that demonstrates OpsBot's effectiveness in filtering actual production server logs.

## Author

### Completed by: [J N Ravinandan](https://github.com/Ravinandan2005)
### SRM University (Vadapalani)

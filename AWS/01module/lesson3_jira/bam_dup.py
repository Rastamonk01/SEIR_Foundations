from incident import report_incident

r = report_incident(agent='bam_dup.py', severity='ERROR',
                    message='BAM duplicate-detection test',
                    incident_id='BAM-DUP-KA-001',
                    evidence='Synthetic test only',
                    recommendation='Confirm the second run reuses the same Jira key.')
print(r)
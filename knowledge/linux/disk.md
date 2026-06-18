# Disk Troubleshooting

Disk usage is 100%

Common Commands:

df -h
du -sh /
find / -type f -size +500M

Common Causes:

- Large log files
- Docker images
- Backup files
- Application logs

Resolution:

- Delete unnecessary files
- Rotate logs
- Expand EBS volume
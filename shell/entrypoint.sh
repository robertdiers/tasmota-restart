printenv | grep -v "no_proxy" >> /etc/environment
python3 -V
cd /app
sed -i "s/PLACEHOLDER/$CRON/" /app/container_cron
echo "Cron schedule: $(cat /etc/cron.d/container_cron)"
echo 'starting cron'
cron -f
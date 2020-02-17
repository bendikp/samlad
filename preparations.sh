sudo sh tablereset.sh
sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
sudo iptables -A FORWARD -i wlan0 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i eth0 -o wlan0 -j ACCEPT

sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"
sudo sed -i  '/^exit 0.*/i iptables-restore < /etc/iptables.ipv4.nat' /etc/rc.local

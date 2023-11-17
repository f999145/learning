# Как проверить открытые порты
	
sudo apt install net-tools

sudo netstat -plnut




# Как открыть порты

```
sudo iptables -A INPUT -p tcp --dport 8888 -j ACCEPT
```
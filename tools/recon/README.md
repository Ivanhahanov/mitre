# Reconnaissance & Resource Development
## Active scanning
### Test servies
```
cd services/recon
docker-compose up -d
```
### Offense
Tools are located in `tools/reocon/` folder

For run scripts you need to install requirements
```
sudo pip3 install -r requirements
```
#### Port scan
```
sudo python3 port_scan.py <service ip> 
```
#### DNS scan
```
sudo python3 dns_scan.py <dns_ip:port> <domain_name>
```
Example
```
sudo python3 dns_scan.py 8.8.8.8:53 google.com
```

### Defence
#### DNS Honeport
Run honey dns server
```
sudo python3 honey_resolver.py
```

Run dns scan
```
sudo python3 dns_scan.py 127.0.0.1:8053 google.com
```
docker build -t w4af_dev -f extras/docker/Dockerfile .
docker run  --rm -it -p5000:5000 w4af_dev w4af_api --i-am-a-developer 0.0.0.0:5000

./w4af_api --i-am-a-developer 0.0.0.0:5000


curl -k -H "Content-Type: application/json" --location 'https://localhost:5000/scans/' \
--data '{
    "target_urls": ["https://megadescargas-new.blogspot.com/"],
    "scan_profile": "OWASP_TOP10.pw4af"
}'



curl -k -H "Content-Type: application/json" --location 'https://localhost:5000/scans/'


./w4af_api --i-am-a-developer 0.0.0.0:5000
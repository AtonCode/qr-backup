clear
echo QR Code Generator
read -p 'Ingresa el nombre del archivo: ' file
python3 main.py -f ${file} -null && python3 main.py -f ${file} -m
echo Done.
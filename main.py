from gpio import * 
//pin untuk membaca input dan mengontrol output berdasarkan kondisi yang berbeda sesuai dengan program yang telah dibuat pada Raspberry Pi
from time import * 
//untuk mengatur waktu

//berguna untuk membaca nilai hasil sensor
def handleSensorData(): 
	value = digitalRead(0)  //membaca nilai yang dihasilkan oleh pin D0 kemudian disimpan divariabel value
	if value == 0:
		customWrite(2, '0') //untuk memberikan informasi ke output device, terdapat 2 parameter
		digitalWrite(1, LOW) //mematikan sensor
		print("Tidak ada gerakan") //menyatakan bahwa ada gerakan
	else:
		customWrite(2, '1')
		digitalWrite(1, HIGH)//mnenyalakan sensor
		print("Ada gerakan")
		
		
def main():
	add_event_detect(0, handleSensorData)
	
	while True:
		delay(1000)
		
if __name__ == "__main__":
	main()

#./get_layency read/read&write path
import os
import numpy as np
import csv 

#original_path = "CDFs/nvme1n1/original/bingI"
deviceName 		= ["nvme1n1", "nvme2n1", "nvme3n1", "nvme0n1", "sdd", "sde"]
editOption	 	= ["original", "out-rerated-10.0", "out-resized-10.0", "out-rerated-100.0", "out-resized-100.0"]
traceType 		= ["bingI", "bingS", "azure", "cosmos"]
main_dir		= "CDFs"
bufferData		= [0 for i in range (27)] #27 -> total columns
#nData_perfile 	= 9

def requestType_level (file_path, first_idx, last_idx):
	if os.path.exists(file_path) :
		print (file_path)
		outfile = open(file_path,'r')
		data = outfile.readlines()
		outfile.close()
		nData_perfile = first_idx
		for line in data:
			if nData_perfile <=last_idx:
				split_line = line.split()
				value = int(split_line[-1])
				bufferData[nData_perfile-1] = value
			nData_perfile += 1
				#print(value)
		#writer.writerow(bufferData)
	else:
		nData_perfile = first_idx
		for idx in range(9):
			bufferData[nData_perfile-1] = "-"
			nData_perfile += 1
		#writer.writerow(bufferData)

def traceType_level (trace):
	requestType 	= ["_read_characteristics.txt", "_write_characteristics.txt", "_rw_characteristics.txt"]
	buff_requestType = []
	buff_requestType = requestType 
	for j in range(3):
		buff_requestType[j] = trace + buff_requestType[j]
	print(requestType)
	#print(buff_requestType)
	for edit in editOption :
		for device in deviceName :
			for request in buff_requestType :
				file_path = os.path.join(main_dir, device, edit, trace, request)
				# print (file_path)
				if request == buff_requestType[0] : 
					requestType_level(file_path, 1, 9)
				elif request == buff_requestType[1] :  
					requestType_level(file_path, 10, 18)
				else :
					requestType_level(file_path, 19, 27)
			writer.writerow(bufferData)
			#print(bufferData)

if __name__ == '__main__':
	with open('latency_data.csv', 'w', encoding='UTF8', newline='') as filehandle:
		writer = csv.writer(filehandle)
		for trace in traceType :
			traceType_level (trace)






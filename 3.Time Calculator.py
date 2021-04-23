#Time Converter from Seconds 
Time = int(input("Enter seconds: "))


if Time >= 86400:
	print ('Days:',int(Time/86400),'/Hours:',(int((Time % 86400)/3600)),'/Minutes:', (int(((Time % 86400) % 3600)/60)), '/Seconds:',
               ((Time % 86400) % 3600) % 60)
else:
	if Time >= 3600:
		print ('Hours:',(int((Time % 86400)/3600)),'Minutes:',(int(((Time % 86400) % 3600)/60)),'Seconds:',((Time % 86400) % 3600) % 60)
	else:
		if Time >= 60:
			print ('Minutes:',int(((Time % 86400) % 3600)/60),'Seconds:',((Time % 86400) % 3600) % 60)

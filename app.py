# pocket.py
# for monitoring pocket usage and updating account

# Core packages
import os
import pickle

def main():
	# Set running directory to current directory of the script
	CURRENT_DIRECTORY = os.path.dirname(__file__)
	if CURRENT_DIRECTORY:
		os.chdir(CURRENT_DIRECTORY)

	# Check to see if they've used the app before
	if not os.path.isfile("pocketpal.pkl"):
		from PocketPal import PocketPal
		pocketpal = PocketPal()
		pocketpal.initialize_pocket()
		if not pocketpal.pocket_initialized():
			print "Sorry- something went wrong :("
			return 0
		else:
			with open("pocketpal.pkl", 'wb') as savefile:
				pickle.dump(pocketpal, savefile, -1)

	with open('pocketpal.pkl', 'rb') as savefile:
		pocketpal = pickle.load(savefile)

	# Main app loop
	while True:
		next = raw_input(("What would you like to do next? "
			"(q for quit, o for options):\n>> "))
		if next == "q" or next == "quit":
			os.system('clear')
			break
		elif next == "o":
			os.system('clear')
			print ("q or quit     -> quits application \n"
"s or summary   -> Gives summary of your recent reading/saving \n"
"sc or scrape   -> Check to see if your favorite sites have put out any "
"new Content\n"
"f or favorites -> Update your \"favorite\" sites\n"
"vf or view     -> List favorite sites\n"
"c or clean     -> Remove articles added before a certain date, or a certain "
"amount of time ago\n"
"st or stats    -> Generate simple statistical summary of reading habits\n"
"j or journal   -> Give \"reading journal\" of past week (IN PROGRESS)\n"
"r or roll      -> Pulls a single random articles from many possible "
"sources \n"
"g or guess     -> Scan headlines from news api and find ones that may "
"potentially be of interest (IN PROGRESS))\n"
"ef             -> Edit favorite feeds")
		elif next == "s" or next == "summary":
			os.system('clear')
			pocketpal.recent_reading()
		elif next == "f" or next == "favorites":
			os.system('clear')
			pocketpal.add_favorites()
		elif next == "sc" or next == "scrape":
			os.system('clear')
			pocketpal.update_articles()
		elif next == "vf" or next == "view":
			os.system('clear')
			pocketpal.view_favorites()
		elif next == "c" or next == "clean":
			os.system('clear')
			pocketpal.clean_up()
		elif next == "st" or next == "stats":
			os.system('clear')
			pocketpal.reading_stats()
		elif next == "r" or next == "roll":
			os.system('clear')
			if not pocketpal.aggregator_enabled():
				pocketpal.enable_aggregator()
			else:
				pocketpal.random_article()
		elif next == "ef":
			os.system('clear')
			pocketpal.edit_favorites()
		else:
			print "Unknown or unsupported command"
	print "Saving..."
	with open("pocketpal.pkl", 'wb') as savefile:
		pickle.dump(pocketpal, savefile, -1)
	print "Saved!"

if __name__ == '__main__':
	main()







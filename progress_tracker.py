class ProgressTracker:
    def __init__(self):
        self.progress_log = []

    def create_log_entry(self):
        while True:
            try:
                day = int(input("\nEnter the day number:"))
                break
            except ValueError:
                print("Please enter a valid value")

        topic = input("\nEnter topic:")

        for entry in self.progress_log:
            if entry['day'] == day:
                entry['topics'].append(topic)
                print("\nTopic added to existing day")
                return
            
        new_entry = {'day':day,'topics':[topic]}
        self.progress_log.append(new_entry)
        print('\nNew entry created!')

    def view_log(self):
        print(f'\nCurrent progress log............')
        if len(self.progress_log)>0:
            for  e in self.progress_log:
                print(f"Day {e['day']}")
                for topic in e['topics']:
                    print(f" -> {topic}")
        else:
            print("\nNo log preserved from previous runs , add some to view.")

    def count_days(self):
        return len(self.progress_log)

    def options(self):
        print('\n1. Add entry')
        print('2. View log')
        print('3. Total number of days of work')
        print('4. Exit')

me = ProgressTracker()

while(True):
    me.options()
    try:
        choice = int(input("\nEnter a valid choice to proceed:"))
    except ValueError:
        print("Enter a number only")
        continue

    if choice == 1:
        me.create_log_entry()
    elif choice == 2:
        me.view_log()
    elif choice == 3:
        print(f'\nTotal days of progress:{me.count_days()}')
        print('Keep going👍')
    elif choice == 4:
        break
    else:
        print("\nEnter valid choice(1,2 or 3...)")
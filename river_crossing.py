class RiverRiddle:
    print 'You are taking grain, a hen, and a fox to market. You come to a river.'
    print 'In order to cross, you must use a ' \
          'small boat. You can only fit two other items in the boat with you at a time.'
    print 'If you leave the hen and grain unsupervised, then hen will eat the grain. '
    print 'If you leave the hen and fox unsupervised, the fox will eat the hen.'
    print 'How will you get everything across the river?'

    def __init__(self):
        self.river_banks = {'near_bank': ['grain', 'hen', 'fox'], 'far_bank': []}
        self.boat = []
        self.current_bank = self.river_banks['near_bank']
        self.destination = self.river_banks['far_bank']

    def win_condition(self):
        if len(self.river_banks['far_bank']) == 3:
            print('You made it across with everything intact!')
            return True
        return False

    def lose_condition(self):
        if 'hen' in self.destination:
            if 'fox' in self.destination:
                print 'The fox ate the hen!'
                return True
            if 'grain' in self.destination:
                print 'The hen ate the grain!'
                return True
        return False

    def still_playing(self):
        if not self.win_condition() and not self.lose_condition():
            return True
        return False

    def boat_action(self):
        options = {1: 'Add passenger', 2: 'Remove passenger', 3: 'Set sail'}
        if len(self.current_bank) > 0:
            print 'On shore:'
            for passenger in self.current_bank:
                print passenger
        if len(self.boat) > 0:
            print 'Aboard the boat:'
            for passenger in self.boat:
                print passenger
        print 'What next?'
        for key, value in options.items():
            print '{key}) {value}'.format(key=key, value=value)
        choice = input()
        if choice == 1:
            self.load_boat()
        elif choice == 2:
            self.unload_boat()
        elif choice == 3:
            self.set_sail()
        else:
            print 'Please choose by number'

    def load_boat(self):
        print 'Ashore:'
        for item in self.current_bank:
            print item
        if len(self.boat) > 1:
            print 'The boat is full.'
        else:
            passenger = raw_input('What will you load aboard?')
            self.boat.append(passenger)
            self.current_bank.remove(passenger)

    def unload_boat(self):
        if len(self.boat) == 0:
            print 'The boat is already empty.'
        else:
            print 'Aboard:'
            for item in self.boat:
                print item
            passenger = raw_input('What will you unload?')
            self.boat.remove(passenger)
            self.current_bank.append(passenger)

    def set_sail(self):
        for passenger in self.boat:
            self.destination.append(passenger)
        self.boat = []
        destination_holder = self.destination
        self.destination = self.current_bank
        self.current_bank = destination_holder

    def run(self):
        while self.still_playing():
            self.boat_action()


if __name__ == '__main__':
    RiverRiddle().run()

# Parking Lot Assignment
import sys
class Ticket:
    def __init__(self, slot_number, registration_number, colour):
        super().__init__()
        self.slot_number = slot_number
        self.registration_number = registration_number
        self.colour = colour
class ParkingLot():
    def __init__(self):
        super().__init__()
    def create_parking_lot(self, capacity):
        self.capacity = capacity
        self.slots = {}
        self.available_slot = [*range(1, capacity + 1)]
        return 'Create parking lot. Capacity is ' + str(capacity)

    def park(self, registration_number, colour):
        if not self.available_slot:
            return 'park '+ registration_number + ' '+ colour + ': successful. Parking lot is full'
        else:
            slot_number = self.available_slot.pop(0)
            self.slots[slot_number] = (Ticket(slot_number, registration_number, colour))
            return 'park '+ registration_number + ' '+ colour + ': successful. The number slot is ' + str(slot_number)
    def leave(self, slot_number):
        if slot_number not in self.slots:
            # print("Leave unsuccessful. The slot", str(slot_number), "doesn't have car.")
            return "Leave unsuccessful. The slot " + str(slot_number) + " doesn't have car."
        else:
            self.slots.pop(slot_number)
            self.available_slot.append(slot_number)
            self.available_slot.sort()
            # print("Leave successful. The slot", str(slot_number), "is available.")
            return "Leave successful. The slot " + str(slot_number) + " is available."
    def status(self):
        # print('Parking lot is full' if len(self.available_slot) == 0 else "Parking lot is ready")
        return 'Status: full' if len(self.available_slot) == 0 else "Status: ready"
    def slot_numbers_for_cars_with_colour(self, colour):
        result = list(map(lambda ticket: ticket.slot_number, filter(lambda x: x.colour == colour ,self.slots.values())))
        # for i in result:
        #     print(i)
        return 'slot_numbers_for_cars_with_colour ' + colour + ': '+  str(result)
    def slot_number_for_registration_number(self, registration_number):
        # result = next(filter(lambda x: x.registration_number == registration_number, self.slots.values())).get('slot_number')
        for ticket in self.slots.values():
            if ticket.registration_number == registration_number:
                result = ticket.slot_number
                # print(result)
                return 'slot_number_for_registration_number ' + registration_number + ': ' + str(result)
        return 'slot_number_for_registration_number ' + registration_number + ': not found in parking lot'
        # return 'slot_number_for_registration_number ' + registration_number + ': ' + str(result)
    def registration_numbers_for_cars_with_colour(self, colour):
        result = list(map(lambda ticket: ticket.registration_number, list(filter(lambda x: x.colour == colour, self.slots.values()))))
        result = [ ticket.registration_number for ticket in self.slots.values() if ticket.colour == colour]
        # for i in result:
        #     print(i)
        return 'registration_numbers_for_cars_with_colour ' + colour +': '+ str(result)

def printInteractiveHepl():
    print('----- Supported Commands -----')
    print("create_parking_lot <n>")
    print("park <registration_number> <colour>")
    print("leave <slot>")
    print("status")
    print("slot_numbers_for_cars_with_colour <colour>")
    print("slot_number_for_registration_number <registration_number>")
    print("registration_numbers_for_cars_with_colour <colour>")
    print("exit")
    print("help")

def InterractiveRunning():
    parkingLot = ParkingLot()
    while 1:
        command = input('>>>').split(' ')
        # reconize command
        if command[0] == 'exit':
            break
        elif command[0] == 'help':
            printInteractiveHepl()
        elif command[0] == 'create_parking_lot':
            if len(command) != 2:
                print('command is invalid. run command `help` for more info.')
                continue
            try:
                number = int(command[1])
            except ValueError:
                print('command is invalid. run command `help` for more info.')
                continue
            # run
            print(parkingLot.create_parking_lot(number))
        elif command[0] == 'park':
            if len(command) != 3:
                print('command is invalid. run command `help` for more info.')
                continue
            registration_number = command[2]
            colour = command[2]
            # run
            print(parkingLot.park(registration_number, colour))
        elif command[0] == 'leave':
            if len(command) != 2:
                print('command is invalid. run command `help` for more info.')
                continue
            try:
                slot_number = int(command[1])
            except ValueError:
                print('command is invalid. run command `help` for more info.')
                continue
            # run
            print(parkingLot.leave(slot_number))
        elif command[0] == 'status':
            if len(command) != 1:
                print('command is invalid. run command `help` for more info.')
                continue
            # run
            print(parkingLot.status())
        elif command[0] == 'slot_numbers_for_cars_with_colour':
            if len(command) != 2:
                print('command is invalid. run command `help` for more info.')
                continue
            colour = command[1]
            # run
            print(parkingLot.slot_numbers_for_cars_with_colour(colour))
        elif command[0] == 'slot_number_for_registration_number':
            if len(command) != 2:
                print('command is invalid. run command `help` for more info.')
                continue
            registration_number = int(command[1])
            # run
            print(parkingLot.slot_number_for_registration_number(registration_number))
        elif command[0] == 'registration_numbers_for_cars_with_colour':
            if len(command) != 2:
                print('command is invalid. run command `help` for more info.')
                continue
            colour = command[1]
            # run
            print(parkingLot.registration_numbers_for_cars_with_colour(colour))
        elif command[0] =='':
            continue
        else:
            print('command is invalid. run command `help` for more info.')

def FileRunning(input_filename):
    input_file = open(input_filename, 'r')
    commands = input_file.read().split('\n')
    input_file.close()

    parkingLot = ParkingLot()
    result = []
    for c in commands:
        command = c.split(' ')
        # reconize command
        if command[0] == 'create_parking_lot':
            if len(command) != 2:
                result.append('command is invalid')
                continue
            else:
                try:
                    number = int(command[1])
                except ValueError:
                    result.append('command is invalid')
                    continue
                if number %2 != 0:
                    result.append('command is invalid')
                    continue
                else:
                    # run
                    result.append(parkingLot.create_parking_lot(number))
        elif command[0] == 'park':
            if len(command) != 3:
                result.append('command is invalid')
                continue
            registration_number = command[1]
            colour = command[2]
            # run
            result.append(parkingLot.park(registration_number, colour))
        elif command[0] == 'leave':
            if len(command) != 2:
                result.append('command is invalid')
                continue
            try:
                slot_number = int(command[1])
            except ValueError:
                result.append('command is invalid')
                continue
            # run
            result.append(parkingLot.leave(slot_number))
        elif command[0] == 'status':
            if len(command) != 1:
                result.append('command is invalid')
                continue
            # run
            result.append(parkingLot.status())
        elif command[0] == 'slot_numbers_for_cars_with_colour':
            if len(command) != 2:
                result.append('command is invalid')
                continue
            colour = command[1]
            # run
            result.append(parkingLot.slot_numbers_for_cars_with_colour(colour))
        elif command[0] == 'slot_number_for_registration_number':
            if len(command) != 2:
                result.append('command is invalid')
                continue
            registration_number = command[1]
            # run
            result.append(parkingLot.slot_number_for_registration_number(registration_number))
        elif command[0] == 'registration_numbers_for_cars_with_colour':
            if len(command) != 2:
                result.append('command is invalid')
                continue
            colour = command[1]
            # run
            result.append(parkingLot.registration_numbers_for_cars_with_colour(colour))
        elif command[0] =='':
            continue
        else:
            result.append('command is invalid')
    result = list(map(lambda line: line + '\n' , result))
    result[-1] = result[-1][:-1]
    output_file_name = input_filename[:-4]+'_result'+input_filename[-4:]
    output_file = open(output_file_name,'w')
    output_file.writelines(result)
    output_file.close()
    print('Running complete. Output is recorded in', output_file_name)
    return ''.join(result)

def runTest(input_file, out_expect_file):
    output = FileRunning(input_file)
    f = open(out_expect_file,'r')
    out_expect = f.read()
    return output == out_expect

def main(argv):
    if len(argv) < 1:
        # Running the application in Interactive mode:
        InterractiveRunning()
    elif len(argv) == 1:
        # Running the application in File mode:
        input_file = argv[0]
        FileRunning(input_file)
    elif len(argv) == 3 and argv[0] == 'test':
        print('Test','OK' if runTest(argv[1], argv[2]) else 'FAIL')
    else:
        printUsage()

def printUsage():
    print('python ./ParkingLot.py input.txt')
    print('python ./ParkingLot.py')
    print('python ./ParkingLot.py test input.txt expect.txt')
if __name__ == '__main__':
    main(sys.argv[1:])
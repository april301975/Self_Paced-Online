#!/usr/bin/env python3

# new file for lesson 6 work to do unit tests.

ddonors = {"Manny Machado": [12.2,2.51,3.20],
            "Adam Jones": [1024.14,22.21,323.45],
            "Chris Davis": [3.2,5.55,4.20]}


def display_list():    
    for name in ddonors.keys():
        print(name)


def write_letter(name,amount):
    line_one = 'Dear {},'.format(name)
    line_two = "Thank you for donating ${:.2f} to the Human Fund. Your money will be used appropriately.".format(amount)
    letter = line_one + "\n" + line_two
    return letter


def write_report(donors):
    print('Donor Name                | Total Given | Num Gifts | Average Gift')
    print('-'*67)
    for i in donors:
        print('{1:27}${0:11.2f}{2:12}  ${3:12.2f}'.format(*i))


def thank_you():
    """Function to send a thank you letter."""
    while True:
        input_name = input("Enter full name: ")
        if input_name in ddonors.keys():
            while True:
                try:
                    donation = float(input("Enter donation amount:"))
                except ValueError:
                    print("Donation needs to be a number.")
                else:
                    break
            ddonors[input_name].append(donation)
            print(write_letter(input_name,donation))
            break
        elif input_name == 'list':
            display_list()
            
        else:
            print("Adding {} to donor database".format(input_name))
            while True:
                try:
                    donation = float(input("Enter donation amount:"))
                except ValueError:
                    print("Donation needs to be a number.")
                else:
                    break
            ddonors[input_name] = [donation]
            print(write_letter(input_name,donation))
            #print(ddonors)
            break


def create_report():
    """Function to write a report of the donors."""
    donors_report = []
    for name, amount in ddonors.items():
        sum_donation = 0
        avg_donation = 0
        for i in amount:
            sum_donation = sum_donation + i
            num_donation = len(amount)
        avg_donation = sum_donation/num_donation
        donors_report.append([sum_donation, name, num_donation, avg_donation])
    donors_report.sort(reverse=True)
    write_report(donors_report)


def all_letters():
    """Function to write letters for everyone."""
    for name in ddonors:
        donation = ddonors[name][0]
        with open('{}.txt'.format(name), 'w') as f:
            f.write(write_letter(name, donation))
    print("Letter files created.")


def challenge(donor_dict,factor):
    """Function to multiply the donations by all donors by a factor"""
    donors_2 = {}
    for k,v in donor_dict.items():
        donors_2[k] = list(map(lambda x:x*factor,v))
    return donors_2


def filter_donations(**kwargs):
    """
    Function creates a donor dict of only donations above or below a specified value.

    Args:
        above: Use to get donations above parameter.
        below: Use to get donations below parameter.
    """

    donors_2 = {}
    if 'above' in kwargs:
        for k,v in ddonors.items():
            donors_2[k] = list(filter(lambda x: x>kwargs.get('above'),v))
    
    if 'below' in kwargs:
        for k,v in ddonors.items():
            donors_2[k] = list(filter(lambda x: x<kwargs.get('below'),v))
    return donors_2


def projection_calc(fact, **kwargs):
    """
    Function returns a total donation about for the rich guy.

    Args:
        fact: factor to multiply donations by.
        above: Use to get donations above parameter. ~OR~
        below: Use to get donations below parameter.
    """  
    # Calculates the total amount of multiplied donations.
    donors_after = {}
    donors_after = challenge(filter_donations(**kwargs),fact)
    total_a = 0
    for k,v in donors_after.items():
        total_a = sum(v,total_a)

    # Calculates the sum of the donations that are being matched.
    donors_filtered = {}
    donors_filtered = filter_donations(**kwargs)
    total_f = 0
    for k,v in donors_filtered.items():
        total_f = sum(v,total_f)
    return total_a - total_f


def projection():
    factor = input("How much to you want to multiply donations by? ")
    up_down = int(input("Do you want to match donations 1: above or 2: below a value? (Enter 1 or 2) "))
    threshold = input("At what value do you want to match donations {}? ".format(up_down))
    
    if up_down == 1:
        total = projection_calc(float(factor),above=float(threshold))
    if up_down == 2:
        total = projection_calc(float(factor),below=float(threshold))
    print("You will donate ${:.2f} under this plan.".format(total))



if __name__ == "__main__":
    main_switch_function = {"1": thank_you, "2": create_report, "3": all_letters, "4": projection, "5": exit}
    while True:
        print("What do you want to do?")
        response = input("1. Send a Thank You, 2. Create a Report, 3. Send all letters, 4. Projection, 5. Quit: ")
        try:
            main_switch_function.get(response)()
        except TypeError:
            print("Not a valid input.")
#script to find valve shim thickness on a 2zz-ge engine with preset parameters

def calculate_new_shim_thickness(thickness_used_shim, measured_clearance, valve_type):
    if valve_type.lower() == 'intake':
        target_clearance = 0.0051  # Target clearance for intake valve in inches
    elif valve_type.lower() == 'exhaust':
        target_clearance = 0.0106  # Target clearance for exhaust valve in inches
    else:
        return None  # Invalid valve type

    new_thickness = thickness_used_shim + (measured_clearance - target_clearance) * 1.5
    return new_thickness

def select_shim_size(new_thickness):
    min_thickness = 0.0787  # Minimum thickness of available shims in inches
    max_thickness = 0.1102  # Maximum thickness of available shims in inches
    increment = 0.0008  # Increment between available shim sizes in inches

    closest_size = min_thickness
    min_difference = abs(min_thickness - new_thickness)

    for size in range(int(min_thickness * 10000), int((max_thickness + increment) * 10000), int(increment * 10000)):
        current_thickness = size / 10000
        difference = abs(current_thickness - new_thickness)
        if difference < min_difference:
            min_difference = difference
            closest_size = current_thickness

    return closest_size

def main():
    ascii = r"""
     ____                ____ _____
    |___ \ ________     / ___| ____|
      __) |_  /_  /____| |  _|  _|
     / __/ / / / /_____| |_| | |___
    |_____/___/___|     \____|_____|
    """
    print(ascii)

    intake_valves = int(input("Number of Intake valves: "))
    exhaust_valves = int(input("Number of Exhaust valves: "))

    for i in range(intake_valves):
        print(f"\nIntake Valve {i+1}:")
        thickness_used_shim = float(input("Thickness of used shim (in): "))
        measured_clearance = float(input("Measured valve clearance (in): "))
        new_thickness = calculate_new_shim_thickness(thickness_used_shim, measured_clearance, 'intake')
        closest_size = select_shim_size(new_thickness)
        print(f"Thickness of new shim: {new_thickness:.7f} in")
        print(f"Selected shim size: {closest_size:.4f} in")

    for i in range(exhaust_valves):
        print(f"\nExhaust Valve {i+1}:")
        thickness_used_shim = float(input("Thickness of used shim (in): "))
        measured_clearance = float(input("Measured valve clearance (in): "))
        new_thickness = calculate_new_shim_thickness(thickness_used_shim, measured_clearance, 'exhaust')
        closest_size = select_shim_size(new_thickness)
        print(f"Thickness of new shim: {new_thickness:.7f} in")
        print(f"Selected shim size: {closest_size:.4f} in")

main()

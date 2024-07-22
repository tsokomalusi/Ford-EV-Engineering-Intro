from pid import PID

# Initialize the PID controller with initial gains
pid_controller = PID(P=0.2, I=0.02, D=0.1)

# Setpoint is the desired position
setpoint_position = 100

# Initialize variables for tracking changes
previous_error = 0
integral = 0

# Iterate over time
for t in range(1, 100):

# Current position feedback from the robot
current_position = 90 + t  # Simulating a change in position

# Calculate the error
error = setpoint_position - current_position

# Update the integral term
integral += error

# Calculate the control output
control_output = pid_controller(error, integral - previous_error, error - previous_error)

# Update the previous error for the next iteration
previous_error = error

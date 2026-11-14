# Simple Pendulum Motion Simulator
#### Video Demo: <https://youtu.be/WUojA1nCVbo>

## Description:
This project is based on a simple pendulum simulation. It can calculate the different parameters of a pendulum depending on the initial input and the command-line arguments.
Moreover, it has an implemented function that generates two different graphs showing how these parameters relate over time.

## Project Files
- **`project.py`**: This file contains different libraries that will be explained in the requirements.txt section. It starts with the main() function, which asks for the input of various physical parameters (mass, length, gravity, and initial angle in degrees). Additionally, this function detects if the inputs are correct (if not, it raises a SystemExit) and finally prints the results for the following variables: angular velocity, linear velocity, oscillation period, kinetic energy, and potential energy.

   The next function, check_argv(), is responsible for checking the command-line arguments. Furthermore, it gets the time necessary for the next calculations. If a command-line argument is wrong, it raises a SystemExit.

    Following this, the file contains other functions responsible for calculating the values of some physical equations. For example, E_pot_calculator is responsible for calculating the potential energy (with the degrees to radians transformation). Another one is period_calculator, which is used to calculate the oscillation period using length and gravity.

    Additionally, this file includes a function that calculates the angular displacement over time based on the initial angle, gravity, pendulum length, and time.

    Finally, it implements a visualization function using Matplotlib to plot both kinetic and potential energy against time, allowing users to clearly observe the conservation and continuous transformation of mechanical energy throughout the pendulum's oscillatory motion.


- **`test_project.py`**: This file serves as the unit testing suite for the project, using the pytest library to rigorously test and validate the primary functions defined in project.py.

     It includes test_check_argv() to verify that command-line input parsing works correctly, asserting expected values for valid arguments and ensuring that improper inputs, such as missing, excessive, or negative parameters, properly trigger a SystemExit exception using pytest.raises().

    Additionally, it provides individual test functions—such as test_vel_ang_calculator(), test_vel_lin_calculator(), test_period_calculator(), test_E_cin_calculator(), test_E_pot_calculator(), and test_theta_t_calculator()—to confirm the mathematical accuracy of all physical equations by making assertions against valid and invalid results using the round() function where precision floating-point comparison is required.

- **`requirements.txt`**:
    pytest: Used to perform automated unit testing, ensuring that the code functions correctly and handles errors as expected.

    matplotlib: Responsible for creating and displaying the physical graphs and visual representations of the simulation over time.

    sys: Used to interact with the system, specifically to handle command-line arguments and manage program termination or system errors.

    math: Provides the necessary mathematical functions and constants required to perform the physical calculations of the pendulum.

## Design Decisions
To enhance the overall presentation, clarity, and organization of the project, I decided to save the generated graphs directly as external .png image files rather than displaying them in temporary runtime windows. Exporting the plots to static .png files ensures that the output data remains permanently accessible for post-execution analysis, prevents cluttering the screen during program execution, and keeps the entire project directory neatly structured, allowing anyone reviewing the code to easily inspect the graphical results independently and with total visual clarity.


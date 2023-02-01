import numpy as np
import matplotlib.pyplot as plot

def multiply():

  # Add seed for replicability.
  np.random.seed(64)

  # Create first matrix.
  A = np.random.random((10**6, 10**3))
  
  # Uncomment to show CDF plot for matrix A
  #cdf_plotter(A, 'A')

  # Create second matrix.
  B = np.random.random((10**3, 10**6))

  # Create third matrix.
  C = np.random.random((10**6, 1))

  # Multiply second and third matrix.
  BC = B@C

  # Multiply result of earlier operation with first matrix.
  D = A@BC

  # Return shape of the final matrix.
  return D.shape

# Helper function for plotting CDF
def cdf_plotter(matrix, name):
  # Cumulative sum of matrix
  matrix_cdf = np.cumsum(matrix)

  # Take every thousandth value to plot
  every_thousandth_value = matrix_cdf[0::1000]

  # Create and show plot
  plot.plot(every_thousandth_value)
  plot.title(f'CDF of matrix {name}')
  plot.show()

def main():
  # Call function responsible for matrix creation
  print(multiply())


# Execute program
main()
def read(input):
  output = []
  with open(input) as f:
    for line in f:
      l = line.rstrip().split(',')
      l = (int(l[0]), int(l[1]), int(l[2]))
      output.append(l)
  return output

def calculate_total_surface_area(pixels):
  # Initialize a counter for the total surface area
  total_surface_area = 0

  # Initialize a set to store the pixels that have already been processed
  processed_pixels = set()

  # Iterate over the pixels in the chunk
  for pixel in pixels:
    # Skip pixels that have already been processed
    if pixel in processed_pixels:
      continue

    # Add the surface area of the current pixel to the total surface area
    total_surface_area += 6

    # Explore the neighboring pixels
    for neighbor in get_neighbors(pixel):
      # If the neighbor is also in the chunk, subtract its surface area from the total surface area
      # to account for shared surfaces
      if neighbor in pixels:
        total_surface_area -= 1

    # Mark the current pixel as processed
    processed_pixels.add(pixel)

  return total_surface_area

def get_neighbors(pixel):
  # Convert the coordinates to integers
  x, y, z = pixel

  # Return the coordinates of the neighboring pixels
  return [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)]

if __name__ == '__main__':
  # Read the input
  pixels = read('input.txt')

  # Calculate the total surface area
  total_surface_area = calculate_total_surface_area(pixels)

  # Print the result
  print(total_surface_area)
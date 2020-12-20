import numpy as np

def parse_tile(chunk):
  split_chunk = chunk.split('\n')
  header = split_chunk[0]
  tile_id = int(header.split(' ')[1].rstrip(':'))

def main():
  input_filename = 'input.txt'
  tiles = {}
  with open(input_filename, 'r') as input:
    input_string = input.read()
    input_split = input_string.split('\n\n')
    for chunk in input_split:
      tile, tile_id = parse_tile(chunk)
      tiles[tile_id] = tile

if __name__ == "__main__":
  main()

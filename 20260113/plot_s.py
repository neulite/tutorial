import pandas as pd
import matplotlib.pyplot as plt
import sys

def main():
    # Check if at least one file is provided as an argument
    if len(sys.argv) < 2:
        print("Usage: python plot_s.py <file1.dat> <file2.dat> ...")
        return

    plt.figure(figsize=(12, 6))

    # Iterate through all files provided in command line arguments
    for i, filename in enumerate(sys.argv[1:]):
        try:
            # Read data using pandas
            # sep=r'\s+' handles one or more whitespace characters as delimiters
            df = pd.read_csv(filename, sep=r'\s+', header=None, names=['Time', 'NeuronID'])
            
            # Plot each file's data
            plt.scatter(df['Time'], df['NeuronID'], s=5, label=filename, alpha=0.7)
            
            print(f"Successfully loaded: {filename} ({len(df)} spikes)")
            
        except Exception as e:
            print(f"Error: Could not read file {filename}. Reason: {e}")

    # Set plot labels and visual styles
    plt.xlabel('Time (ms)')
    plt.ylabel('Neuron ID')
    plt.legend(loc='upper right', markerscale=5)
    plt.grid(True, linestyle=':', alpha=0.5)
    
    plt.tight_layout()
    
    # Save the output as a PNG file
    output_filename = "plot_s.png"
    plt.savefig(output_filename, dpi=300)
    print(f"File saved as: {output_filename}")

    # Show the final plot
    plt.show()

if __name__ == "__main__":
    main()

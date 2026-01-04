import pandas as pd
import matplotlib.pyplot as plt
import sys

def main():
    # Check if at least one file is provided as an argument
    if len(sys.argv) < 2:
        print("Usage: python plot_v.py <file1.dat> <file2.dat> ...")
        return

    plt.figure(figsize=(10, 6))

    # Iterate through all files provided in command line arguments
    for filename in sys.argv[1:]:
        try:
            # Read data using pandas
            # sep=r'\s+' handles one or more whitespace characters as delimiters
            df = pd.read_csv(filename, sep=r'\s+', header=None, names=['Time', 'Value'])
            
            # Plot each file's data
            plt.plot(df['Time'], df['Value'], label=filename, alpha=0.8)
            print(f"Successfully loaded: {filename}")
            
        except Exception as e:
            print(f"Error: Could not read file {filename}. Reason: {e}")

    # Set plot labels and visual styles
    plt.xlabel('Time (ms)')
    plt.ylabel('Membrane potential (mV)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    
    # Save the output as a PNG file
    output_filename = "plot_v.png"
    plt.savefig(output_filename, dpi=300)
    print(f"File saved as: {output_filename}")

    # Show the final plot
    plt.show()

if __name__ == "__main__":
    main()

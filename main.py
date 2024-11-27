import os
import subprocess

#Step 1: User input protein family and taxonomic group
print("This is the system that analyse the level of conservation between the protein sequences of your "
      "chosen protein family within a taxonomic group.")

protein = input("Please enter the protein family thet you are interested: ")
taxonomy = input("Please enter the taxonomic group you would like to search: ")

query = protein + " [PROT] AND " + taxonomy + " [ORGANISM]"

#print(query)

#Step 2: Obtain relevant protein sequence data
#subprocess.call(f"esearch -db protein -query \"{query}\" | "
#                f"efetch -format fasta > sequence.fasta", shell=True)

#sequences = subprocess.run(["esearch", "-db", "nucleotide", "-query", protein],
#                           capture_output=True, shell=True)

with open("sequence.fasta") as file:
      sequence = file.read()

number_of_sequences = 0

for i in sequence:
      if i == ">":
            number_of_sequences += 1
      else:
            continue

print("The search through NCBI database returns a total of", number_of_sequences, "sequences")

#Step 3: Decision to check so that sequences are possibly below 1,000

if number_of_sequences > 1000:
      print("The number of sequences is above 1000 and it may take significant amount of time to complete the search.")

      while True:
            decision = input("Do you wish to continue? (Please enter Yes or No)")
            if decision == "Yes" or decision == "yes" or decision == "Y":
                  break
            elif decision == "No" or decision == "no" or decision == "N":
                  os.execv(sys.executable, ['python'] + sys.argv)
            else:
                  print("Invalid input! Please enter Yes or No.")
else:
      print("The number of sequences is within the acceptable range.")


#Step 4: Do clustalo and obtain level of conservation (plot)

subprocess.call("clustalo -i \"sequence.fasta\" -o \"clustalo_aligned.aln\" --force --threads=10 ", shell = True)

subprocess.call("plotcon -sequences clustalo_aligned.aln -graph ps -graph x11", shell = True)

subprocess.call("plotcon -sequences aligned_sequences.aln -graph png -gtitle Conservation_Plot "
                "-gdirectory . -goutfile plot.png", shell = True)


#Step 5: Do BLAST to scan protein sequence with motifs (PROSITE databas)


#glucose-6-phosphatase in birds (Aves)
#Remember to include error trap


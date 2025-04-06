# 🧬 Hamming Distance Calculator (DNA Strings)

This Python script calculates the **Hamming distance** between two DNA strings of equal length. The Hamming distance is defined as the number of differing positions between two strings.

---

## 📁 Input

The input must be provided in a text file named `dna.txt`, with the following format:

GAGCCTACTAACGGGAT 
CATCGTAATGACGGCCT

Each line represents a DNA string. Both strings **must** be of equal length and contain only the nucleotides: A, T, C, G.

---

## 🚀 How to Run

1. Clone the repository or download the script.
2. Make sure `dna.txt` is in the same directory as the script.
3. Run the Python script:

```bash
python hamming_distance.py
________________________________________
🧪 Sample Output
Hamming Distance: 7
________________________________________
🛠️ Code Explanation
•	The script reads the two DNA strings from dna.txt.
•	It strips any trailing newline or space characters.
•	It uses zip() to compare characters at the same position in both strings.
•	For every mismatch, the counter is incremented.
•	Finally, the Hamming distance is printed.
________________________________________
✅ Requirements
•	Python 3.x
•	A properly formatted dna.txt file
________________________________________
📄 License
This project is open-source and available under the MIT License.
________________________________________
🤝 Contributing
Contributions, suggestions, and improvements are welcome!
Feel free to open issues or submit a pull request.

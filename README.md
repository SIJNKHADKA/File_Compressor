# File_Compresso# File Compressor Using Huffman Coding

A lightweight and efficient file compression tool that utilizes Huffman Coding, a lossless data compression algorithm, to reduce the size of files. This project implements both compression and decompression functionality, making it easy to compress files and retrieve the original data seamlessly.



 Features

- Efficient Compression**: Reduces file sizes using the Huffman Coding algorithm.
- Lossless Compression**: Ensures that no data is lost during compression.
- Custom File Support**: Supports various file types (e.g., text, binary).
- Easy-to-Use Interface**: Simple command-line interface for compression and decompression.



How It Works

Huffman Coding is a method of lossless data compression that assigns variable-length codes to input characters, with shorter codes assigned to more frequent characters.

Steps:
1. Analyze the frequency of characters in the input file.
2. Construct a Huffman Tree based on character frequencies.
3. Generate Huffman Codes from the tree.
4. Replace characters in the input file with their corresponding Huffman Codes to create the compressed file.
5. To decompress, the process is reversed using the Huffman Tree.



## Installation

 Prerequisites
- Python 3.x




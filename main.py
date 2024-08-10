
import os
from heaps import heappush, heappop

class compress:
    def __init__(self):
        self.heapQueue=[]
        self.codeDict={}

    class heap_node:
        def __init__(self,character,freq):
            self.character=character
            self.frequency=freq
            self.rightChild=None
            self.leftChild=None

        def __lt__(self,anotherClass):
            return self.frequency<anotherClass.frequency
        
        def __eq__(self,anotherClass):
            if(anotherClass==None):
                return False

            if(not isinstance(anotherClass,self)):
                return False

            return self.frequency==anotherClass.frequency

    def calcFrequency(self,Texts):
        #calculate frequency dictionary of texts
        frequencyDict={}

        for character in Texts:
            if character in frequencyDict:
                frequencyDict[character]+=1
            else:
                frequencyDict[character]=0
        return frequencyDict
        
    def heapify(self,frequency,Texts):
        #make proriy queue and return it

        for key in frequency:
            heapNode=self.heap_node(key,frequency[key])
            heappush(self.heapQueue,heapNode)
        return self.heapQueue
    
    def huffmanTree(self):
        #make huffman tree
        while(len(self.heapQueue)>1):
            node1=heappop(self.heapQueue)
            node2=heappop(self.heapQueue)

            huffman_tree=self.heap_node(None,node1.frequency + node2.frequency)
            huffman_tree.leftChild=node1
            huffman_tree.rightChild=node2

            heappush(self.heapQueue,huffman_tree)

    def makeCode(self):
        #make unique codes for characters
        rootNode=heappop(self.heapQueue)
        self.makeCodeForNodes(rootNode,"")
            
            
    def makeCodeForNodes(self,node,currentCode):
        if(node == None):
            return 
        if(node.character!=None):
            self.codeDict[node.character]=currentCode

        self.makeCodeForNodes(node.leftChild,currentCode + "0")
        self.makeCodeForNodes(node.rightChild,currentCode + "1")
            
    
    def encodeText(self,Texts):
        #replace characters with code and replace it

        encodedText=""
        for characters in Texts:
            encodedText+=self.codeDict[characters]
        return encodedText

    def padText(self,encodedTexts):
        #if overall length of Texts is not multiple of 8 add padding to text
        extraPaddingText= 8- len(encodedTexts) % 8
        for index in range(extraPaddingText):
            encodedTexts+="0"
        #Add the number of padding lenth to the text for decompression
        extraPaddingInfo= "{0:08b}".format(extraPaddingText)
        
        encodedTexts+=extraPaddingInfo
        
        return encodedTexts

    def getInByte(self,paddedText):
        #convert the padded encoded text into byte form and return it
        byteArray=bytearray()

        for index in range(0,len(paddedText),8):
            ByteArray=paddedText[index:index+8]
            byteArray.append(int(ByteArray,2))
        return byteArray
        

    def compressor(self,filePath):
        """This section compresses the file"""
        fileName,fileExtention=os.path.splitext(filePath)
        outputFilePath=fileName + ".bin"
        
        
        with open(filePath,"rb") as file, open(outputFilePath,"wb") as outputFile:


            
            binaryfileText=file.read()
            binaryfileText=binaryfileText.rstrip()

            frequency = self.calcFrequency(binaryfileText)

            self.heapify(frequency,binaryfileText)

            self.huffmanTree()
            self.makeCode()

            encodedText=self.encodeText(binaryfileText)
            paddedEncodedText=self.padText(encodedText)

            paddedEncodedTextByte=self.getInByte(paddedEncodedText)
            """lenth of code in 00000012"""
            revCodeDict= {v:k for k,v in self.codeDict.items()}
            lenth_to_be_added=8-len(str(len(str(revCodeDict))))
            lengthofCodeIn8digit=str(len(str(revCodeDict)))

            for index in range(lenth_to_be_added):
                lengthofCodeIn8digit= "0"+ lengthofCodeIn8digit

            toAddCodeDict=lengthofCodeIn8digit+str(revCodeDict)
            outputFile.write(toAddCodeDict.encode())

            outputFile.write(bytes(paddedEncodedTextByte))



            """         The file is in format 
            ---------------------------------------------------------------------------------------------------------------------
            (codeDictionary for converting in huffman code stored in binary format only no huffman code used for this)+(length of codeDictionary added ) + (huffman code values for file in binary format)+(0's to complete in 8 bit format)+(no of 0's added in 8 bit binary format eg:00001101))
            ---------------------------------------------------------------------------------------------------------------------

            here codeDictionary is in format:
            codeDictionary ={101: \'000\', 105: \'001\', 98: \'010000\', 44: \'010001\', 33: \'01001000\', 78: \'0100100100\', 81: \'0100100101\', 68: \'0100100110\', 84: \'010010011100\', 70: \'010010011101\', 79: \'01001001111\', 104: \'01001010\', 80: \'01001011000\', 77: \'01001011001\', 69: \'0100101101\', 65: \'0100101110\', 67: \'01001011110\', 83: \'01001011111\', 102: \'0100110\', 46: \'01001110\', 120: \'01001111\', 111: \'0101\', 99: \'01100\', 112: \'01101\', 115: \'0111\', 32: \'100\', 116: \'1010\', 100: \'10110\', 108: \'10111\', 117: \'1100\', 97: \'1101\', 113: \'111000\', 63: \'111001000\', 73: \'11100100100\', 82: \'11100100101\', 66: \'1110010011000\', 85: \'11100100110010\', 72: \'11100100110011\', 76: \'111001001101\', 86: \'11100100111\', 103: \'11100101\', 118: \'1110011\', 110: \'11101\', 114: \'11110\', 109: \'11111\'}

            where \ =Tokenization is skipped for long lines for performance reasons. This can be configured via editor.maxTokenizationLineLength.(as it says from output)


            sample from sample.bin
            00000738{101: \'000\', 105: \'001\', 98: \'010000\', 44: \'010001\', 33: \'01001000\', 78: \'0100100100\', 81: \'0100100101\', 68: \'0100100110\', 84: \'010010011100\', 70: \'010010011101\', 79: \'01001001111\', 104: \'01001010\', 80: \'01001011000\', 77: \'01001011001\', 69: \'0100101101\', 65: \'0100101110\', 67: \'01001011110\', 83: \'01001011111\', 102: \'0100110\', 46: \'01001110\', 120: \'01001111\', 111: \'0101\', 99: \'01100\', 112: \'01101\', 115: \'0111\', 32: \'100\', 116: \'1010\', 100: \'10110\', 108: \'10111\', 117: \'1100\', 97: \'1101\', 113: \'111000\', 63: \'111001000\', 73: \'11100100100\', 82: \'11100100101\', 66: \'1110010011000\', 85: \'11100100110010\', 72: \'11100100110011\', 76: \'111001001101\', 86: \'11100100111\', 103: \'11100101\', 118: \'1110011\', 110: \'11101\', 114: \'11110\', 109: \'11111\'}.....................xc7\x95\x19\xae\xf9\xf1\xdblsP\xda\x1b\xdf?8\xcd\xfc\xdb\x9e0\xd9"%\x85\xf7\x95\x18\xe2\xc9\xc0\x05
            """

    def decompressor(self,filePath):
        """This section compresses the file"""
        fileName,fileExtention=os.path.splitext(filePath)
        outputFilePath=fileName + "_decompressed.txt"
        with open(filePath,'rb') as file, open(outputFilePath,'x') as file2:
            chunk = file.read(8)
            dictLen = int(chunk.decode('utf-8'))
            encodingDictStr = file.read(dictLen)
            encodingDict = eval(encodingDictStr.decode('utf-8'))
            readBin = bin(int(file.read().hex(),16))[2:]
            readBin = readBin[:-(8+int(readBin[-8:],2))]

            minLen = len(min(encodingDict,key=len))
            maxLen = len(max(encodingDict,key=len))

            ind = 0
            decodedStr = ''
            while ind<len(readBin):
                for i in range(minLen,maxLen+1):
                    enc = readBin[ind:ind+i] 
                    if enc in encodingDict:
                        decodedStr += chr(encodingDict[enc]) 
                        ind = ind+i
                        break
            file2.write(decodedStr)



if __name__ == '__main__':
    # This code won't run if this file is imported.
    # path="c:\\Users\\Dell\\Desktop\\DSA\\Project\\File-Compressor\\sample.txt"
    #   Dont try to run with this path .... :-) ,change path as per your pc  
    # compressFile=compress(path)
    # compressFile.compressor()
    pass
